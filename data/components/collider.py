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
        self.rect.y = y 
        