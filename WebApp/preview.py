import streamlit as st
import pandas as pd

def run():
    st.title("資料表數據預覽")

    # 顯示數據預覽
    st.subheader("數據預覽")
    url = "https://raw.githubusercontent.com/Infinirc/113vr/main/v1.csv"
    data = pd.read_csv(url)
    st.dataframe(data)

