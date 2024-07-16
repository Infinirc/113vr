import streamlit as st
import importlib
from config import modules


st.set_page_config(
    page_title="光合之旅學習歷程數據分析平台", 
    page_icon="images/LOGO-1.png",  
    layout="wide"  
)

def load_module(module_name):
    module = importlib.import_module(module_name)
    with st.spinner(f'正在加載 {module_name} 模組...'):
        module.run()

if 'current_page' not in st.session_state:
    st.session_state.current_page = "首頁"

url_page = st.query_params.get("page", "首頁")
if url_page != st.session_state.current_page and not st.session_state.get('navigation_triggered', False):
    st.session_state.current_page = url_page

selection = st.sidebar.selectbox("選擇單元", list(modules.keys()), index=list(modules.keys()).index(st.session_state.current_page))
if selection != st.session_state.current_page:
    st.session_state.current_page = selection
    st.query_params["page"] = selection
    st.experimental_rerun()


with st.spinner(f'正在加載 {modules[st.session_state.current_page]} 模組...'):
    load_module(modules[st.session_state.current_page])

st.markdown("""
<style>
.main .block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-right: 2rem;
    padding-left: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)
