import pyautogui
from time import sleep


def TrainAttack(k):
    n = 0
    while n != k:
        pyautogui.press('w')
        pyautogui.press('d')
        pyautogui.press('a')
        pyautogui.press('w')
        pyautogui.press('d')
        pyautogui.press('a')
        pyautogui.press('w')
        pyautogui.press('d')
        pyautogui.press('a')
        pyautogui.press('w')
        pyautogui.press('d')
        pyautogui.press('a')
        n += 1


sleep(15)
TrainAttack(25000)
