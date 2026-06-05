# SYSTEM VERSION: 1.2.1
# LAST UPDATED: 2026-06-05
# UPDATE NOTE: 重構目錄結構，將工具中心移至專屬 /tool/ 目錄
import streamlit as st

# 嘗試載入教學模組
try: import tutorials.post1 as post1
except ImportError: post1 = None

try: import tutorials.post2 as post2
except ImportError: post2 = None

try: import tutorials.post3 as post3
except ImportError: post3 = None

# 嘗試載入歷史紀錄
try: import history.main as history_mod
except ImportError: history_mod = None

# 【重構點】嘗試載入專屬 /tool/ 目錄下的工具中心
try:
    import tool.tool001 as tool001
except ImportError:
    tool001 = None

st.set_page_config(page_title="Luciffar AI: Dawnstar Command", layout="centered", page_icon="⭐")

# 全域樣式注入 (維持 Dawnstar 經典黑金風格)
st.markdown("""
    <style>
    .stApp { background-color: #0A0A0A; color: #FFFFFF; }
    h1, h2, h3 { color: #FFD700; }
    .nav-bar { background-color: #1a1a1a; padding: 10px; margin-bottom: 20px; border-bottom: 2px solid #FFD700; text-align: left; }
    .nav-link { color: #FFD700 !important; font-weight: bold; font-size: 1.1em; text-decoration: none; padding: 5px 10px; border: 1px solid #FFD700; background-color: #0A0A0A; margin-right: 10px; display: inline-block; }
    .nav-link:hover { background-color: #FFD700; color: #0A0A0A !important; }
    .header-tag { background-color: #1a1a1a; padding: 20px; border-left: 6px solid #00FF41; margin-bottom: 30px; width: 100%; }
    .chinese-title { color: #00FF41; font-weight: bold; font-size: 1.8em; display: inline-block; vertical-align: middle; margin-right: 15px; }
    .english-title { color: #00FFFF; font-size: 1.8em; font-family: monospace; display: inline-block; vertical-align: middle; }
    .version-tag { color: #888; font-size: 1em; margin-top: 5px; display: block; }
    </style>
""", unsafe_allow_html=True)

# 導航欄
st.markdown("""
    <div class='nav-bar'>
        <a href='?page=main' class='nav-link'>🛸 戰略總部</a>
        <a href='?page=tool_center' class='nav-link'>🛠️ 工具整備中心</a>
        <a href='?page=tutorial' class='nav-link'>🎓 教學區</a>
        <a href='?page=history' class='nav-link'>📜 創建歷史</a>
    </div>
""", unsafe_allow_html=True)

# 路由控制
current_page = st.query_params.get("page", "main")

if current_page == "tool_center":
    if tool001 is not None: tool001.show()
    else: st.error("找不到 tool/tool001.py，請確認目錄名稱是否正確。")
elif current_page == "tutorial":
    if post1 is not None: post1.show()
elif current_page == "post2":
    if post2 is not None: post2.show()
elif current_page == "post3":
    if post3 is not None: post3.show()
elif current_page == "history":
    if history_mod is not None: history_mod.show()
else:
    # 預設首頁
    try: st.image("logo.png", width=250)
    except: pass
    st.markdown("""
        <div class='header-tag'>
            <span class='chinese-title'>路西法智庫:AI破曉晨星戰略指揮總部</span>
            <span class='english-title'>Luciffar AI: Dawnstar Command</span>
            <span class='version-tag'>SYSTEM VERSION: 1.2.1 (Restructured)</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("#### 🛡️ 戰略指揮模組 (Active Command Deck)")
    tools = [
        {"name": "決策之眼", "desc": "新聞搜尋", "url": "https://luciffar-thinktank.streamlit.app/"},
        {"name": "極光裁決", "desc": "YT 縮網址", "url": "https://luciffar-yturl.streamlit.app/"},
        {"name": "工具中心", "desc": "腳本下載", "url": "?page=tool_center"}
    ]
    cols = st.columns(3)
    for i, tool in enumerate(tools):
        with cols[i]:
            st.write(f"### {tool['name']}")
            st.caption(tool['desc'])
            if tool['url'].startswith("?"):
                if st.button(f"OPEN", key=f"tool_idx_{i}"):
                    st.query_params["page"] = tool['url'].split("=")[1]
                    st.rerun()
            else:
                st.link_button("EXECUTE", tool['url'], use_container_width=True)

st.markdown("---")
st.caption("Dawnstar Command | Operational | v1.2.1 | All Systems Online")
