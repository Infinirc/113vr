#!/bin/bash


sudo apt update
sudo apt install -y python3 python3-pip


python3 -m pip install --upgrade pip


pip3 install streamlit
pip3 install pandas
pip3 install matplotlib




streamlit run main.py
