import streamlit as st
from config import modules

def run():
    # 自訂 CSS 樣式
    st.markdown("""
    <style>
    .stButton > button {
        background-color: #90EE90;  /* 淺綠色 */
        color: black;
        border: none;
        padding: 5px 12px;  /* 減小內邊距 */
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;  /* 減小字體大小 */
        margin: 2px 1px;  /* 減小外邊距 */
        cursor: pointer;
        border-radius: 4px;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #7CFC00;  /* 懸停時的顏色 */
        color: blue;
    }
    .stButton > button:active, .stButton > button:focus {
        background-color: #32CD32;  /* 選中時的顏色 */
        color: white;  /* 選中時的字體顏色 */
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'>光合之旅學習歷程數據分析平台</h1>", unsafe_allow_html=True)
    
    # 使用全寬的列來居中圖像
    col1, col2, col3 = st.columns([1, 3, 1])  # 調整比例以更好地控制居中
    with col2:
        st.image("images/LOGO-1.png", use_column_width=True)  # 使用列寬來自動調整圖像大小

    if 'navigation_triggered' not in st.session_state:
        st.session_state.navigation_triggered = False

    cols = st.columns(len(modules))
    for idx, (label, module_name) in enumerate(modules.items()):
        with cols[idx]:
            if st.button(label):
                st.session_state.navigation_triggered = True
                st.session_state.current_page = label
                st.query_params["page"] = label
                st.rerun()

    # 重置導航標誌在會話周期結束時
    if st.session_state.navigation_triggered:
        st.session_state.navigation_triggered = False

if __name__ == "__main__":
    run()
