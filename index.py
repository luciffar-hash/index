# SYSTEM VERSION: 1.0.1
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
    }
    .chinese-title { color: #00FF41; font-weight: bold; font-size: 3em; display: block; line-height: 1.2; }
    .english-title { color: #00FF41; font-size: 3em; font-family: monospace; display: block; line-height: 1.2; }
    .version-tag { color: #888; font-size: 1.2em; margin-top: 10px; display: block; }
    
    /* 歷史卡片樣式 */
    .history-card { 
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

# --- 3. 頂部導航欄 (同頁面參數切換) ---
st.markdown("""
    <div class='nav-bar'>
        <a href='?page=main' class='nav-link'>🛸 戰略總部</a>
        <a href='?page=history' class='nav-link'>📜 本站創建歷史</a>
    </div>
""", unsafe_allow_html=True)

# 獲取目前的頁面參數
current_page = st.query_params.get("page", "main")

# ================= 頁面分支：本站創建歷史 =================
if current_page == "history":
    st.markdown("<h1 style='text-align: center;'>本站創建歷史</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00FF41; text-align: center; font-size: 1.5em; font-weight: bold;'>0基礎驅動AI寫程式架站</p>", unsafe_allow_html=True)
    st.write("**作者本身背景**：無程式語言基礎背景")
    st.markdown("---")
    
    history_data = [
        ("2026/05/29", "起源與覺醒", "一時興起想測試 AI 到底有多神，問了 AI 大名鼎鼎 PYTHON 難不難學。AI 說並不難就開始安裝程式，寫出 HELLO WORLD 與小遊戲。", "https://www.ptt.cc/bbs/Gossiping/M.1780035188.A.18E.html"),
        ("2026/05/30", "決策之眼 (新聞搜尋)", "架設爬蟲網站，可以關鍵字搜尋新聞，並且按照台灣的時序排列。", "https://www.ptt.cc/bbs/Gossiping/M.1780118601.A.41D.html"),
        ("2026/05/31", "創世神手 (Python 線上編譯器)", "第三天：架設 Python 線上編輯器，成功部署雲端編譯環境。", "https://www.ptt.cc/bbs/Gossiping/M.1780226831.A.D00.html"),
        ("2026/06/01", "極光裁決 (YT 縮網址)", "第四天：架設 YT 縮網址線上服務。", "https://www.ptt.cc/bbs/Gossiping/M.1780274581.A.B62.html"),
        ("2026/06/02", "戰略總部入口", "第五天：架設主網站，統合旗下所有線上服務。", "https://luciffar.streamlit.app/"),
        ("2026/06/03", "命運重塑 (樹精靈轉檔)", "第六天：架設國泰樹精靈電腦版 CSV 轉 ODS。自動判斷本地端/網路，兩用版雙刀流程式+網站。", "https://www.ptt.cc/bbs/Stock/M.1780470116.A.663.html")
    ]
    
    for date, title, desc, link in history_data:
        st.markdown(f"""
            <div class='history-card'>
                <span style='color: #FFD700; font-weight: bold; font-size: 1.2em;'>{date} —— {title}</span><br>
                <p style='margin-top: 5px; margin-bottom: 10px; line-height: 1.5;'>{desc}</p>
                <a href='{link}' target='_blank' style='color: #00FF41; text-decoration: none; font-weight: bold;'>[ 查看相關紀錄 / 服務連結 ]</a>
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
            <span class='version-tag'>SYSTEM VERSION: 1.0.1</span>
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

# --- 5. 底部狀態列 ---
st.markdown("---")
st.caption("Dawnstar Command | Operational | All Systems Online")
