#!/bin/bash

if python3 --version ; then

    echo Python is not installed, please install it to continue.
    exit 1

else
    virtualenv -p python3 venv
    source venv/bin/activate

    pip install pyinstaller packaging customtkinter
    pyinstaller --onefile app.py
fi