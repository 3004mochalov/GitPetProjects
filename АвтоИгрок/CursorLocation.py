import pyautogui
import winsound
import tkinter.messagebox as mb
n = 0
while n != 5:
    winsound.Beep(300, 1000)
    n += 1
n = 0
while n != 10:
    winsound.Beep(300, 500)
    n += 1
n = 0
while n != 10:
    winsound.Beep(300, 300)
    n += 1
n = 0
while n != 10:
    winsound.Beep(400, 200)
    n += 1

def show_info():
    msg = pyautogui.position()
    mb.showinfo("Cursor Location (x | y)", msg)
show_info()