import pygame as pg
from .. components import info
from .. import sound
from .. import constante as c 

class GameOver(object):
    def __init__(self):
        self.done = False
        self.next = c.MAIN_MENU
        self.current_update = 0
        
    def startup(self,current_time):
        sound.gameover.play()
        self.info = info.Info(c.GAMEOVER)
        self.current_update = current_time

        
    def cleanup(self):
        self.done = False
    
    def update(self,keys,screen,current_time):
        if current_time - self.current_update < 4000:
            self.info.update(current_time)
            screen.fill((0,0,0))
            self.info.draw(screen)
        else:
            self.done = True