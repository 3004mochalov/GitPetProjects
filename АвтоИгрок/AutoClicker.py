import pyautogui
import datetime
from time import sleep, time

def UpDown():
        while True:
                d = (datetime.datetime.now().hour)
                m = (datetime.datetime.now().minute)
                pyautogui.mouseUp()
                sleep(15)
                pyautogui.mouseDown()
                pyautogui.moveRel(-10, 0, duration=0.25)
                sleep(15)
                pyautogui.moveRel(10, 0, duration=0.25)
                if (m == 8) and (d == 2 or d == 6 or d == 10 or d == 14 or d == 18 or d == 22):
                        pyautogui.mouseUp()
                        sleep(420)
                        pyautogui.moveTo(960, 577, duration=3)
                        pyautogui.click(button='left')
                        pyautogui.moveTo(703, 125, duration=3)
                        pyautogui.click(button='left')
                        sleep(180)

UpDown()
