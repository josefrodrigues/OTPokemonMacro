import time
import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard

LIST_ATTACKS = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10']

def attack(hotkey, delay=0.025):
    # Start
    print("Iniciando o combo")
    for item in hotkey:
        pg.press(f'{item}')
        time.sleep(delay)
    
def key_code(key):
    if key == keyboard.Key.esc:
        return False
    if key == keyboard.Key.f12:
        attack(LIST_ATTACKS)
        
with Listener(on_press=key_code) as listener:
    listener.join()