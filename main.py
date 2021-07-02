import pyautogui
import time

time.sleep(5)
f = open('file.txt', "r")

for word in f:
    pyautogui.typewrite(word)
    time.sleep(0.5)
    pyautogui.press("enter")