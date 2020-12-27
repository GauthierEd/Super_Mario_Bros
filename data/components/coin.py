import pygame as pg
from .. import constante as c

class Coin(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_object.png").convert()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y - self.rect.height
        self.initial_y = self.rect.y + 1
        self.gravity = c.GRAVITY
        self.vy = -20
        self.current_update = 0
        self.last_update = 0

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(6,113,4,14))
        self.frame.append(self.getImage(20,113,8,14))
        self.frame.append(self.getImage(38,113,4,14))
        self.frame.append(self.getImage(56,113,1,14))


    def update(self,current_time):
        self.current_update = current_time

        self.vy += self.gravity
        self.rect.y += self.vy

        if (self.current_update - self.last_update) > 80:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 3
        
        left = self.rect.left
        bottom = self.rect.bottom
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        if self.rect.y > self.initial_y:
            self.kill()

class flash_coin(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_object.png").convert()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 60
        self.current_update = 0
        self.last_update = 0
    
    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((255,255,255))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(1,160,5,8))
        self.frame.append(self.getImage(9,160,5,8))
        self.frame.append(self.getImage(17,160,5,8))

    def update(self):
        self.current_update = pg.time.get_ticks()
        if self.last_update == 0:
            self.last_update = self.current_update
        elif self.time_between_2_date(200,250):
            self.frame_index = 0
        elif self.time_between_2_date(750,800):
            self.frame_index = 1
        elif self.time_between_2_date(875,925):
            self.frame_index = 2
            self.last_update = 0
        
        bottom = self.rect.bottom
        left = self.rect.left
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
    
    def time_between_2_date(self,t1,t2):
        if (self.current_update - self.last_update) >= t1 and (self.current_update - self.last_update) < t2:
            return True

class BigCoin(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_object.png").convert()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.current_update = 0
        self.last_update = 0

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((255,255,255))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(3,98,10,14))
        self.frame.append(self.getImage(19,98,10,14))
        self.frame.append(self.getImage(35,98,10,14))
    
    def update(self,current_time):
        self.current_update = current_time
        if self.last_update == 0:
            self.last_update = self.current_update
        elif self.time_between_2_date(200,250):
            self.frame_index = 0
        elif self.time_between_2_date(750,800):
            self.frame_index = 1
        elif self.time_between_2_date(875,925):
            self.frame_index = 2
            self.last_update = 0
    
        bottom = self.rect.bottom
        left = self.rect.left
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
    
    def time_between_2_date(self,t1,t2):
        if (self.current_update - self.last_update) >= t1 and (self.current_update - self.last_update) < t2:
            return True