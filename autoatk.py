## Version 0.1.2
import time
import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard

LIST_ATTACKS = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10']

def attack(hotkey, delay=0.2):
    # Start
    for item in hotkey:
        pg.press(f'{item}')
        time.sleep(delay)
    
def key_code(key):
    if key == keyboard.Key.esc:
        print("Finalizando script")
        return False
    if key == keyboard.Key.f12 or keyboard.Key.f4:
        attack(LIST_ATTACKS)

with Listener(on_press=key_code) as Listener:
    Listener.join()