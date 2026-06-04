# VERSION: 1.4.3
# LAST UPDATED: 2026-06-05

import streamlit as st

def show():
    st.markdown("### 🎓 技術教學紀錄")
    st.markdown("<h2 style='color: #00FF41;'>⚡ 挑戰 60 秒極速 Debug：不懂程式碼沒關係，如何讓你的 Code 在沙箱中重生？</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888;'>紀錄日期：2026-06-05 | 歷時時間：60 秒極速通關 | 開發模式：錯誤訊息驅動、零基礎除錯</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("### 💡 寫在前面：線上學 Python，卻被系統無情拒絕？")
    st.write("在線上學習 Python 或測試功能時，你一定遇過這種情況：程式碼明明看著沒問題，點擊執行後系統卻突然噴出一整行紅色英文報錯。")
    st.write("這篇教學的核心就是展示：**即使你完全不懂程式碼，如何利用純白話對話與錯誤訊息，在 60 秒內指揮 AI 精準定位問題、重打一份完美代碼！**")
    
    st.write("### 🚨 案發現場：肉眼難以察覺的語法地雷")
    st.info("🔗 **實戰測試環境**：本案例發生於 [路西法智庫創世神手：Python 線上編譯器](https://luciffar-py.streamlit.app/)。")
    
    # 【教材保留】這裡故意放「會導致編譯器報錯」的程式碼，不進行變動
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
    
    # 顯示終端機看到的真實紅色錯誤訊息
    st.markdown("""
    <div style='background-color: #2b1d1d; border-left: 5px solid #FF4444; padding: 15px; margin-bottom: 25px;'>
        <span style='color: #FF4444; font-weight: bold;'>❌ 執行出錯 (Terminal 輸出)：</span><br>
        <code style='color: #FFF; font-family: monospace;'>unterminated string literal (detected at line 5)</code>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("### 🧠 AI 極速解析：凶手就是那條字串！")
    st.markdown("""
    * **🔍 錯誤解讀**：`unterminated string literal` 代表**「未結束的字串」**。Python 看到單個雙引號開頭卻找不到結尾，因為它被隔到下一行去了。
    * **💡 協作心法**：直接把這一整段錯誤丟給 AI，它會在 2 秒內看出你的引號換行錯了，並主動補好它。
    """, unsafe_allow_html=True)
    
    st.write("### ✅ AI 產出的「完美通關版」（語法安全修正）")
    
    # 【已修正】這裡將原本會導致編譯錯誤的換行字串，修正為安全的單行與 \n 格式，並更新版號
    good_code = """# ==========================================================
# 實戰：購物車結帳系統 (v2.4.7 語法安全修正版)
# ==========================================================
simulated_cart_totals = [350, 1200, 800, 2500, 150]

# ✅ 修正方案：改用 \\n 處理換行，確保字串在同一行完美閉合
print("====== 購物車結帳系統執行中 ======\\n")

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
    st.code(good_code, language="python")
    st.success("🎉 恭喜您解鎖成就：60秒內讓程式碼完美重生！")
    
    st.markdown("---")
    if st.button("⬅ 返回教學區首頁", key="back_to_menu_p3"):
        st.query_params["page"] = "tutorial"
        st.rerun()
