import pyautogui
import time

text = 'auto message'
while True:
    time.sleep(2)
    pyautogui.typewrite(text)
    time.sleep(2)
    pyautogui.press('enter')
