# SYSTEM VERSION: 1.0.4
# LAST UPDATED: 2026-06-04

import streamlit as st

# 引入外部教學文章模組
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

# --- 2. 戰情室 CSS ---
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
    
    .header-tag { 
        background-color: #1a1a1a; padding: 20px; 
        border-left: 6px solid #00FF41; margin-bottom: 30px;
        width: 100%;
    }
    
    /* 標題色彩與並排設定 */
    .chinese-title { 
        color: #00FF41; font-weight: bold; font-size: 1.8em; 
        display: inline-block; vertical-align: middle; margin-right: 15px;
    }
    .english-title { 
        color: #00FFFF; font-size: 1.8em; font-family: monospace; 
        display: inline-block; vertical-align: middle;
    }
    .demo-tag { 
        color: #FF4444; font-size: 1.2em; font-weight: bold; 
        margin-top: 15px; display: block;
    }
    .version-tag { color: #888; font-size: 1em; margin-top: 5px; display: block; }
    
    /* 歷史與教學卡片樣式 */
    .history-card, .tutorial-card { 
        background-color: #1a1a1a; padding: 20px; border-radius: 0px; 
        border-left: 5px solid #FFD700; margin-bottom: 20px;
    }
    
    .stButton>button { 
        width: 100%; border: 1px solid #FFD700; color: #FFD700; 
        background: transparent; border-radius: 0px; margin-top: 10px;
    }
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

# ================= 頁面分支：教學區主頁 =================
if current_page == "tutorial":
    st.markdown("<h1 style='text-align: center; color: #FFD700;'>🎓 智庫技術教學區</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00FF41; text-align: center; font-size: 1.2em;'>人類負責邏輯與體驗，AI負責技術與產出</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 第一篇教學卡片
    st.markdown("""
        <div class='tutorial-card'>
            <span style='color: #FFD700; font-weight: bold; font-size: 1.3em;'>🐍 零基礎、沒改過半行Code！我如何用純白話驅動AI 在20分鐘內打造「防崩潰計算機」？</span><br>
            <span style='color: #888; font-size: 0.9em;'>發布日期：2026-06-04 | 分類：AI 協作實戰</span>
            <p style='margin-top: 10px; margin-bottom: 15px; line-height: 1.6; color: #CCCCCC;'>
                不會寫程式，也能當軟體設計師？本文將帶你完整直擊這場「AI協作」的黃金開發歷程！看作者如何用純白話討論，在20分鐘內打造出官方穩定版（v1.3.3）防崩潰計算機...
            </p>
            <a href='?page=tutorial_001' style='color: #00FFFF; text-decoration: none; font-weight: bold;'>[ 點擊閱讀全文 & 複製原始碼 ]</a>
        </div>
    """, unsafe_allow_html=True)

# ================= 頁面分支：教學區 - 連結到獨立檔案 =================
elif current_page == "tutorial_001":
    if post1 is not None:
        post1.show()
    else:
        st.error("找不到教學文章檔案，請確認 tutorials/post1.py 是否存在。")

# ================= 頁面分支：歷史 =================
elif current_page == "history":
    st.markdown("<h1 style='text-align: center;'>本站創建歷史</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00FF41; text-align: center; font-size: 1.5em; font-weight: bold;'>0基礎驅動AI寫程式架站</p>", unsafe_allow_html=True)
    st.write("**作者背景**：無程式語言基礎")
    st.markdown("---")
    
    history_data = [
        ("2026/05/29", "起源與覺醒", "測試 AI 能力，問了 PYTHON 難不難學。開始安裝並寫出 HELLO WORLD 與小遊戲。", "https://www.ptt.cc/bbs/Gossiping/M.1780035188.A.18E.html"),
        ("2026/05/30", "決策之眼", "架設爬蟲網站，支援關鍵字搜尋新聞並按時序排列。", "https://www.ptt.cc/bbs/Gossiping/M.1780118601.A.41D.html"),
        ("2026/05/31", "創世神手", "架設 Python 線上編輯器，部署雲端編譯環境。", "https://www.ptt.cc/bbs/Gossiping/M.1780226831.A.D00.html"),
        ("2026/06/01", "極光裁決", "架設 YT 縮網址線上服務。", "https://www.ptt.cc/bbs/Gossiping/M.1780274581.A.B62.html"),
        ("2026/06/02", "戰略總部", "架設主網站，統合旗下所有服務。", "https://luciffar.streamlit.app/"),
        ("2026/06/03", "命運重塑", "架設國泰樹精靈 CSV 轉 ODS，雙刀流模式。", "https://www.ptt.cc/bbs/Stock/M.1780470116.A.663.html")
    ]
    
    for date, title, desc, link in history_data:
        st.markdown(f"""
            <div class='history-card'>
                <span style='color: #FFD700; font-weight: bold; font-size: 1.2em;'>{date} —— {title}</span><br>
                <p style='margin-top: 5px; margin-bottom: 10px; line-height: 1.5;'>{desc}</p>
                <a href='{link}' target='_blank' style='color: #00FF41; text-decoration: none; font-weight: bold;'>[ 查看紀錄 / 服務連結 ]</a>
            </div>
        """, unsafe_allow_html=True)

# ================= 頁面分支：主戰情室 =================
else:
    try:
        st.image("logo.png", width=250)
    except:
        st.write("", unsafe_allow_html=True)

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
        {"name": "創世神手", "desc": "Python 線上編譯器", "eng": "Python Compiler", "url": "https://luciffar-py.streamlit.app/"},
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
