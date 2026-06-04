# VERSION: 1.3.6
# LAST UPDATED: 2026-06-04

import streamlit as st

def show():
    st.markdown("### 🎓 技術教學紀錄")
    st.markdown("<h2 style='color: #00FF41;'>🐍 零基礎、沒改過半行Code！我如何用純白話驅動AI 在20分鐘內打造「防崩潰計算機」？</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888;'>紀錄日期：2026-06-04 | 歷時時間：20 分鐘黃金除錯記 | 開發模式：零程式基礎、純白話驅動</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("### 💡 寫在前面：不會寫程式，也能當軟體設計師？")
    st.write("在過去，如果你想寫出一個有視窗介面、能按鍵盤、還具備科學運算功能的計算機，你可能要先啃完好幾本程式教科書。")
    st.write("但是，時代變了。")
    st.write("這台進階計算機的誕生，作者本人完全沒有任何程式基礎，在開發過程中更沒有動手修改過任何一行程式碼。所有的功能擴充、Bug修正、防呆提示，完全是靠「純白話的討論與描述」來驅動AI自動產出程式碼。整個過程從一無所有到「官方穩定版（v1.3.3）」，僅僅耗時20分鐘。本文將帶情完整直擊這場「AI協作」的黃金開發歷程！")
    
    # ------------------ 圖片讀取區 (路徑已導向 images/) ------------------
    st.write("### 📊 AI 協作開發流程與邏輯架構")
    try:
        # 已將路徑更改為 images/ai_flow.jpg
        st.image("images/ai_flow.jpg", caption="白話驅動 AI 與邊界狀況防禦邏輯演進圖", use_container_width=True)
    except:
        st.error("⚠️ 讀取 images/ai_flow.jpg 失敗，請確認圖片是否已放入 images 資料夾中。")
    st.markdown("---")
    # ------------------------------------------------------------------

    st.write("### ⏱️ 核心開發時間線：白話溝通與AI的精準火花")
    
    st.markdown("#### 🛠️【第 1 ~ 5 分鐘】誕生與鍵盤衝突 (v1.1.0)")
    st.write("一開始，我們用白話請AI用 Python內建的Tkinter快速畫出了計算機的按鈕介面，並加上了鍵盤輸入功能。")
    st.markdown("""
    * **遇到的第一個大坑**：按鍵盤輸入 `1` 竟然變成 `11`？
    * **白話回報 AI**：「鍵盤輸入無效，而且算幾次之後輸入 1 變成 11。」
    * **AI 自動修正**：AI 發現 Tkinter 輸入框預設就會接收鍵盤，而程式碼又多插入了一次，導致重複。AI 立刻放手讓系統元件自己管理數字，改為專注監聽 Enter（執行計算）等功能鍵。
    """, unsafe_allow_html=True)
    
    st.markdown("#### 💥【第 5 ~ 15 分鐘】功能擴充與邊界測試：連續的語法死結 (v1.3.1 ~ v1.3.2)")
    st.write("解決了鍵盤衝突後，我們用白話要求加入更進階的「開根號（√）」與「平方」功能。這時，我們像專業的軟體測試人員（QA）一樣，點出了兩個致命的語法崩潰點：")
    
    st.markdown("""
    * **💣 踩坑紀錄 A**：`invalid decimal literal` 閃退錯誤
        * *使用者操作*：輸入 `9√(` 並按下 `=`。
        * *白話回報 AI*：直接截圖回報程式出現 `invalid decimal literal`。
        * *AI 自動修正**：AI 發現 Python 內部的 `eval()` 函數把算式轉換成 `9math.sqrt(`，但程式語言中數字與函式之間缺少乘號（*）。AI 引入了「正規表達式（Regex）」，讓程式自動偵測，只要數字後面黏著根號，就自動在中間補上 `*`。
    * **💣 踩坑紀錄 B**：`was never closed` 語法錯誤
        * *使用者操作*：修正了乘號，但再次輸入 `9√(` 點 `=` 依然跳出錯誤。
        * *白話回報 AI*：截圖回報 `was never closed` 錯誤訊息。
        * *AI 自動修正*：按下根號按鈕時會自動帶出左括號 `√(`，但如果使用者沒有手動輸入右括號 `)` 就直接按等於，語法不完整就會導致系統拋出錯誤。AI 馬上寫了一個「括號計數器」，在按下等於的瞬間，在算式末端自動補齊右括號。
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🚀【第 15 ~ 20 分鐘】邏輯先後順序的黃金交織點 (v1.3.3最終穩定版)")
    st.write("原本以為萬無一失了，結果我們故意測試了一個極端狀況：輸入 `9√(`（括號內不放數字）直接按等於，程式又噴出了一串英文系統報錯。")
    st.markdown("""
    * **白話回報 AI**：截圖反映 `math.sqrt() takes exactly one argument (0 given)`。
    * **AI 發現關鍵**：這就像工廠品管，檢查順序錯了！之前的程式邏輯是「先檢查是不是空根號 ➔ 再補齊括號」。當字串是 `9*math.sqrt(` 時，它成功繞過了空根號檢查，隨後被自動補上括號變成空的 `9*math.sqrt()`，丟給 Python 計算就直接爆炸。
    """, unsafe_allow_html=True)
    
    st.markdown("🏆 **最終正確的邏輯順序**：")
    st.write("AI在第 20分鐘時調整了架構：「先補齊括號 ➔ 再檢查是否為空根號」。當字串先被補齊成 `9*math.sqrt()` 後，立刻被攔截，並跳出溫暖的繁體中文提示：「請在根號中輸入數字再進行計算！」，接著中斷執行，保護程式永遠不崩潰。")
    
    st.write("### 🎯 實戰心得：AI時代的「產品經理」思維")
    st.write("這個歷程展現了AI時代最核心的競爭力：你不需要懂得程式碼的語法，但你必須具備「邏輯思維」與「觀察邊界狀況（Edge Cases）」的能力。")
    
    st.write("---")
    st.markdown("### 💻 附錄：防崩潰計算機 完整原始碼 (v1.3.3)")
    
    calc_code = """# ====================================================================
# 版號: v1.3.3 [官方第一個穩定發行版]
# ====================================================================
import tkinter as tk
from tkinter import messagebox
import math
import re

def on_click(button_text):
    try:
        current_text = entry.get()
        if button_text == "=":
            expression = current_text.replace("√", "math.sqrt")
            expression = re.sub(r'(\d)math\.sqrt', r'\\1*math.sqrt', expression)
            left_count = expression.count('(')
            right_count = expression.count(')')
            if left_count > right_count:
                expression += ')' * (left_count - right_count)
            if "math.sqrt()" in expression:
                messagebox.showerror("提示", "請在根號中輸入數字再進行計算！")
                return
            result = eval(expression)
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
        elif button_text == "√":
            entry.insert(tk.END, "√(")
        else:
            entry.insert(tk.END, button_text)
    except Exception as e:
        messagebox.showerror("錯誤", f"運算失敗: {e}")
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("簡易進階計算機v1.3.3穩定版")
entry = tk.Entry(root, width=20, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+', '√', 'C', '←', '平方']
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, width=8, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val, padx=2, pady=2)
    col_val += 1
    if col_val > 3: col_val = 0; row_val += 1
root.mainloop()"""
    
    st.code(calc_code, language="python")
    
    # ------------------ 新增圖片讀取區 (改用 GitHub 絕對路徑確保載入) ------------------
    st.markdown("---")
    st.write("### 📸 實機測試與防崩潰提示畫面")
    
    col1, col2 = st.columns(2)
    with col1:
        try:
            # 使用絕對網址，繞過 Streamlit Cloud 雲端相對路徑失效的問題
            st.image("https://raw.githubusercontent.com/luciffar-hash/index/main/images/v133_error.jpg", caption="未處理空根號前的系統報錯 (v1.3.2 舊版畫面)", use_container_width=True)
        except:
            st.error("⚠️ 讀取 images/v133_error.jpg 失敗，請確認檔案是否存在。")
            
    with col2:
        try:
            # 使用絕對網址，繞過 Streamlit Cloud 雲端相對路徑失效的問題
            st.image("https://raw.githubusercontent.com/luciffar-hash/index/main/images/v133_success.jpg", caption="調整邏輯順序後的中文防呆提示 (v1.3.3 穩定版畫面)", use_container_width=True)
        except:
            st.error("⚠️ 讀取 images/v133_success.jpg 失敗，請確認檔案是否存在。")
    # ------------------------------------------------------------------
    
    if st.button("⬅ 返回教學區首頁"):
        st.query_params["page"] = "tutorial"
        st.rerun()
