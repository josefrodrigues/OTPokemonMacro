import time


from utils import move_and_click

class PokeList:
    def __init__(self) -> None:
        self.count = 0
        self.list_pos = [(22,1145), 
                          (22,1190), 
                          (22,1235), 
                          (22,1280), 
                          (22,1325), 
                          (22,1370)]
    
    
    def check_poke_lenght(self):
        self.count = self.count % len(self.list_pos)
    
    def next(self):
        self.count += 1
        self.check_poke_lenght()
        move_and_click(self.list_pos[self.count], 'right')
        time.sleep(1.0)
    
    def previous(self):
        self.count -= 1
        self.check_poke_lenght()
        move_and_click(self.list_pos[self.count], 'right')
        time.sleep(1.0)
    
poke = PokeList()