#!/bin/bash

# 安裝 Python（需要 sudo 權限）
sudo apt update
sudo apt install -y python3 python3-pip

# 確保 pip 已安裝最新版本
python3 -m pip install --upgrade pip

# 安裝 Streamlit
pip3 install streamlit
pip3 install pandas
pip3 install matplotlib



# 啟動 main.py
streamlit run main.py
