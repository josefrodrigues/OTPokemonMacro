## Version 0.1.2
import time
import pyautogui as pg

def combo(hotkeys, delay=0.15):
    # Start
    for item in hotkeys:
        pg.press(item)
        time.sleep(delay)