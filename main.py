## Version 0.1.2
import time
import pyautogui as pg
from pynput.keyboard import Listener
from pynput import keyboard
from PokeList import PokeList

from autoatk import combo

LIST_ATTACKS = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
PLAYER_POSITION = (1305, 690)
autocast = False

poke_list = PokeList()

def key_code(key):
    global autocast
    if key == keyboard.Key.esc:
        print("Finalizando script")
        return False
    if hasattr(key, 'char') and key.char == '1':
        combo(LIST_ATTACKS)
    if hasattr(key, 'char') and key.char == 'e':
        poke_list.next()
        if not autocast:
            time.sleep(0.5)
            combo(LIST_ATTACKS)
    if hasattr(key, 'char') and key.char == 'q':
        poke_list.previous()
        if not autocast:
            time.sleep(0.5)
            combo(LIST_ATTACKS)
    if key == keyboard.Key.f12:
        if not autocast:
            for atk in LIST_ATTACKS:
                pg.keyDown(atk)
            autocast = True
        else:
            for atk in LIST_ATTACKS:
                pg.keyUp(atk)
            autocast = False

with Listener(on_release=key_code) as Listener:
    Listener.join()