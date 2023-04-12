import pyautogui
import time


i = 1
while i < 2:
    pyautogui.moveTo(150, 250)
    time.sleep(30)
    pyautogui.moveTo(200, 500)
    pyautogui.doubleClick()
\

