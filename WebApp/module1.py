import streamlit as st
import pandas as pd

def run():
    st.title("單元一")

    
    # 顯示數據預覽
    st.subheader("單元一數據預覽")
    url = "https://raw.githubusercontent.com/Infinirc/113vr/main/v1.csv"
    data = pd.read_csv(url)
    
    # 過濾 "Scene_Name" 為 "2_Chapter_1" 的數據
    filtered_data = data[data["Scene_Name"] == "2_Chapter_1"]
    
    # 顯示基本信息
    st.subheader("基本信息")
    st.write(f"總共包含 {len(data)} 條記錄")
    st.write(f"與 '2_Chapter_1' 相關的記錄有 {len(filtered_data)} 條")
    
    # 顯示詳細數據
    st.subheader("詳細數據")
    st.dataframe(filtered_data)
    
    # 顯示統計信息
    st.subheader("統計信息")
    type_counts = filtered_data['type'].value_counts()
    st.write("Type 分佈:")
    st.bar_chart(type_counts)

    if 'answer' in filtered_data.columns:
        answer_counts = filtered_data['answer'].value_counts()
        st.write("Answer 分佈:")
        st.bar_chart(answer_counts)

    if 'correct' in filtered_data.columns:
        correct_counts = filtered_data['correct'].value_counts()
        st.write("Correct 分佈:")
        st.bar_chart(correct_counts)
