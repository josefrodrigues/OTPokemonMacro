
import pyautogui as pg



def move_and_click(position, mbtn, click=1):
    original_position = pg.position()
    pg.moveTo(position)
    pg.click(button=mbtn, clicks=click)
    pg.moveTo(original_position)