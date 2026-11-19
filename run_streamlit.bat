@echo off
title Utkarsh Dwivedi AI-ML Streamlit Portfolio
echo ==========================================================
echo   Starting Utkarsh Dwivedi AI-ML Portfolio on Streamlit...
echo   United College of Engineering and Research (UCER)
echo ==========================================================
cd /d "%~dp0"
streamlit run app.py --server.port 8501
pause
