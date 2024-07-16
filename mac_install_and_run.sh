#!/bin/bash


if ! command -v brew &>/dev/null; then
    echo "Homebrew 未安裝，正在安裝 Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi


brew install python


python3 -m pip install --upgrade pip


pip3 install streamlit
pip3 install pandas
pip3 install matplotlib


streamlit run main.py
