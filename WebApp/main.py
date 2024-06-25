import streamlit as st
import importlib

# 定義單元和其對應的檔案名稱
modules = {
    "數據表預覽": "preview",
    "單元一": "module1",
    "單元二": "module2",
    "單元三": "module3",
    "單元四": "module4",
    "單元五": "module5",
    "單元六": "module6",
}

# 在側邊欄中添加選擇選項
selection = st.sidebar.selectbox("選擇單元", list(modules.keys()))

# 自定義CSS樣式
st.markdown(
    """
    <style>
    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 根據選擇導入相應的模組並顯示其內容
module = importlib.import_module(modules[selection])
module.run()
