import pygame as pg
from .. components import info
from .. import constante as c 

class timeOut(object):
    def __init__(self):
        self.done = False
        self.next = c.LOAD
        self.current_update = 0
        
    def startup(self,current_time):
        if info.game_info["lives"] == 0:
            self.next = c.GAMEOVER
        else:
            self.next = c.LOAD
        self.info = info.Info(c.TIMEOUT)
        self.current_update = current_time
        
    def cleanup(self):
        self.done = False
    
    def update(self,keys,screen,current_time):
        if current_time - self.current_update < 3000:
            self.info.update(current_time)
            screen.fill((0,0,0))
            self.info.draw(screen)
        else:
            self.done = True