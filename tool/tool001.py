# VERSION: v1.2.1
# LAST UPDATED: 2026-06-06

import streamlit as st
import os

def show():
    # --- 1. 版本號與標題常駐 ---
    st.write("#### 🛠️ 戰術小工具總目錄 (Tactical Tool Arsenal)")
    st.caption("MODULE VERSION: v1.2.1 | STATUS: ACTIVE")
    st.markdown("---")
    st.info("ℹ️ **操作建議與規範：**\n\n"
            "1. 本地端運行如有缺任何插件，請直接截圖詢問 AI 如何 CMD 安裝。\n"
            "2. 程式碼如有疑慮，可先貼入 AI 請 AI 分析安全性。\n"
            "3. 本工具受著作權保護，嚴禁竄改署名或假冒作者進行二次發佈。")
    
    # --- 2. 工具下載矩陣 ---
    st.write("### 🛸 獨立版腳本下載區")
    st.write("*點擊下方按鈕即可直接下載對應的 Python 腳本至在地端執行。*")
    st.write("")

    # --- 項目一：路西法智庫梗圖產生器 ---
    meme_file_path = os.path.join("tool", "meme.py")
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("#### 🎯 路西法智庫梗圖產生器")
        st.caption("📄 連結檔名：`meme.py` │ 說明：0基礎快速合成網路熱門迷因與戰情梗圖。")
        st.markdown("[[查看說明圖](https://i.urusai.cc/6XH0u.png)]")
    with col2:
        try:
            with open(meme_file_path, "rb") as file:
                st.download_button(label="DOWNLOAD", data=file, file_name="meme.py", mime="text/x-python", use_container_width=True)
        except FileNotFoundError:
            st.error("檔案佈署中")

    st.markdown("---")

    # --- 項目二：外掛版射擊小遊戲 ---
    ssa_file_path = os.path.join("tool", "ssa.py")
    col3, col4 = st.columns([3, 1])
    with col3:
        st.markdown("#### 🕹️ 外掛版射擊小遊戲")
        st.caption("📄 連結檔名：`ssa.py`")
        st.markdown("說明：  \n"
                    "• 操作：ASDW 方向控制 | 空白鍵連發 | ENTER 暫停 | ALT+ENTER 全螢幕  \n"
                    "• 特色：無敵 | 一秒十發子彈  \n"
                    "• 道具：白色寶石(子彈兩排) | 紅色寶石(子彈五排) | 黃色寶石(加速)")
        st.markdown("[[查看說明圖](https://i.urusai.cc/Yn2li.png)]")
    with col4:
        try:
            with open(ssa_file_path, "rb") as file:
                st.download_button(label="DOWNLOAD", data=file, file_name="ssa.py", mime="text/x-python", use_container_width=True)
        except FileNotFoundError:
            st.error("檔案佈署中")

    st.markdown("---")
    st.caption("Luciffar Intelligence Tank | Tool Module Loader")
    st.caption("Luciffar Intelligence Tank | © 2026 Luciffar. All rights reserved.")
