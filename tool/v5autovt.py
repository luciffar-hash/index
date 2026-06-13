import sys
import json
import os
import asyncio
import traceback
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, 
                             QHeaderView, QPlainTextEdit, QMessageBox, QLabel, QDoubleSpinBox)
from PySide6.QtCore import QThread, Signal, Slot, Qt, QTimer
from playwright.async_api import async_playwright

CONFIG_FILE = "config.json"

class MonitorWorker(QThread):
    status_update = Signal(int, str, str)
    error_signal = Signal(str)
    task_finished = Signal()

    def __init__(self, urls):
        super().__init__()
        self.urls = urls

    def run(self):
        try:
            asyncio.run(self.async_monitor())
        except Exception as e:
            self.error_signal.emit(traceback.format_exc())
        finally:
            self.task_finished.emit()

    async def async_monitor(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True) 
            for i, url in enumerate(self.urls):
                try:
                    context = await browser.new_context()
                    page = await context.new_page()
                    
                    await page.goto(url, wait_until="networkidle", timeout=20000)
                    
                    wake_up_btn = page.get_by_role("button", name="Yes, get this app back up!")
                    if await wake_up_btn.is_visible():
                        await wake_up_btn.click()
                        await page.wait_for_timeout(5000) 
                        self.status_update.emit(i, url, "Woken Up!")
                    else:
                        self.status_update.emit(i, url, "Already Active")
                        
                    await context.close()
                except Exception as e:
                    self.status_update.emit(i, url, f"Failed: {type(e).__name__}")
            await browser.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("路西法智庫-網站自動喚醒系統 v5.0.0")
        self.resize(700, 600)

        main_widget = QWidget()
        layout = QVBoxLayout(main_widget)

        # 頂部狀態與設定區域
        top_layout = QHBoxLayout()
        self.info_label = QLabel("模式：手動模式 (未啟動自動循環)")
        self.info_label.setStyleSheet("font-weight: bold; color: #555555;")
        top_layout.addWidget(self.info_label)
        
        top_layout.addStretch()
        
        # 新增手動設定循環時間元件
        timer_label = QLabel("循環間隔 (小時):")
        top_layout.addWidget(timer_label)
        
        self.time_spinner = QDoubleSpinBox()
        self.time_spinner.setRange(0.01, 168.0) # 最短約 36 秒，最長 1 週
        self.time_spinner.setValue(5.0)        # 預設 5 小時
        self.time_spinner.setDecimals(2)       # 支援兩位小數
        self.time_spinner.setSingleStep(0.5)
        self.time_spinner.setFixedWidth(80)
        top_layout.addWidget(self.time_spinner)
        
        layout.addLayout(top_layout)

        # 輸入框
        self.input_area = QPlainTextEdit()
        self.input_area.setPlaceholderText("請貼上網址，一行一個")
        layout.addWidget(self.input_area)

        # 控制按鈕
        self.btn_run = QPushButton("執行單次喚醒")
        self.btn_run.setStyleSheet("background-color: #2196F3; color: white; font-weight: bold; height: 30px;")
        self.btn_run.clicked.connect(self.run_single_task)
        layout.addWidget(self.btn_run)

        self.btn_loop = QPushButton("啟動自動循環機制")
        self.btn_loop.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; height: 30px;")
        self.btn_loop.clicked.connect(self.toggle_loop_mode)
        layout.addWidget(self.btn_loop)

        # 狀態表
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["目標 URL", "目前狀態"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.table)

        self.setCentralWidget(main_widget)

        self.loop_timer = QTimer(self)
        self.loop_timer.timeout.connect(self.execute_task_core)
        self.is_loop_active = False

        # 啟動時自動讀取歷史列表與時間設定
        self.load_config()

    def load_config(self):
        """讀取本地的 config.json 檔案"""
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    urls = data.get("urls", [])
                    interval = data.get("interval", 5.0)
                    if urls:
                        self.input_area.setPlainText("\n".join(urls))
                    self.time_spinner.setValue(interval)
            except Exception:
                pass

    def save_config(self, urls):
        """保存當前的網址清單與時間到 config.json"""
        try:
            interval = self.time_spinner.value()
            with open(CONFIG_FILE, "w", encoding="utf-8") as f:
                json.dump({"urls": urls, "interval": interval}, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"儲存設定檔失敗: {e}")

    def run_single_task(self):
        if self.is_loop_active:
            QMessageBox.information(self, "提示", "目前處於自動循環模式，程式將依排程自動執行。")
            return
        self.execute_task_core()

    def toggle_loop_mode(self):
        urls = [line.strip() for line in self.input_area.toPlainText().splitlines() if line.strip()]
        if not urls:
            QMessageBox.warning(self, "警告", "請先輸入網址再啟動循環機制。")
            return

        # 同步儲存設定
        self.save_config(urls)

        if not self.is_loop_active:
            self.is_loop_active = True
            
            # 取得當前設定的小時數並轉換為毫秒
            hours = self.time_spinner.value()
            ms_interval = int(hours * 60 * 60 * 1000)
            
            self.btn_loop.setText(f"停止自動循環機制 (每 {hours} 小時)")
            self.btn_loop.setStyleSheet("background-color: #f44336; color: white; font-weight: bold; height: 30px;")
            self.input_area.setEnabled(False)
            self.btn_run.setEnabled(False)
            self.time_spinner.setEnabled(False)
            
            self.execute_task_core()
            self.loop_timer.start(ms_interval) 
        else:
            self.is_loop_active = False
            self.loop_timer.stop()
            self.btn_loop.setText("啟動自動循環機制")
            self.btn_loop.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; height: 30px;")
            self.input_area.setEnabled(True)
            self.btn_run.setEnabled(True)
            self.time_spinner.setEnabled(True)
            self.info_label.setText("模式：手動模式 (未啟動自動循環)")

    def execute_task_core(self):
        urls = [line.strip() for line in self.input_area.toPlainText().splitlines() if line.strip()]
        if not urls:
            return

        self.save_config(urls)

        if self.is_loop_active:
            self.info_label.setText(f"模式：自動循環中... [正在執行 {self.time_spinner.value()} 小時週期任務]")
        else:
            self.info_label.setText("模式：手動模式... [正在執行喚醒任務]")

        self.btn_run.setEnabled(False)
        self.table.setRowCount(0)
        self.table.setRowCount(len(urls))
        
        self.worker = MonitorWorker(urls)
        self.worker.status_update.connect(self.update_row_status)
        self.worker.error_signal.connect(self.handle_critical_error)
        self.worker.task_finished.connect(self.on_worker_finished)
        self.worker.start()

    @Slot(int, str, str)
    def update_row_status(self, row, url, status):
        url_item = QTableWidgetItem(url)
        status_item = QTableWidgetItem(status)
        
        if status == "Woken Up!":
            status_item.setForeground(Qt.green)
        elif status == "Already Active":
            status_item.setForeground(Qt.blue)
        elif "Failed" in status:
            status_item.setForeground(Qt.red)
            
        self.table.setItem(row, 0, url_item)
        self.table.setItem(row, 1, status_item)

    @Slot(str)
    def handle_critical_error(self, error_msg):
        QMessageBox.critical(self, "執行異常", f"背景線程發生錯誤：\n\n{error_msg}")

    @Slot()
    def on_worker_finished(self):
        if self.is_loop_active:
            self.info_label.setText(f"模式：自動循環中... [等待下一次 {self.time_spinner.value()} 小時週期]")
        else:
            self.btn_run.setEnabled(True)
            self.info_label.setText("模式：手動模式 (未啟動自動循環)")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())