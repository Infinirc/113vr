import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform
from datetime import datetime


system = platform.system()
if system == 'Windows':
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
elif system == 'Darwin':  
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False 

def run():
    st.title("單元一 植物是什麼 學習歷程分析")
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])  
    with col2:
        st.image("images/1-1.png", use_column_width=True)  

   
    data_csv = pd.read_csv("data/v1.csv")

    
    uploaded_files = st.file_uploader("選擇要上傳的 TXT 文件（每個文件代表一個學生）", type="txt", accept_multiple_files=True)
    results = []
    student_details = {}  

    if uploaded_files:
        for uploaded_file in uploaded_files:
            txt_data = pd.read_csv(uploaded_file, names=['historyId', 'timestamp', 'value1', 'value2'], header=None)
            txt_data['timestamp'] = pd.to_datetime(txt_data['timestamp'])
            min_time = txt_data['timestamp'].min()
            max_time = txt_data['timestamp'].max()
            total_time = (max_time - min_time).total_seconds() / 60
            combined_data = pd.merge(txt_data, data_csv, on='historyId')
            student_details[uploaded_file.name] = combined_data

            for scene_name in combined_data['Scene_Name'].unique():
                scene_filtered_data = combined_data[combined_data['Scene_Name'] == scene_name]
                unique_history_ids_in_csv = data_csv[data_csv['Scene_Name'] == scene_name]['historyId'].nunique()
                unique_history_ids_in_combined = scene_filtered_data['historyId'].nunique()
                completion_rate = (unique_history_ids_in_combined / unique_history_ids_in_csv) * 100 if unique_history_ids_in_csv > 0 else 0
                results.append({
                    '學生': uploaded_file.name,
                    '單元': scene_name,
                    '總元素': unique_history_ids_in_csv,
                    '完成元素': unique_history_ids_in_combined,
                    '完成度 (%)': completion_rate,
                    '使用時間 (分鐘)': total_time
                })

        results_df = pd.DataFrame(results)
        display_charts_and_stats(results_df)
        st.markdown("---")

      
        st.subheader("學生操作記錄預覽")
        selected_student = st.selectbox("", options=results_df['學生'].unique())
        if selected_student:
            st.write(f"{selected_student} 的詳細操作記錄")
            st.dataframe(student_details[selected_student])
            
           
            total_time = results_df[results_df['學生'] == selected_student]['使用時間 (分鐘)'].sum()
            total_completion_rate = results_df[results_df['學生'] == selected_student]['完成度 (%)'].mean()
            st.write(f"總共完成花費時間: {total_time:.2f} 分鐘")
            st.write(f"完成度: {total_completion_rate:.2f}%")
            
            st.markdown("---")

def highlight_below_average(s, average):

    tolerance = 0.0001
    return ['background-color: #92a8d1' if v < average - tolerance else '' for v in s]

def display_charts_and_stats(results_df):
    st.subheader("學生單元完成度統計圖")
    average_completion_rate = results_df['完成度 (%)'].mean()
    average_time = results_df['使用時間 (分鐘)'].mean()

    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].bar(results_df['學生'], results_df['完成度 (%)'], color='lightblue')
    ax[0].set_title("每位學生的完成度")
    ax[0].set_xlabel('學生')
    ax[0].set_ylabel('完成度 (%)')
    ax[0].set_xticklabels(results_df['學生'], rotation=45, ha='right')
    ax[1].pie([average_completion_rate, 100 - average_completion_rate], labels=['平均已完成', '平均未完成'], autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgrey'])
    ax[1].set_title("所有學生平均完成度")
    st.pyplot(fig)
    st.markdown("---")
    st.subheader("學生完成度與使用時間")

    styled_df = results_df.style.format({'完成度 (%)': "{:.2f}%", '使用時間 (分鐘)': "{:.2f}"})
    st.write(f"所有學生的平均完成時間為：{average_time:.2f} 分鐘")
    st.write(f"所有學生的平均完成度為：{average_completion_rate:.2f}%")
    styled_df = styled_df.apply(highlight_below_average, average=average_completion_rate, subset=['完成度 (%)'], axis=1)
    styled_df = styled_df.apply(highlight_below_average, average=average_time, subset=['使用時間 (分鐘)'], axis=1)
    st.dataframe(styled_df)


if __name__ == "__main__":
    run()
