# SYSTEM VERSION: 1.0.0
# LAST UPDATED: 2026-06-01

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
    
    .header-tag { 
        background-color: #1a1a1a; padding: 20px; 
        border-left: 6px solid #00FF41; margin-bottom: 30px;
    }
    .chinese-title { color: #00FF41; font-weight: bold; font-size: 3em; display: block; line-height: 1.2; }
    .english-title { color: #00FF41; font-size: 3em; font-family: monospace; display: block; line-height: 1.2; }
    .version-tag { color: #888; font-size: 1.2em; margin-top: 10px; display: block; }
    
    .stButton>button { 
        width: 100%; border: 1px solid #FFD700; color: #FFD700; 
        background: transparent; border-radius: 0px; margin-top: 10px;
    }
    .stButton>button:hover { background: #FFD700; color: #0A0A0A; }
    </style>
""", unsafe_allow_html=True)

# --- 3. 頁面頂部 ---
try:
    st.image("logo.png", width=250)
except:
    st.write("", unsafe_allow_html=True)

st.markdown("""
    <div class='header-tag'>
        <span class='chinese-title'>路西法智庫:AI破曉晨星戰略指揮總部</span>
        <span class='english-title'>Luciffar AI: Dawnstar Command</span>
        <span class='version-tag'>SYSTEM VERSION: 1.0.0</span>
    </div>
""", unsafe_allow_html=True)

# --- 4. 戰略指揮面板 ---
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
