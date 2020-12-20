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
        self.multi = info.game_info["multi"]


    def draw_everything(self,screen):
        screen.fill((0,0,0))
    
    def draw_mario(self,screen):
        self.info.draw_load_mario(screen)
    
    def draw_luigi(self,screen):
        self.info.draw_load_luigi(screen)

    def update(self,keys,screen,current_time):
        if not self.multi:
            if current_time - self.current_update < 3000:
                self.info.update(current_time)
                self.draw_everything(screen)
                self.draw_mario(screen)
            elif current_time - self.current_update < 3500:
                screen.fill((0,0,0))
            else:
                self.done = True
                sound.main.play(-1)
        else:
            if info.game_info["mario_lifes"] > 0 and info.game_info["luigi_lifes"] > 0:
                if current_time - self.current_update < 3000:
                    self.info.update(current_time)
                    self.draw_everything(screen)
                    self.draw_mario(screen)
                elif current_time - self.current_update < 3500:
                    screen.fill((0,0,0))
                elif current_time - self.current_update < 6500:
                    self.info.update(current_time)
                    self.draw_everything(screen)
                    self.draw_luigi(screen)
                elif current_time - self.current_update < 7000:
                    screen.fill((0,0,0))
                else:
                    self.done = True
                    sound.main.play(-1)
            elif info.game_info["mario_lifes"] > 0 and info.game_info["luigi_lifes"] == 0:
                if current_time - self.current_update < 3000:
                    self.info.update(current_time)
                    self.draw_everything(screen)
                    self.draw_mario(screen)
                elif current_time - self.current_update < 3500:
                    screen.fill((0,0,0))
                else:
                    self.done = True
                    sound.main.play(-1)
            elif info.game_info["mario_lifes"] == 0 and info.game_info["luigi_lifes"] > 0:
                if current_time - self.current_update < 3000:
                    self.info.update(current_time)
                    self.draw_everything(screen)
                    self.draw_luigi(screen)
                elif current_time - self.current_update < 3500:
                    screen.fill((0,0,0))
                else:
                    self.done = True
                    sound.main.play(-1)

