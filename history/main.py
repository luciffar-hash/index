#版號 V1.6.0
# history/main.py
import streamlit as st

def show():
    st.markdown("<h1 style='text-align: center;'>📜 本站創建歷史</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00FF41; text-align: center; font-size: 1.5em; font-weight: bold;'>0基礎驅動AI寫程式架站</p>", unsafe_allow_html=True)
    st.write("**作者背景**：無程式語言基礎")
    st.caption("目前版本：V1.6.0")
    st.markdown("---")
    
    # 歷史事件資料庫（最新事件已成功追加於末端）
    history_data = [
        ("2026/05/29", "起源與覺醒", "測試 AI 能力，問了 PYTHON 難不難學。開始安裝並寫出 HELLO WORLD 與小遊戲。", "https://www.ptt.cc/bbs/Gossiping/M.1780035188.A.18E.html"),
        ("2026/05/30", "決策之眼", "架設爬蟲網站，支援關鍵字搜尋新聞並按時序排列。", "https://www.ptt.cc/bbs/Gossiping/M.1780118601.A.41D.html"),
        ("2026/05/31", "創世神手", "架設 Python 線上編輯器，部署雲端編譯環境。", "https://www.ptt.cc/bbs/Gossiping/M.1780226831.A.D00.html"),
        ("2026/06/01", "極光裁決", "架設 YT 縮網址線上服務。", "https://www.ptt.cc/bbs/Gossiping/M.1780274581.A.B62.html"),
        ("2026/06/02", "戰略總部", "架設主網站，統合旗下所有服務。", "https://luciffar.streamlit.app/"),
        ("2026/06/03", "命運重塑", "架設國泰樹精靈 CSV 轉 ODS，雙刀流模式。", "https://www.ptt.cc/bbs/Stock/M.1780470116.A.663.html"),
        ("2026/06/04", "新增教學區", "智庫技術教學區正式開闢！首篇教學上線：🐍 零基礎、沒改過半行Code！我如何用純白話驅動AI在20分鐘內打造「防崩潰計算機」？詳細紀錄白話溝通、極端測試與AI協作的黃金歷程。", "https://luciffar.streamlit.app/~/+/?page=tutorial"),
        ("2026/06/05", "新增戰術小工具", "智庫戰術小工具存放各式 Python 原始檔等提供下載學習參考。1. 本地端運行如有缺任何插件請直接截圖詢問 AI 如何 CMD 安裝。2. 程式碼如有疑慮可先貼入 AI 請 AI 分析安全性。", "https://luciffar.streamlit.app/")
    ]
    
    for date, title, desc, link in history_data:
        # 判斷連結是否為內部頁面跳轉
        target_blank = "target='_blank'" if link.startswith("http") else ""
        
        st.markdown(f"""
            <div class='history-card'>
                <span style='color: #FFD700; font-weight: bold; font-size: 1.2em;'>{date} —— {title}</span><br>
                <p style='margin-top: 5px; margin-bottom: 10px; line-height: 1.5;'>{desc}</p>
                <a href='{link}' {target_blank} style='color: #00FF41; text-decoration: none; font-weight: bold;'>[ 查看紀錄 / 服務連結 ]</a>
            </div>
        """, unsafe_allow_html=True)
