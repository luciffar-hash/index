# VERSION: 1.3.7
# LAST UPDATED: 2026-06-04

import streamlit as st

def show():
    st.markdown("### 🎓 技術教學紀錄")
    st.markdown("<h2 style='color: #00FF41;'>⚡ 挑戰 60 秒極速 Debug：不懂程式碼沒關係，如何讓你的 Code 在沙箱中重生？</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888;'>紀錄日期：2026-06-04 | 歷時時間：60 秒極速通關 | 開發模式：錯誤截圖驅動、零基礎除錯</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.write("### 💡 寫在前面：在線上學 Python，卻被系統擋下來？")
    st.write("在線上學習 Python 時，你是否遇過這種情況：明明邏輯正確，但系統卻噴出紅色警告並拒絕執行？")
    st.write("這不是你的錯， family！而是線上沙箱環境的「安全審查機制」觸發了誤判。")
    st.write("這篇教學的核心不在於複雜的程式邏輯，而是展示作者如何透過精準的「白話文對話」，在不閱讀任何一行程式碼的情況下，交由 AI 完成急速協作與除錯。只要你把錯誤訊息丟給 AI，它能在兩秒內讀懂錯誤、定位問題並重打正確的程式碼！")
    
    st.write("### 🚨 案發現場：AI 與系統的第一次「摩擦」")
    st.write("我們在嘗試運行購物車系統時，由於在註解中無意間提到了敏感詞，觸發了沙箱的防禦機制：")
    
    # 呼籲使用者去運行的區塊
    st.info("🔗 **實戰測試連結**：請將下方原始程式碼貼入 [Streamlit 運行環境](https://luciffar-py.streamlit.app/) 並測試。")
    
    # 原始程式碼區塊
    bad_code = """# 原始程式碼（執行會觸發安全機制報錯）
# (這裡用固定變數取代了 input()，確保在任何網頁環境都能 100% 運行成功)
simulated_cart_totals = [350, 1200, 800, 2500, 150]
print("====== 購物車結帳系統 ======\n")

for order_number, amount in enumerate(simulated_cart_totals, 1):
    if amount >= 1000:
        print(f"優惠金額: {int(amount * 0.9)}")
    else:
        print(f"原始金額: {amount}")"""
    
    st.code(bad_code, language="python")
    st.markdown("<p style='color: #FF4B4B; font-weight: bold;'>⚠️ 錯誤判讀：系統直接鎖定並報錯：「檢測到敏感或不支援的程式碼（如 input 等）」。</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("### 🚀 AI 極速協作：兩秒除錯術")
    st.write("這就是本次教學的精髓——「白話文對話」。作者無需具備深厚的程式功功底，只需將錯誤截圖丟給 AI，並用口語說明狀況。")
    
    # ------------------ 圖片讀取區 (路徑已導向 images/) ------------------
    try:
        # 預留給除錯流程或對話截圖
        st.image("images/debug_flow.jpg", caption="白話文回報與 AI 兩秒定位邏輯示意圖", use_container_width=True)
    except:
        st.error("⚠️ 讀取 images/debug_flow.jpg 失敗，請確認圖片是否已放入 images 資料夾中。")
    # ------------------------------------------------------------------

    st.markdown("""
    * **🗣️ 作者指令**：直接告知 AI 系統報錯，並提供錯誤的截圖。
    * **🧠 AI 精準判斷**：兩秒內精準定位關鍵問題 —— 網頁過濾器不分青紅皂白，連註解文字也掃描，誤判了註解裡的 `input` 字串。
    * **🏆 成果產出**：AI 立刻重打一份完全乾淨的程式碼，並在 60 秒內由作者完成測試並通關。
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("### ✅ AI 產出的「完美通關版」（直接複製即可運行）")
    st.write("這份程式碼是由 AI 針對錯誤訊息即時重打，拿掉了註解中的敏感字眼，確保完全符合沙箱安全標準：")
    
    # 完美通關版程式碼區塊
    good_code = """# ==========================================================
# 實戰：購物車結帳系統 (沙箱友善版)
# ==========================================================
# 1. 使用固定串列模擬消費金額
simulated_cart_totals = [350, 1200, 800, 2500, 150]
print("====== 購物車結帳系統執行中 ======\n")

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

print("\n系統提示：所有資料已解析完畢。")"""
    
    st.code(good_code, language="python")
    st.success("🎉 恭喜您解鎖成就：人生第一次 Debug 成功！")
    
    st.markdown("---")
    st.write("### 💡 給學習者的關鍵心法")
    st.markdown("""
    1. **白話溝通勝過專業術語**：當遇到程式問題時，只要能清楚說明「發生什麼錯誤」或提供截圖，AI 就能取代人工去閱讀並理解底層程式碼。
    2. **信任 AI 的除錯速度**：不要自己糾結在幾百行程式碼中尋找錯誤，將錯誤訊息「餵」給 AI，它能在兩秒內為你重寫一份更安全的程式碼。
    3. **保持資料與邏輯分離**：學會使用 AI 提供的「固定變數賦值」技巧，這是對抗網頁沙箱限制的最強武器。
    """, unsafe_allow_html=True)
    
    st.write("這次 60 秒的極速 Debug 證明：不懂程式碼沒關係，只要你會「跟 AI 聊天」，你就是最強的除錯大師！")
    
    # 底部統一的返回主頁按鈕
    st.markdown("---")
    if st.button("⬅ 返回教學區首頁"):
        st.query_params["page"] = "tutorial"
        st.rerun()
