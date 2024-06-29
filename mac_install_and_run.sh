#!/bin/bash

# 檢查並安裝 Homebrew（如果尚未安裝）
if ! command -v brew &>/dev/null; then
    echo "Homebrew 未安裝，正在安裝 Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# 安裝 Python
brew install python

# 確保 pip 已安裝最新版本
python3 -m pip install --upgrade pip

# 安裝 Streamlit
pip3 install streamlit
pip3 install pandas
pip3 install matplotlib

# 啟動 main.py
streamlit run main.py
