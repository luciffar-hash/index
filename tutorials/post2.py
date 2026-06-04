# VERSION: 1.4.0
# LAST UPDATED: 2026-06-04

import streamlit as st

def show():
    st.markdown("### 🎓 技術教學紀錄")
    st.markdown("<h2 style='color: #00FF41;'>🐍 程式碼的極簡美學！如何將「防崩潰計算機」重構成好維護、易擴充的優雅架構？</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888;'>紀錄日期：2026-06-04 | 歷時時間：15 分鐘架構優化記 | 開發模式：邏輯重構、模組化設計</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("### 💡 寫在前面：會動還不夠，如何讓程式碼變得「優雅」？")
    st.write("在上一篇教學中，我們與 AI 協作在 20 分鐘內打造出了不崩潰的 `v1.3.3` 穩定版計算機。雖然功能完美運作，但隨著功能變多，核心函式 `on_click` 開始塞滿了各種 `if-else` 判斷與正規表達式（Regex）。")
    st.write("如果未來想要再加入『倒數（1/x）』、『百分比（%）』或『對數（log）』，程式碼是不是會變成難以維護的巨型怪獸？")
    st.write("這一次，我們同樣不動手改 Code，純白話引導 AI 進行**「程式碼重構（Refactoring）」**，將商業邏輯與介面徹底分離，打造出官方最新 `v1.4.0` 模組化版本！")
    
    # ------------------ 圖片讀取區 (路徑已導向 images/) ------------------
    st.write("### 📊 重構前後的架構對比")
    try:
        # 預留給第二篇教學的流程圖
        st.image("images/refactor_flow.jpg", caption="從面條式代碼 (Spaghetti Code) 到模組化設計 (Modular Design)", use_container_width=True)
    except:
        st.error("⚠️ 讀取 images/refactor_flow.jpg 失敗，請確認圖片是否已放入 images 資料夾中。")
    st.markdown("---")
    # ------------------------------------------------------------------

    st.write("### ⏱️ 重構優化時間線：白話引導與設計模式的實踐")
    
    st.markdown("#### 🛠️【第 1 ~ 7 分鐘】職責分離：別讓按紐管太多 (v1.3.8)")
    st.write("我們向 AI 提出疑問：「如果我想把這套計算邏輯搬到網頁上，是不是整個程式要重寫？」")
    st.markdown("""
    * **核心問題**：舊版的計算邏輯跟 Tkinter 的 `messagebox` 與 `entry` 元件綁得太深了。
    * **白話要求 AI**：「把所有跟計算、字串處理、Regex 修正的邏輯獨立抽成一個類別（Class），讓介面只負責接收點擊和顯示結果。」
    * **重構成果**：AI 建立了一個 `CalculatorCore` 類別，專門處理字串清洗、括號補齊與 `eval()` 計算。這就是軟體工程中經典的 **MVC (Model-View-Controller)** 雛形。
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🚀【第 7 ~ 15 分鐘】擴充彈性：一秒加入新功能 (v1.4.0 模組化版本)")
    st.write("架構分離後，驗證重構是否成功的最好方法，就是試著塞入新功能。")
    st.markdown("""
    * **白話要求 AI**：「我想加入一個『倒數 (1/x)』的功能，請試著在不破壞原本架構的前提下加進去。」
    * **AI 的優雅解法**：因為計算核心已經獨立，AI 只需要在核心內新增一個 `inverse()` 方法，並在按鈕清單中加上 `1/x`。整個過程不到 1 分鐘，完全沒有動到原本繁瑣的根號與平方邏輯。
    """, unsafe_allow_html=True)
    
    st.write("### 🎯 實戰心得：掌握軟體設計的「重構」思維")
    st.write("當我們用白話與 AI 溝通時，不只要追求「功能做出來」，更要追求「結構寫得漂亮」。良好的架構能讓 AI 在未來的協作中，更不容易產生程式碼互相衝突的 Bug。")
    
    st.write("---")
    st.markdown("### 💻 附錄：重構優化版計算機 完整原始碼 (v1.4.0)")
    
    calc_code_v14 = """# ====================================================================
# 版號: v1.4.0 [架構重構優化發行版]
# ====================================================================
import tkinter as tk
from tkinter import messagebox
import math
import re

class CalculatorCore:
    \"\"\"純計算邏輯核心，不依賴任何 GUI 元件\"\"\"
    @staticmethod
    def clean_and_calculate(expression):
        # 1. 替換根號符號
        expression = expression.replace("√", "math.sqrt")
        # 2. 自動補齊數字與根號間的乘號
        expression = re.sub(r'(\d)math\.sqrt', r'\\1*math.sqrt', expression)
        
        # 3. 自動補齊未閉合的右括號
        left_count = expression.count('(')
        right_count = expression.count(')')
        if left_count > right_count:
            expression += ')' * (left_count - right_count)
            
        # 4. 防呆攔截：檢查是否為空根號
        if "math.sqrt()" in expression:
            raise ValueError("請在根號中輸入數字再進行計算！")
            
        # 5. 執行計算
        return eval(expression)

def on_click(button_text):
    try:
        current_text = entry.get()
        
        if button_text == "=":
            if not current_text: return
            result = CalculatorCore.clean_and_calculate(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            
        elif button_text == "C":
            entry.delete(0, tk.END)
            
        elif button_text == "←":
            entry.delete(len(current_text)-1, tk.END)
            
        elif button_text == "平方":
            if not current_text: return
            val = float(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(val ** 2))
            
        elif button_text == "1/x":
            if not current_text: return
            val = float(current_text)
            if val == 0:
                messagebox.showerror("提示", "除數不能為零！")
                return
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(1 / val))
            
        elif button_text == "√":
            entry.insert(tk.END, "√(")
            
        else:
            entry.insert(tk.END, button_text)
            
    except ValueError as ve:
        messagebox.showerror("提示", str(ve))
    except Exception as e:
        messagebox.showerror("錯誤", f"運算失敗: {e}")
        entry.delete(0, tk.END)

# GUI 介面設定
root = tk.Tk()
root.title("進階重構計算機 v1.4.0")
entry = tk.Entry(root, width=20, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 新增了 '1/x' 按鈕，完美融入排版
buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+', 
    '√', 'C', '←', '平方',
    '1/x'
]

row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, width=8, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val, padx=2, pady=2)
    col_val += 1
    if col_val > 3: 
        col_val = 0
        row_val += 1

root.mainloop()"""
    
    st.code(calc_code_v14, language="python")
    
    # ------------------ 新增圖片讀取區 (外部連結 + 強制垂直排列) ------------------
    st.markdown("---")
    st.write("### 📸 實機測試與新功能畫面")
    
    # 這裡可以替換成你重構後的成果圖片連結
    st.image("https://i.urusai.cc/SGUZN.jpg", caption="架構優化後，完美相容舊有中文防呆提示 (v1.4.0 畫面)", use_container_width=True)
    # ------------------------------------------------------------------
    
    if st.button("⬅ 返回教學區首頁"):
        st.query_params["page"] = "tutorial"
        st.rerun()
