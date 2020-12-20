import pygame as pg
from .. import constante as c
from . power import *
from . coin import *

class CoinBrick(pg.sprite.Sprite):
    def __init__(self,x,y,group = None,content = None,name = "overworld"):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_block.png").convert_alpha()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.initial_height = self.rect.y
        self.vy = 0
        self.state = c.RESTING
        self.last_update = 0
        self.content = content
        self.group = group
        self.name = name

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((255,255,255))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        pass

    def startBump(self):
        self.frame_index = 3
        self.vy = -6
        self.state = c.BUMPED
    
    def handleState(self):
        if self.state == c.RESTING:
            self.resting()
        elif self.state == c.BUMPED:
            self.bumped()
        elif self.state == c.OPENED:
            self.opened()
        

    def bumped(self):
        self.vy += c.GRAVITY
        self.rect.y += round(self.vy)
        if self.rect.y > self.initial_height:
            self.rect.y = self.initial_height
            self.vy = 0
            if self.content == "mush":
                self.group.add(Mushroom(self.rect.x,self.rect.y))
            elif self.content == "flower":
                self.group.add(Flower(self.rect.x,self.rect.y))
            elif self.content == "coin":
                self.group.add(Coin(self.rect.centerx,self.rect.y))
            elif self.content == "star":
                self.group.add(Star(self.rect.centerx,self.rect.y))
            elif self.content == "mushLife":
                self.group.add(MushroomLife(self.rect.x,self.rect.y))
            self.state = c.OPENED

    def time_between_2_date(self,t1,t2):
        if (self.current_update - self.last_update) >= t1 and (self.current_update - self.last_update) < t2:
            return True

    def resting(self):
        if self.last_update == 0:
            self.last_update = self.current_update
        elif self.time_between_2_date(200,250):
            self.frame_index = 0
        elif self.time_between_2_date(750,800):
            self.frame_index = 1
        elif self.time_between_2_date(875,925):
            self.frame_index = 2
            self.last_update = 0
            

    def opened(self):
        pass
        
    def update(self):
        self.current_update = pg.time.get_ticks()
        self.handleState()
        bottom = self.rect.bottom
        left = self.rect.left
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

class CoinBrickOverworld(CoinBrick):
    def __init__(self,x,y,group = None,content = None,name = "overworld"):
        CoinBrick.__init__(self,x,y,group,content,name)
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0
        self.frame.append(self.getImage(80,112,16,16)) # coin brick [1]
        self.frame.append(self.getImage(96,112,16,16)) # coin brick [2]
        self.frame.append(self.getImage(112,112,16,16)) # coin brick [3]
        self.frame.append(self.getImage(128,112,16,16)) # coin brick opened

class CoinBrickUnderground(CoinBrick):
    def __init__(self,x,y,group = None,content = None,name = "underground"):
        CoinBrick.__init__(self,x,y,group,content,name)
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0
        self.frame.append(self.getImage(80,128,16,16)) # coin brick [1]
        self.frame.append(self.getImage(96,128,16,16)) # coin brick [2]
        self.frame.append(self.getImage(112,128,16,16)) # coin brick [3]
        self.frame.append(self.getImage(144,128,16,16)) # coin brick opened