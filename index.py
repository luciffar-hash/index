import streamlit as st

# --- 1. 頁面配置 ---
st.set_page_config(
    page_title="Luciffar AI: Dawnstar Command", 
    layout="centered",
    page_icon="⭐"
)

# --- 2. 戰情室 CSS 樣式 ---
st.markdown("""
    <style>
    .stApp { background-color: #0A0A0A; color: #FFFFFF; }
    h1, h2, h3 { color: #FFD700; }
    /* 版號與名稱整合標籤 */
    .header-tag { 
        background-color: #333; color: #FFD700; 
        padding: 5px 15px; font-size: 0.9rem; 
        border-left: 4px solid #FFD700; margin-bottom: 15px;
        display: block; font-family: sans-serif;
    }
    .stButton>button { 
        width: 100%; border: 1px solid #FFD700; color: #FFD700; 
        background: transparent; border-radius: 0px; margin-top: 10px;
    }
    .stButton>button:hover { background: #FFD700; color: #0A0A0A; }
    </style>
""", unsafe_allow_html=True)

# --- 3. 頁面頂部 ---
# 將名稱與版號整合為一個戰略識別區塊
st.markdown("""
    <div class='header-tag'>
        LUCIFFAR AI: DAWNSTAR COMMAND | SYSTEM VERSION: 1.0.0
    </div>
""", unsafe_allow_html=True)

try:
    st.image("logo.jpg", width=250)
except:
    st.error("Error: logo.jpg not found.")

st.title("Luciffar AI")
st.subheader("Dawnstar Command")
st.markdown("---")

# --- 4. 戰略指揮面板 ---
st.write("#### 🛡️ 戰略指揮模組 (Active Command Deck)")

tools = [
    {"name": "Decision Eye", "url": "https://luciffar-thinktank.streamlit.app/"},
    {"name": "Python Compiler", "url": "https://luciffar-py.streamlit.app/"},
    {"name": "YT Linker", "url": "https://luciffar-yturl.streamlit.app/"},
    {"name": "CSV Converter", "url": "https://luciffar-ods.streamlit.app/"}
]

cols = st.columns(2)
for i, tool in enumerate(tools):
    with cols[i % 2]:
        st.write(f"### {tool['name']}")
        st.link_button(f"EXECUTE", tool['url'], use_container_width=True)
        st.write("") 

# --- 5. 底部狀態列 ---
st.markdown("---")
st.caption("Dawnstar Command | Operational | All Systems Online")