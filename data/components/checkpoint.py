import pygame as pg
from .. import constante as c  

class checkPoint(pg.sprite.Sprite):
    def __init__(self,x,y,name = None):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32 * c.BACKGROUND_SIZE_MULTIPLIER,c.HEIGHT), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y
        self.name = name

class FlagEnd(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_object.png")
        self.image = self.getImage(129,2,13,14)
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.vy = 0
        self.state = c.WAITFLAG

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,(int(w* c.BACKGROUND_SIZE_MULTIPLIER),int(h* c.BACKGROUND_SIZE_MULTIPLIER)))
        return image
    
    def update(self):
        self.handleState()

    def handleState(self):
        if self.state == c.SLIDEFLAG:
            self.slideFlag()
        elif self.state == c.WAITFLAG:
            self.waitFlag()

    def slideFlag(self):
        self.vy = -0.5
        self.rect.y += self.vy
        if self.rect.bottom < 121*c.BACKGROUND_SIZE_MULTIPLIER:
            self.vy = 0
            self.state = c.WAITFLAG

    def waitFlag(self):
        pass

class Flag(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_object.png")
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER - self.rect.width
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.vy = 0
        self.state = c.WAITFLAG

    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(128,32,16,16))
        

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,(int(w* c.BACKGROUND_SIZE_MULTIPLIER),int(h* c.BACKGROUND_SIZE_MULTIPLIER)))
        return image
    
    def update(self):
        self.handleState()

    def handleState(self):
        if self.state == c.SLIDEFLAG:
            self.slideFlag()
        elif self.state == c.WAITFLAG:
            self.waitFlag()

    def slideFlag(self):
        self.vy = 4
        self.rect.y += self.vy
        if self.rect.y > 493 - self.rect.height:
            self.vy = 0
            self.state = c.WAITFLAG

    def waitFlag(self):
        pass
