# SYSTEM VERSION: 1.0.4
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
        width: 100%;
    }
    
    /* 標題與教學卡片樣式 */
    .chinese-title { 
        color: #00FF41; font-weight: bold; font-size: 1.8em; 
        display: inline-block; vertical-align: middle; margin-right: 15px;
    }
    .english-title { 
        color: #00FFFF; font-size: 1.8em; font-family: monospace; 
        display: inline-block; vertical-align: middle;
    }
    .demo-tag { color: #FF4444; font-size: 1.2em; font-weight: bold; margin-top: 15px; display: block; }
    .version-tag { color: #888; font-size: 1em; margin-top: 5px; display: block; }
    
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
    st.write("教學內容更新中...")

# ================= 頁面分支：歷史 =================
elif current_page == "history":
    st.markdown("<h1 style='text-align: center;'>本站創建歷史</h1>", unsafe_allow_html=True)
    history_data = [
        ("2026/05/29", "起源與覺醒", "測試 AI 能力，問了 PYTHON 難不難學。開始安裝並寫出 HELLO WORLD 與小遊戲。", "#"),
        ("2026/06/03", "命運重塑", "架設國泰樹精靈 CSV 轉 ODS，雙刀流模式。", "#")
    ]
    for date, title, desc, link in history_data:
        st.markdown(f"<div class='history-card'><b>{date} —— {title}</b><p>{desc}</p></div>", unsafe_allow_html=True)

# ================= 頁面分支：主戰情室 =================
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

st.markdown("---")
st.caption("Dawnstar Command | Operational | All Systems Online")
