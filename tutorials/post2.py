# VERSION: 1.3.7
# LAST UPDATED: 2026-06-04

import streamlit as st

def show():
    st.markdown("### 🎓 技術教學紀錄")
    st.markdown("<h2 style='color: #00FF41;'>🐍 零基礎、沒改過半行Code！我如何用純白話驅動AI 在20分鐘內打造「防崩潰計算機」？</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888;'>紀錄日期：2026-06-04 | 歷時時間：20 分鐘黃金除錯記 | 開發模式：零程式基礎、純白話驅動</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("### 💡 寫在前面：不會寫程式，也能當軟體設計師？")
    st.write("在過去，如果你想寫出一個有視窗介面、能按鍵盤、還具備科學運算功能的計算機，你可能要先啃完好幾本程式教科書。但是，時代變了。")
    st.write("這台進階計算機的誕生，作者本人完全沒有任何程式基礎，在開發過程中更沒有動手修改過任何一行程式碼。所有的功能擴充、Bug修正、防呆提示，完全是靠「純白話的討論與描述」來驅動AI自動產出程式碼。整個過程從一無所有到「官方穩定版（v1.3.3）」，僅僅耗時20分鐘。本文將帶你完整直擊這場「AI協作」的黃金開發歷程！")
    
    st.write("### 📊 AI 協作開發流程與邏輯架構")
    try:
        st.image("images/ai_flow.jpg", caption="白話驅動 AI 與邊界狀況防禦邏輯演進圖", use_container_width=True)
    except:
        st.error("⚠️ 讀取 images/ai_flow.jpg 失敗，請確認圖片是否已放入 images 資料夾中。")
    st.markdown("---")

    st.write("### ⏱️ 核心開發時間線：白話溝通與AI的精準火花")
    st.markdown("""
    * **🛠️【第 1 ~ 5 分鐘】誕生與鍵盤衝突 (v1.1.0)**：解決輸入 1 變成 11 的重複監聽 Bug。
    * **💥【第 5 ~ 15 分鐘】功能擴充與邊界測試 (v1.3.1 ~ v1.3.2)**：修正 `invalid decimal literal` 與未閉合括號錯誤。
    * **🚀【第 15 ~ 20 分鐘】邏輯先後順序的黃金交織點 (v1.3.3 穩定版)**：調整為「先補齊括號 ➔ 再檢查是否為空根號」，完美攔截崩潰。
    """, unsafe_allow_html=True)
    
    st.write("### 💻 附錄：防崩潰計算機 完整原始碼 (v1.3.3)")
    
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
    
    st.markdown("---")
    st.write("### 📸 實機測試與防崩潰提示畫面")
    st.image("https://i.urusai.cc/GvyjJ.jpg", caption="未處理空根號前的系統報錯 (v1.3.0 舊版畫面)", use_container_width=True)
    st.image("https://i.urusai.cc/SGUZN.jpg", caption="調整邏輯順序後的中文防呆提示 (v1.3.3 穩定版畫面)", use_container_width=True)
    
    # 返回對齊到 post1
    st.markdown("---")
    if st.button("⬅ 返回教學區首頁", key="back_to_menu_p2"):
        st.query_params["page"] = "tutorial"
        st.rerun()
