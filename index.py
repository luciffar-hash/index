# SYSTEM VERSION: 1.0.5
# LAST UPDATED: 2026-06-04

import streamlit as st

# --- 1. 頁面配置 ---
st.set_page_config(
    page_title="Luciffar AI: Dawnstar Command", 
    layout="centered",
    page_icon="⭐"
)

# --- 2. 戰情室 CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0A0A0A; color: #FFFFFF; }
    h1, h2, h3 { color: #FFD700; }
    
    .nav-bar { 
        background-color: #1a1a1a; padding: 10px; margin-bottom: 20px;
        border-bottom: 2px solid #FFD700; text-align: left;
    }
    .nav-link { 
        color: #FFD700 !important; font-weight: bold; font-size: 1.1em;
        text-decoration: none; padding: 5px 10px; border: 1px solid #FFD700;
        background-color: #0A0A0A; margin-right: 10px; display: inline-block;
    }
    .nav-link:hover { background-color: #FFD700; color: #0A0A0A !important; }
    
    .header-tag { background-color: #1a1a1a; padding: 20px; border-left: 6px solid #00FF41; margin-bottom: 30px; }
    .chinese-title { color: #00FF41; font-weight: bold; font-size: 1.8em; display: inline-block; vertical-align: middle; margin-right: 15px; }
    .english-title { color: #00FFFF; font-size: 1.8em; font-family: monospace; display: inline-block; vertical-align: middle; }
    .demo-tag { color: #FF4444; font-size: 1.2em; font-weight: bold; margin-top: 15px; display: block; }
    .version-tag { color: #888; font-size: 1em; margin-top: 5px; display: block; }
    
    .tutorial-card { background-color: #1a1a1a; padding: 20px; border-left: 5px solid #FFD700; margin-bottom: 20px; }
    .history-card { background-color: #1a1a1a; padding: 20px; border-left: 5px solid #FFD700; margin-bottom: 20px; }
    
    .stButton>button { width: 100%; border: 1px solid #FFD700; color: #FFD700; background: transparent; border-radius: 0px; margin-top: 10px; }
    .stButton>button:hover { background: #FFD700; color: #0A0A0A; }
    </style>
""", unsafe_allow_html=True)

# --- 3. 頂部導航欄 ---
st.markdown("""
    <div class='nav-bar'>
        <a href='?page=main' class='nav-link'>🛸 戰略總部</a>
        <a href='?page=history' class='nav-link'>📜 本站創建歷史</a>
        <a href='?page=tutorial' class='nav-link'>🎓 教學區</a>
    </div>
""", unsafe_allow_html=True)

current_page = st.query_params.get("page", "main")

# ================= 頁面分支：教學區 =================
if current_page == "tutorial":
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🎓 教學區</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class="tutorial-card">
            <h2 style="color: #FFD700;">🐍 零基礎、沒改過半行Code！我如何用純白話驅動AI 在20分鐘內打造「防崩潰計算機」？</h2>
            <div style="color: #888; font-size: 0.9em; margin-bottom: 15px;">發布日期：2026-06-04</div>
            <p style="color: #FFFFFF; line-height: 1.6;">
                這是一個關於零程式基礎者，如何透過邏輯思維與 AI 協作，從無到有開發出穩定運算工具的完整開發歷程。
            </p>
            <a href='?page=tutorial_detail' style="color: #00FF41; font-weight: bold; text-decoration: none;">[ 點擊閱讀全文 ]</a>
        </div>
    """, unsafe_allow_html=True)

elif current_page == "tutorial_detail":
    st.markdown("<h1 style='color: #FFD700;'>🐍 零基礎、沒改過半行Code！</h1>", unsafe_allow_html=True)
    st.write("### 核心心法：人類負責邏輯，AI 負責產出")
    st.write("在過去，想寫出具備科學運算功能的計算機通常需要深厚的程式底子 [cite: 1]。但這次開發的「v1.3.3 穩定版計算機」，完全靠與 AI 的「純白話討論」完成，過程中未手動修改任何一行程式碼 [cite: 3]。")
    st.write("### 開發歷程精華")
    st.write("- **語法崩潰防護**：針對 `9√( =` 的錯誤，引入正規表達式自動補上乘號，解決銜接問題 [cite: 12]。")
    st.write("- **極端狀況測試 (Edge Cases)**：故意輸入空根號 `9√()` 逼出系統漏洞，並調整邏輯為「先補括號 ➔ 再檢查空值」，達成零崩潰 [cite: 18, 19]。")
    st.write("- **AI 協作技巧**：扮演產品經理，描述預期效果而非底層語法 [cite: 24]。")
    if st.button("⬅ 返回教學區"):
        st.query_params["page"] = "tutorial"
        st.rerun()

# ================= 頁面分支：歷史 =================
elif current_page == "history":
    st.markdown("<h1 style='text-align: center;'>本站創建歷史</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00FF41; text-align: center; font-size: 1.5em; font-weight: bold;'>0基礎驅動AI寫程式架站</p>", unsafe_allow_html=True)
    # ... (歷史資料內容同前版本)

# ================= 頁面分支：主戰情室 =================
else:
    st.markdown("""
        <div class='header-tag'>
            <span class='chinese-title'>路西法智庫:AI破曉晨星戰略指揮總部</span>
            <span class='english-title'>Luciffar AI: Dawnstar Command</span>
            <span class='demo-tag'>0基礎驅動AI寫程式架站 :功能示範展示</span>
            <span class='version-tag'>SYSTEM VERSION: 1.0.5</span>
        </div>
    """, unsafe_allow_html=True)
    st.write("#### 🛡️ 戰略指揮模組 (Active Command Deck)")
    # ... (其餘 UI 組件)

st.markdown("---")
st.caption("Dawnstar Command | Operational | All Systems Online")
