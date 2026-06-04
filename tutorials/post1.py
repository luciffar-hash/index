# VERSION: 2.0.0
# LAST UPDATED: 2026-06-04

import streamlit as st

def show():
    st.markdown("<h2 style='color: #00FF41; text-align: center;'>🎓 智庫技術教學區</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #888; text-align: center;'>人類負責邏輯與體驗，AI 負責技術與產出</p>", unsafe_allow_html=True)
    st.markdown("---")

    # ------ 第一篇：防崩潰計算機卡片 (指向 post2) ------
    st.markdown("""
    <div style='border-left: 5px solid #00FF41; padding-left: 15px; margin-bottom: 15px;'>
        <h4 style='color: #00FF41; margin-bottom: 5px;'>🐍 零基礎、沒改過半行Code！我如何用純白話驅動AI 在20分鐘內打造「防崩潰計算機」？</h4>
        <p style='color: #666; font-size: 0.85rem; margin-bottom: 10px;'>發布日期：2026-06-04 | 分類：AI 協作實戰</p>
        <p style='color: #BBB;'>不會寫程式，也能當軟體設計師？本文將帶你完整直擊這場「AI協作」的黃金開發歷程！看作者如何用純白話討論與描述驅動 AI 自動產出程式碼...</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("👉 點擊閱讀全文 & 複製原始碼", key="go_to_calc"):
        st.query_params["page"] = "post2"
        st.rerun()

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # ------ 第二篇：60秒極速Debug卡片 (指向 post3) ------
    st.markdown("""
    <div style='border-left: 5px solid #00FF41; padding-left: 15px; margin-bottom: 15px;'>
        <h4 style='color: #00FF41; margin-bottom: 5px;'>⚡ 挑戰 60 秒極速 Debug：不懂程式碼沒關係，如何讓你的 Code 在沙箱中重生？</h4>
        <p style='color: #666; font-size: 0.85rem; margin-bottom: 10px;'>發布日期：2026-06-04 | 分類：AI 協作實戰</p>
        <p style='color: #BBB;'>在線上學習 Python 時遇到系統安全機制誤判噴紅字？本文展示如何透過精準的「白話文對話」，在 60 秒內交由 AI 完成急速協作與除錯通關！</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("👉 點擊閱讀全文 & 複製原始碼", key="go_to_debug"):
        st.query_params["page"] = "post3"
        st.rerun()

    st.markdown("<br><br><p style='color: #444; text-align: center; font-size: 0.8rem;'>Dawnstar Command | Operational | All Systems Online</p>", unsafe_allow_html=True)
