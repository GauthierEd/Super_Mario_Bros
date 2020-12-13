import pygame as pg
from pygame.locals import *
from .. components.mario import *
from .. import constante as c  
from .. components import info

class Menu(object):
    def __init__(self):
        self.done = False
        self.next = c.LOAD
        self.startup(0.0)
        
    def startup(self,current_time):
        self.info = info.Info(c.MAIN_MENU)
        self.sprite = pg.image.load("images/sprite_menu.png")
        self.setup_game_info()
        self.setup_background()
        self.setup_mario()
        self.setup_title()
        self.setup_button()

    def cleanup(self):
        self.done = False

    def setup_game_info(self):
        info.game_info = {
            "coin_count" : 0,
            "lives" : 3,
            "time" : 401,
            "scores": 0,
        }

    def setup_mario(self):
        self.mario = Mario(50,c.GROUND_HEIGHT)
 

    def setup_background(self):
        self.background = pg.image.load("images/fond_0.png")
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,(int(self.back_rect.width * c.BACKGROUND_SIZE_MULTIPLIER),int(self.back_rect.height * c.BACKGROUND_SIZE_MULTIPLIER)))
        self.back_rect = self.background.get_rect()
        self.back_rect.x = 0
        self.back_rect.y = 0
    
    def setup_title(self):
        self.title = self.getImage(1,60,176,88)
        self.title_rect = self.title.get_rect()
        self.title_rect.x = 110
        self.title_rect.y = 100
    
    def setup_button(self):
        self.button = self.getImage(3,155,8,8)
        self.button_rect = self.button.get_rect()
        self.button_rect.x = 250
        self.button_rect.y = 380

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((255,0,220))
        image = pg.transform.scale(image,(int(w* 3.4),int(h* c.BACKGROUND_SIZE_MULTIPLIER)))
        return image

    def draw_everything(self,screen):
        screen.blit(self.background,(self.back_rect.x,self.back_rect.y))
        screen.blit(self.mario.image,(self.mario.rect.x,self.mario.rect.y))
        screen.blit(self.title,(self.title_rect.x,self.title_rect.y))
        screen.blit(self.button,(self.button_rect.x,self.button_rect.y))
        self.info.draw(screen)
        

    def update(self,keys,screen,current_time):
        self.info.update(current_time)
        if keys[K_DOWN]:
            if self.button_rect.y == 380:
                self.button_rect.y += 50
        
        elif keys[K_UP]:
            if self.button_rect.y == 430:
                self.button_rect.y -= 50
        
        elif keys[K_RETURN]:
            if self.button_rect.y == 380:
                self.done = True
            elif self.button_rect.y == 430:
                self.done = True

        self.draw_everything(screen)


        

