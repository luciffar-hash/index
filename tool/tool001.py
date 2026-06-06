# VERSION: v1.3.0
# LAST UPDATED: 2026-06-06

import streamlit as st
import os

def show():
    # --- 1. 版本號與標題常駐 ---
    st.write("#### 🛠️ 戰術小工具總目錄 (Tactical Tool Arsenal)")
    st.caption("MODULE VERSION: v1.3.0 | STATUS: ACTIVE")
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
        # 修改標題顏色為綠色
        st.markdown("#### <span style='color:#00FF41'>🎯 路西法智庫梗圖產生器</span>", unsafe_allow_html=True)
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
        # 修改標題顏色為綠色
        st.markdown("#### <span style='color:#00FF41'>🕹️ 外掛版射擊小遊戲</span>", unsafe_allow_html=True)
        st.caption("📄 連結檔名：`ssa.py`")
        st.markdown("說明：  \n"
                    "• 操作：ASDW 方向控制 | 空白鍵連發 | ENTER 暫停 | ALT+ENTER 全螢幕  \n"
                    "• 特色：無敵 | 一秒十發子彈  \n"
                    "• 道具：白色寶石(子彈兩排) | 紅色寶石(子彈五排) | 黃色寶石(加速)")
        st.markdown("[[查看說明圖](https://i.urusai.cc/Yn2li.png)]")
        
        st.markdown("""
這是一份為小朋友量身打造的程式啟盟教學，強調「創作者」的權力。

成為遊戲的創世神：動手寫出你的專屬射擊遊戲
你是否玩膩了那些一碰到敵人就會「Game Over」的遊戲？市面上的遊戲為了挑戰你，設定了重重限制，但在這裡，規則由你說了算。

今天，我們不用昂貴的引擎，只需幾行簡單的 Python 程式碼，就能創造一個永遠不會失敗、絕對無敵的射擊遊戲。這就是程式設計的魅力：你不是在玩遊戲，你是在「定義」遊戲。

為什麼要寫「無敵」遊戲？
當你不再需要為了「生存」而焦慮時，你可以把全部的專注力放在「創造」上。這段代碼中，你可以自由修改：

速度 (Speed)：將數字改大，角色就能以閃電般的速度穿梭畫面。

火力 (Fire Rate)：將發射間隔縮小，螢幕就能瞬間噴發出無窮無盡的黃金子彈。

視覺效果 (Visuals)：修改顏色數值，讓每一發子彈都變成你喜歡的顏色。

如何體驗創作者的樂趣？
請嘗試找到程式碼中 player_speed = 10 或 fire_rate = 50 這些地方，試著將數字加上一個零。當你按下執行鍵，看到畫面因你的指令而產生劇變時，那就是程式設計賦予你的「魔法」。

給未來的開發者一句話
電腦就像一張畫布，而程式碼就是你的畫筆。透過這段小遊戲，你學會了如何控制物件的移動、碰撞與狀態。當你學會了這些邏輯，下一個步驟，你可以嘗試加入「計分系統」，挑戰自己在不敗的前提下，一分鐘內能粉碎多少掉落物。

不要去適應遊戲的規則，去改寫規則吧！ 從今天起，你不是玩家，你是這個世界的開發者。

你可以從修改 player_speed 這個參數開始，感受一下掌控世界速度的感覺！
""")

    with col4:
        try:
            with open(ssa_file_path, "rb") as file:
                st.download_button(label="DOWNLOAD", data=file, file_name="ssa.py", mime="text/x-python", use_container_width=True)
        except FileNotFoundError:
            st.error("檔案佈署中")

    st.markdown("---")
    st.caption("Luciffar Intelligence Tank | Tool Module Loader")
    st.caption("Luciffar Intelligence Tank | © 2026 Luciffar. All rights reserved.")
