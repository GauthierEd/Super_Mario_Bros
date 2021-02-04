import pygame as pg
from .. import constante as c

class Collider(pg.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pg.sprite.Sprite.__init__(self)
        self.name = "collider"
        self.w = w * c.BACKGROUND_SIZE_MULTIPLIER
        self.h = h * c.BACKGROUND_SIZE_MULTIPLIER
        self.image = pg.Surface([self.w,self.h],pg.SRCALPHA,32).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER


class Lift(pg.sprite.Sprite):
    def __init__(self,x,y,direction):
        pg.sprite.Sprite.__init__(self)
        self.name = "lift"
        self.sprite = pg.image.load("images/sprite_object.png").convert()
        self.image = self.load_img()
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.vy = 2 * direction
    
    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,(int(w* c.BACKGROUND_SIZE_MULTIPLIER),int(h*c.BACKGROUND_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        self.frame = []
        self.frame.append(self.getImage(208,128,16,8))
        surface = pg.Surface((126,21),pg.SRCALPHA,32).convert_alpha()
        for i in range(3):
            surface.blit(self.frame[0],(i*42,0))
        return surface
    
    def update(self):
        self.rect.y += self.vy
        if self.rect.bottom < 0:
            self.rect.top = c.HEIGHT
        elif self.rect.top > c.HEIGHT:
            self.rect.bottom = 0


class Pipe(pg.sprite.Sprite):
    def __init__(self,x,y,w,h,pirana = None):
        pg.sprite.Sprite.__init__(self)
        self.name = "pipe"
        self.sprite = pg.image.load("images/sprite_tiles.png").convert()
        self.w = w * c.PIPE_SIZE_MULTIPLIER
        self.h = h * c.PIPE_SIZE_MULTIPLIER
        self.nb_body = int((h - 16) / 16)
        self.image = self.load_img()
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.pirana = pirana

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((255,0,255))
        image = pg.transform.scale(image,(int(w* c.PIPE_SIZE_MULTIPLIER),int(h*c.PIPE_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        self.frame = []
        self.frame.append(self.getImage(0,128,32,16))
        self.frame.append(self.getImage(0,144,32,16))

        surface = pg.Surface((self.w,self.h),pg.SRCALPHA,32).convert_alpha()
        surface.blit(self.frame[0],(0,0))
        
        for i in range(1,self.nb_body+1):
            surface.blit(self.frame[1],(0,(16 * i)* c.PIPE_SIZE_MULTIPLIER))
        
        return surface  

