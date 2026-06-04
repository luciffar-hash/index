# VERSION: 1.4.0
# LAST UPDATED: 2026-06-04

import streamlit as st

def show():
    st.markdown("### 🎓 技術教學紀錄")
    st.markdown("<h2 style='color: #00FF41;'>⚡ 挑戰 60 秒極速 Debug：不懂程式碼沒關係，如何讓你的 Code 在沙箱中重生？</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888;'>紀錄日期：2026-06-04 | 歷時時間：60 秒極速通關 | 開發模式：錯誤訊息驅動、零基礎除錯</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("### 💡 寫在前面：線上學 Python，卻被系統無情拒絕？")
    st.write("在線上學習 Python 或測試功能時，你一定遇過這種情況：程式碼明明看著沒問題，點擊執行後系統卻突然噴出一整行讓人摸不著頭緒的紅色英文報錯。")
    st.write("這篇教學的核心就是展示：**即使你完全不懂程式碼，如何利用純白話對話與錯誤訊息，在 60 秒內指揮 AI 精準定位問題、重打一份完美代碼！**")
    
    st.write("### 🚨 案發現場：肉眼難以察覺的語法地雷")
    st.info("🔗 **實戰測試環境**：本案例發生於 [路西法智庫創世神手：Python 線上編譯器](https://luciffar-py.streamlit.app/)。")
    
    # 這裡完美還原你在線上編輯器導致 unterminated string literal 的程式碼
    bad_code = """# 原始報錯程式碼（引號換行未閉合錯誤）
simulated_cart_totals = [350, 1200, 800, 2500, 150]

# 👇 致命崩潰點：使用單個雙引號時直接按 Enter 鍵換行了！
print("====== 購物車結帳系統執行中 ======
")

# 2. 核心邏輯：滿 1000 元享 9 折
for order_number, amount in enumerate(simulated_cart_totals, 1):
    print(f"正在處理第 {order_number} 筆訂單... 原始金額: {amount}")
    
    if amount >= 1000:
        discounted_amount = int(amount * 0.9)
        print(f"🎉 恭喜！觸發優惠！折扣後金額: {discounted_amount}")
    else:
        gap = 1000 - amount
        print(f"提示：還差 {gap} 即可享優惠。")
    print("-" * 45)
"""
    st.code(bad_code, language="python")
    
    # 顯示你在終端機看到的真實紅色錯誤訊息
    st.markdown("""
    <div style='background-color: #2b1d1d; border-left: 5px solid #FF4444; padding: 15px; margin-bottom: 25px;'>
        <span style='color: #FF4444; font-weight: bold;'>❌ 執行出錯 (Terminal 輸出)：</span><br>
        <code style='color: #FFF; font-family: monospace;'>unterminated string literal (detected at line 6) (, line 6)</code>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("### 🧠 AI 極速解析：凶手就是那條字串！")
    
    st.markdown("""
    * **🔍 錯誤解讀**：`unterminated string literal` 翻譯成白話文就是**「未結束的字串字面量」**。Python 在執行到第 6 行時，看到雙引號開頭卻找不到對應的雙引號結尾，因為它被你按 Enter 隔到第 7 行去了！
    * **💡 協作心法**：遇到這種狀況，完全不用慌張去改邏輯。直接把這一整段錯誤丟給 AI
