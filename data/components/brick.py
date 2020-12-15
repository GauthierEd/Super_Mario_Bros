import pygame as pg
from .. import constante as c
from . power import *
from . coin import *



class Brick(pg.sprite.Sprite):
    def __init__(self,x,y,underground = False,group = None,content = None):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_block.png")
        self.underground = underground
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.initial_height = self.rect.y
        self.vy = 0
        self.state = c.RESTING
        self.content = content
        self.group = group
        self.coin = 6
        

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((255,255,255))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        self.frame = []
        if self.underground:
            self.frame_index = 2
        else:
            self.frame_index = 0
        self.frame.append(self.getImage(272,112,16,16)) # brick
        self.frame.append(self.getImage(320,112,16,16)) # brick opened
        self.frame.append(self.getImage(272,128,16,16)) # brick underground
        self.frame.append(self.getImage(336,128,16,16)) # brick underground opened

    def startBump(self):
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
            self.state = c.RESTING
            if self.content == "star":
                self.group.add(Star(self.rect.centerx,self.rect.y,"star"))
                self.state = c.OPENED
            elif self.content == "coin":
                self.group.add(Coin(self.rect.centerx,self.rect.y))
                self.coin -= 1
                self.state = c.RESTING
                if self.coin == 0:
                    self.content = None
                    self.state = c.OPENED
                

    def resting(self):
        pass

    def opened(self):
        if self.underground:
            self.frame_index = 3
        else:
            self.frame_index = 1
        self.image = self.frame[self.frame_index]
        
    def update(self):
        self.handleState()



class BrickPiece(pg.sprite.Sprite):
    def __init__(self,x,y,vx,vy,frame_index,underground = False):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_block.png")
        self.underground = underground
        self.frame_index = frame_index
        self.loadImg()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vy = vy
        self.vx = vx

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h)).convert()
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((251,251,251))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def loadImg(self):
        self.frame = []
        if self.underground:
            self.frame_index += 4
        self.frame.append(self.getImage(304,112,8,8)) # overworld
        self.frame.append(self.getImage(312,112,8,8))
        self.frame.append(self.getImage(304,120,8,8))
        self.frame.append(self.getImage(312,120,8,8))
        self.frame.append(self.getImage(304,128,8,8)) # underground
        self.frame.append(self.getImage(312,128,8,8))
        self.frame.append(self.getImage(304,136,8,8))
        self.frame.append(self.getImage(312,136,8,8))


    def update(self):
        self.vy += c.GRAVITY

        self.rect.x += round(self.vx)
        self.rect.y += round(self.vy)

        if self.rect.y > c.HEIGHT:
            self.kill()
            
            
                

           