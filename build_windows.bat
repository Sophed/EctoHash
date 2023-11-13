@echo off

python3 -m pip --version || pause && goto:EOF

pip install pyinstaller packaging customtkinter
pyinstaller -i icon.ico --onefile app.py