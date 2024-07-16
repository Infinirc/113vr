@echo off
cd %~dp0
REM 檢查Streamlit是否已安裝，如果未安裝則安裝
python -m pip show matplotlib || python -m pip install matplotlib
python -m pip show pandas || python -m pip install pandas
python -m pip show streamlit || python -m pip install streamlit
REM 執行main.py
start /B streamlit run main.py
REM 等待一定時間後發送 ENTER 鍵
timeout /t 5
powershell -ExecutionPolicy Bypass -File send_enter.ps1
pause
