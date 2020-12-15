import pygame as pg
from .. components import info
from .. import constante as c 
from . import state

class timeOut(state.State):
    def __init__(self):
        state.State.__init__(self)

        
    def startup(self,current_time):
        if info.game_info["lives"] == 0:
            self.next = c.GAMEOVER
        else:
            self.next = c.LOAD
        self.info = info.Info(c.TIMEOUT)
        self.current_update = current_time
        
    
    def draw_everything(self,screen):
        screen.fill((0,0,0))
        self.info.draw(screen)

    def update(self,keys,screen,current_time):
        if current_time - self.current_update < 3000:
            self.info.update(current_time)
            self.draw_everything(screen)
        else:
            self.done = True