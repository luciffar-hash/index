# VERSION: 1.1.0
# LAST UPDATED: 2026-06-05
# PATH: /tool/tool001.py
import streamlit as st

def show():
    st.markdown("<h2 style='color: #FFD700;'>🛠️ 工具整備中心 (Arsenal)</h2>", unsafe_allow_html=True)
    st.info("⚠️ 注意：本模組已遷移至專屬 /tool/ 目錄。")
    st.write("這裡是「路西法智庫」開發的戰術腳本存放區。")
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div style='background-color: #1a1a1a; padding: 20px; border-left: 5px solid #00FFFF;'>
                <h4 style='color: #00FFFF;'>🐍 防崩潰計算機 v1.3.3</h4>
                <p style='color: #BBB;'>包含 Tkinter 介面與自動防崩潰邏輯。</p>
            </div>
        """, unsafe_allow_html=True)
        # 由於 index.py 在根目錄，路徑指向 tutorials/post2.py (原始碼所在地)
        try:
            with open("tutorials/post2.py", "rb") as f:
                st.download_button("下載腳本 (.py)", f, file_name="anti_crash_calc.py", key="dl_calc")
        except:
            st.warning("檔案暫不可用")

    with col2:
        st.markdown("""
            <div style='background-color: #1a1a1a; padding: 20px; border-left: 5px solid #FF4444;'>
                <h4 style='color: #FF4444;'>⚡ 60秒極速 Debug 範本</h4>
                <p style='color: #BBB;'>沙箱友善版代碼下載。</p>
            </div>
        """, unsafe_allow_html=True)
        try:
            with open("tutorials/post3.py", "rb") as f:
                st.download_button("下載腳本 (.py)", f, file_name="fast_debug_template.py", key="dl_debug")
        except:
            st.button("尚未開放", disabled=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⬅ 返回主戰略部"):
        st.query_params["page"] = "main"
        st.rerun()
