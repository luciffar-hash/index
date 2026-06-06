# VERSION: 1.2.2
# LAST UPDATED: 2026-06-06

import streamlit as st

# ================= 🛡️ 0. Google Search Console 驗證專屬通道 =================
# 取得目前的頁面參數
current_page = st.query_params.get("page", "main")

# 攔截 Google 驗證請求：當網址為 ?page=google59a00902dc2ee317.html 時精準回應
if current_page == "google59a00902dc2ee317.html":
    st.write("google-site-verification: google59a00902dc2ee317.html")
    st.stop()  # 立刻中斷後續所有程式碼執行，確保頁面純淨

# ================= 🛡️ 1. 頁面基本配置 =================
st.set_page_config(
    page_title="Luciffar AI: Dawnstar Command", 
    layout="centered",
    page_icon="⭐"
)

# ================= 📦 2. 安全動態掛載外部獨立模組 =================
def safe_import(module_path):
    """安全匯入模組，區分檔案不存在或內部程式碼錯誤"""
    try:
        return __import__(module_path, fromlist=['*'])
    except ModuleNotFoundError:
        return None
    except Exception as e:
        st.error(f"⚠️ 模組 `{module_path}` 載入失敗，內部程式碼存在錯誤：\n`{str(e)}`")
        return None

history_mod = safe_import("history.main")
post1 = safe_import("tutorials.post1")
post2 = safe_import("tutorials.post2")
post3 = safe_import("tutorials.post3")

# --- 小工具控制模組 ---
tool001_mod = safe_import("tool.tool001")

# ================= 🎨 3. 戰情室全域 CSS 最佳化 =================
st.markdown("""
    <style>
    /* 全域背景與文字底色 */
    .stApp { background-color: #0A0A0A; color: #FFFFFF; }
    h1, h2, h3 { color: #FFD700; }
    
    /* 頂部常駐導航條 */
    .nav-bar { 
        background-color: #1a1a1a; padding: 12px; margin-bottom: 25px;
        border-bottom: 2px solid #FFD700; text-align: left;
    }
    .nav-link { 
        color: #FFD700 !important; font-weight: bold; font-size: 1.05em;
        text-decoration: none; padding: 6px 14px; border: 1px solid #FFD700;
        background-color: #0A0A0A; margin-right: 10px; display: inline-block;
        transition: all 0.3s ease;
    }
    .nav-link:hover { background-color: #FFD700; color: #0A0A0A !important; }
    
    /* 戰術大標題外殼 */
    .header-tag { background-color: #1a1a1a; padding: 20px; border-left: 6px solid #00FF41; margin-bottom: 30px; width: 100%; }
    .chinese-title { color: #00FF41; font-weight: bold; font-size: 1.8em; display: inline-block; vertical-align: middle; margin-right: 15px; }
    .english-title { color: #00FFFF; font-size: 1.8em; font-family: monospace; display: inline-block; vertical-align: middle; }
    .demo-tag { color: #FF4444; font-size: 1.2em; font-weight: bold; margin-top: 15px; display: block; }
    .version-tag { color: #888; font-size: 1em; margin-top: 5px; display: block; }
    
    /* 戰略指揮卡片按鈕優化 */
    .stButton>button { 
        width: 100%; border: 1px solid #FFD700 !important; color: #FFD700 !important; 
        background: transparent !important; border-radius: 0px !important; margin-top: 10px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover { background: #FFD700 !important; color: #0A0A0A !important; }
    </style>
""", unsafe_allow_html=True)

# ================= 🧭 4. 頂部導航欄 (新增小工具入口) =================
st.markdown("""
    <div class='nav-bar'>
        <a href='?page=main' target='_self' class='nav-link'>🛸 戰略總部</a>
        <a href='?page=history' target='_self' class='nav-link'>📜 本站創建歷史</a>
        <a href='?page=tutorial' target='_self' class='nav-link'>🎓 教學區</a>
        <a href='?page=tool001' target='_self' class='nav-link'>🛠️ 戰術小工具</a>
    </div>
""", unsafe_allow_html=True)

# ================= 🔀 5. 戰術核心路由邏輯 =================

# 分支：教學區主頁
if current_page == "tutorial":
    if post1 is not None:
        post1.show()
    else:
        st.error("❌ 找不到教學總目錄檔案，請確認 `tutorials/post1.py` 是否存在且無語法錯誤。")

# 分支：第一篇教學文章
elif current_page == "post2":
    if post2 is not None:
        post2.show()
    else:
        st.error("❌ 找不到教學文章檔案，請確認 `tutorials/post2.py` 是否存在且無語法錯誤。")

# 分支：第二篇教學文章
elif current_page == "post3":
    if post3 is not None:
        post3.show()
    else:
        st.error("❌ 找不到教學文章檔案，請確認 `tutorials/post3.py` 是否存在且無語法錯誤。")

# 分支：歷史
elif current_page == "history":
    if history_mod is not None:
        history_mod.show()
    else:
        st.error("❌ 找不到歷史紀錄檔案，請確認 `history/main.py` 是否存在且無語法錯誤。")

# 戰術小工具主控頁
elif current_page == "tool001":
    if tool001_mod is not None:
        tool001_mod.show()
    else:
        st.info("🛠️ **戰術小工具模組佈署中**")
        st.write("此分頁已成功由 `index.py` 接管。請等待指揮官下達後續擴充命令以建立 `tool/tool001.py`。")

# 分支：主戰情室
else:
    try:
        st.image("logo.png", width=250)
    except Exception:
        pass

    st.markdown("""
        <div class='header-tag'>
            <span class='chinese-title'>路西法智庫:AI破曉晨星戰略指揮總部</span>
            <span class='english-title'>Luciffar AI: Dawnstar Command</span>
            <span class='demo-tag'>0基礎驅動AI寫程式架站：功能示範展示</span>
            <span class='version-tag'>SYSTEM VERSION: 1.2.2</span>
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
            st.markdown(f"### {tool['name']}")
            st.markdown(f"*{tool['desc']}*")
            st.caption(tool['eng'])
            st.link_button("EXECUTE", tool['url'], use_container_width=True)
            st.write("") 

# ================= 🏁 6. 全域頁尾 =================
st.markdown("---")
st.caption("Dawnstar Command | Operational | All Systems Online")
