import pyautogui
import datetime
from time import sleep, time

def MoveToSell():
    pyautogui.moveRel(22, 0, duration=5)
    pyautogui.keyDown('w')
    sleep(0.5)
    pyautogui.keyUp('w')
    pyautogui.moveRel(3, -2, duration=2)
    pyautogui.keyDown('w')
    sleep(1)
    pyautogui.keyUp('w')
    pyautogui.moveRel(-3, 4, duration=2)
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')
def WarpShop():
    pyautogui.press('/')
    pyautogui.typewrite('warp shop', interval=0.25)
    pyautogui.press('enter')
def Home():
    pyautogui.press('/')
    pyautogui.typewrite('home', interval=0.25)
    pyautogui.press('enter')
def CollectCrystals(n):
    pyautogui.click(button='right')
    pyautogui.moveTo(808, 94, duration=3)
    pyautogui.keyDown('shift')
    while n != 37:
        pyautogui.click(button='left')
        n += 1
    pyautogui.keyUp('shift')
    pyautogui.press('esc')
def Sell(n):
    pyautogui.click(button='right')
    pyautogui.moveTo(753, 426, duration=2)
    pyautogui.click(button='left')
    pyautogui.moveTo(854, 358, duration=2)
    pyautogui.click(button='left')
    pyautogui.moveTo(1151, 556, duration=2)
    while n != 2400:
        pyautogui.click(button='left')
        n += 1
    pyautogui.press('e')

def go():
    while True:
        sleep(10)
        Home()
        sleep(10)
        CollectCrystals(0)
        WarpShop()
        sleep(10)
        MoveToSell()
        sleep(1)
        Sell(0)
go()