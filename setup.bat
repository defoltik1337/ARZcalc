@echo off
pip install -r requirements.txt
python utils\updates.py
python calculator.py