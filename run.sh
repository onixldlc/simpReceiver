#! /bin/sh
if [ ! -d "./simpReceiver/Scripts/" ]; then
  python -m venv "simpReceiver"
fi

source ./simpReceiver/Scripts/activate

pip install pyautogui

python main.py

