# SYSTEM VERSION: 1.0.4
# LAST UPDATED: 2026-06-04

import streamlit as st

# ================= 動態掛載外部獨立模組 =================
try:
    import history.main as history_mod
except ImportError:
    history_mod = None

try:
    import tutorials.post1 as post1
except ImportError:
    post1 = None

# --- 1. 頁面配置 ---
st.set_page_config(
    page_title="Luciffar AI: Dawnstar Command", 
    layout="centered",
    page_icon="⭐"
)

# --- 2. 戰情室 全域 CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0A0A0A; color: #FFFFFF; }
    h1, h2, h3 { color: #FFD700; }
    
    /* 頂部常駐導航條 */
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
    
    .header-tag { background-color: #1a1a1a; padding: 20px; border-left: 6px solid #00FF41; margin-bottom: 30px; width: 100%; }
    .chinese-title { color: #00FF41; font-weight: bold; font-size: 1.8em; display: inline-block; vertical-align: middle; margin-right: 15px; }
    .english-title { color: #00FFFF; font-size: 1.8em; font-family: monospace; display: inline-block; vertical-align: middle; }
    .demo-tag { color: #FF4444; font-size: 1.2em; font-weight: bold; margin-top: 15px; display: block; }
    .version-tag { color: #888; font-size: 1em; margin-top: 5px; display: block; }
    
    /* 模組卡片通用樣式 */
    .history-card, .tutorial-card { 
        background-color: #1a1a1a; padding: 20px; border-radius: 0px; 
        border-left: 5px solid #FFD700; margin-bottom: 20px;
    }
    
    .stButton>button { width: 100%; border: 1px solid #FFD700; color: #FFD700; background: transparent; border-radius: 0px; margin-top: 10px; }
    .stButton>button:hover { background: #FFD700; color: #0A0A0A; }
    </style>
""", unsafe_allow_html=True)

# --- 3. 頂部導航欄 (主邏輯：往右擴充新功能只需在此加 A 標籤) ---
st.markdown("""
    <div class='nav-bar'>
        <a href='?page=main' class='nav-link'>🛸 戰略總部</a>
        <a href='?page=history' class='nav-link'>📜 本站創建歷史</a>
        <a href='?page=tutorial' class='nav-link'>🎓 教學區</a>
    </div>
""", unsafe_allow_html=True)

current_page = st.query_params.get("page", "main")

# ================= 分支：教學區主頁 =================
if current_page == "tutorial":
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🎓 智庫技術教學區</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00FF41; text-align: center; font-size: 1.2em;'>人類負責邏輯與體驗，AI負責技術與產出</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("""
        <div class='tutorial-card'>
            <span style='color: #FFD700; font-weight: bold; font-size: 1.3em;'>🐍 零基礎、沒改過半行Code！我如何用純白話驅動AI 在20分鐘內打造「防崩潰計算機」？</span><br>
            <span style='color: #888; font-size: 0.9em;'>發布日期：2026-06-04 | 分類：AI 協作實戰</span>
            <p style='margin-top: 10px; margin-bottom: 15px; line-height: 1.6; color: #CCCCCC;'>
                不會寫程式，也能當軟體設計師？本文將帶你完整直擊這場「AI協作」的黃金開發歷程！看作者如何用純白話討論...
            </p>
            <a href='?page=tutorial_001' style='color: #00FFFF; text-decoration: none; font-weight: bold;'>[ 點擊閱讀全文 & 複製原始碼 ]</a>
        </div>
    """, unsafe_allow_html=True)

# ================= 分支：教學文章內頁分流 =================
elif current_page == "tutorial_001":
    if post1 is not None:
        post1.show()
    else:
        st.error("找不到教學文章檔案，請確認 tutorials/post1.py 是否存在。")

# ================= 分支：歷史 (已移出至外部檔案) =================
elif current_page == "history":
    if history_mod is not None:
        history_mod.show()
    else:
        st.error("找不到歷史紀錄檔案，請確認 history/main.py 是否存在。")

# ================= 分支：主戰情室 (核心控制面板) =================
else:
    try:
        st.image("logo.png", width=250)
    except:
        pass

    st.markdown("""
        <div class='header-tag'>
            <span class='chinese-title'>路西法智庫:AI破曉晨星戰略指揮總部</span>
            <span class='english-title'>Luciffar AI: Dawnstar Command</span>
            <span class='demo-tag'>0基礎驅動AI寫程式架站 :功能示範展示</span>
            <span class='version-tag'>SYSTEM VERSION: 1.0.4</span>
        </div>
    """, unsafe_allow_html=True)

    st.write("#### 🛡️ 戰略指揮模組 (Active Command Deck)")
    tools = [
        {"name": "決策之眼", "desc": "新聞搜尋", "eng": "Decision Eye", "url": "https://luciffar-thinktank.streamlit.app/"},
        {"name": "極光裁決", "desc": "YT 縮網址", "eng": "YT Linker", "url": "https://luciffar-yturl.streamlit.app/"},
        {"name": "創世神手", "desc": "Python 線上編輯器", "eng": "Python Compiler", "url": "https://luciffar-py.streamlit.app/"},
        {"name": "命運重塑", "desc": "樹精靈轉檔", "eng": "CSV Converter", "url": "https://luciffar-ods.streamlit.app/"}
    ]

    cols = st.columns(2)
    for i, tool in enumerate(tools):
        with cols[i % 2]:
            st.write(f"### {tool['name']}")
            st.write(f"*{tool['desc']}*")
            st.caption(tool['eng'])
            st.link_button(f"EXECUTE", tool['url'], use_container_width=True)
            st.write("") 

st.markdown("---")
st.caption("Dawnstar Command | Operational | All Systems Online")
