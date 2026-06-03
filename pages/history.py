# SYSTEM VERSION: 1.0.0
# LAST UPDATED: 2026-06-04

import streamlit as st

st.set_page_config(page_title="本站創建歷史", layout="centered")

# --- CSS 樣式 ---
st.markdown("""
    <style>
    .stApp { background-color: #0A0A0A; color: #FFFFFF; }
    h1 { color: #FFD700; text-align: center; }
    .subtitle { color: #00FF41; text-align: center; font-size: 1.5em; margin-bottom: 30px; font-weight: bold; }
    .history-card { 
        background-color: #1a1a1a; padding: 20px; border-radius: 10px; 
        border-left: 5px solid #FFD700; margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 標題區 ---
st.markdown("<h1>本站創建歷史</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>0基礎驅動AI寫程式架站</div>", unsafe_allow_html=True)

st.markdown("---")

# --- 歷史時序內容 ---
history_data = [
    ("2026/05/29", "起源與覺醒", "測試 AI 能力，建立首個程式碼體驗 (Hello World)", "https://www.ptt.cc/bbs/Gossiping/M.1780035188.A.18E.html"),
    ("2026/05/30", "決策之眼", "架設新聞爬蟲，支援關鍵字搜尋與台灣時序排列", "https://www.ptt.cc/bbs/Gossiping/M.1780118601.A.41D.html"),
    ("2026/05/31", "創世神手", "部署 Python 線上編譯器，實現雲端程式撰寫與運行", "https://www.ptt.cc/bbs/Gossiping/M.1780226831.A.D00.html"),
    ("2026/06/01", "極光裁決", "完成 YouTube 縮網址服務上線", "https://www.ptt.cc/bbs/Gossiping/M.1780274581.A.B62.html"),
    ("2026/06/02", "戰略總部", "完成主入口網站建置，統合旗下所有線上服務", "https://luciffar.streamlit.app/"),
    ("2026/06/03", "命運重塑", "國泰樹精靈 CSV 轉 ODS 工具，雙刀流模式", "https://www.ptt.cc/bbs/Stock/M.1780470116.A.663.html")
]

for date, title, desc, link in history_data:
    st.markdown(f"""
        <div class='history-card'>
            <strong>{date} - {title}</strong><br>
            {desc}<br>
            <a href='{link}' style='color: #00FF41;'>查看戰報紀錄</a>
        </div>
    """, unsafe_allow_html=True)

st.sidebar.link_button("返回戰情總部", "https://luciffar.streamlit.app/")
