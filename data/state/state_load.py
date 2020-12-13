import pygame as pg
from .. components.mario import *
from .. import constante as c  
from .. components import info
from .. import sound
from . import state

class Load(state.State):
    def __init__(self):
        state.State.__init__(self)

    def startup(self,current_time):
        self.next = c.LEVEL
        self.info = info.Info(c.LOAD)
        self.current_update = current_time
        info.game_info["time"] = 401


    def draw_everything(self,screen):
        screen.fill((0,0,0))
        self.info.draw(screen)

    def update(self,keys,screen,current_time):
        if current_time - self.current_update < 3000:
            self.info.update(current_time)
            self.draw_everything(screen)
        elif current_time - self.current_update < 3500:
            screen.fill((0,0,0))
        else:
            self.done = True
            sound.main.play(-1)
