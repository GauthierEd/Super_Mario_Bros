import pygame as pg
from .. import constante as c

class Mushroom(pg.sprite.Sprite):
    def __init__(self,x,y,name):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.sprite = pg.image.load("images/sprite_object.png")
        self.load_img()
        self.image = self.frame[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.max_y = y - self.rect.height
        self.vy = -1
        self.vx = 0
        self.state = c.MUSH_SPAWN
    
    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        self.frame = []

        self.frame.append(self.getImage(0,0,16,16))

    def handleState(self):
        if self.state == c.MUSH_SPAWN:
            self.mushSpawn()
            
        elif self.state == c.MUSH_MOVE:
            self.mushMove()

    def update(self):
        self.handleState()

    def mushSpawn(self):
        if self.rect.top > self.max_y:
            self.rect.y += self.vy
        else:
            self.vy = 0
            self.vx = 4
            self.state = c.MUSH_MOVE

    def mushMove(self):
        self.vy += c.GRAVITY

        if self.rect.x < 0:
            self.kill()
        elif self.rect.y > c.HEIGHT:
            self.kill()

class Flower(pg.sprite.Sprite):
    def __init__(self,x,y,name):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.sprite = pg.image.load("images/sprite_object.png")
        self.load_img()
        self.frame_index = 0
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.max_y = y - self.rect.height
        self.vy = -1
        self.state = c.FLOWER_SPAWN
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

        self.frame.append(self.getImage(0,32,16,16))
        self.frame.append(self.getImage(16,32,16,16))
        self.frame.append(self.getImage(32,32,16,16))
        self.frame.append(self.getImage(48,32,16,16))

    def handleState(self):
        if self.state == c.FLOWER_SPAWN:
            self.flowerSpawn()
            
        elif self.state == c.FLOWER_RESTING:
            self.resting()

    def update(self):
        self.current_update = pg.time.get_ticks()
        self.handleState()
        if self.current_update - self.last_update > 100:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 4
        bottom = self.rect.bottom
        left = self.rect.left
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
    
    def flowerSpawn(self):
        if self.rect.top > self.max_y:
            self.rect.y += self.vy
        else:
            self.vy = 0
            self.state = c.FLOWER_RESTING

    def resting(self):
        pass

class Star(pg.sprite.Sprite):
    def __init__(self,x,y,name):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.sprite = pg.image.load("images/sprite_object.png")
        self.load_img()
        self.frame_index = 0
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.max_y = y - self.rect.height
        self.vx = 0
        self.vy = -0.5
        self.state = c.STAR_SPAWN
        self.current_update = 0
        self.last_update = 0
        self.gravity = c.GRAVITY
   
    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        self.frame = []

        self.frame.append(self.getImage(1,48,14 ,16))
        self.frame.append(self.getImage(17,48,14,16))
        self.frame.append(self.getImage(33,48,14,16))
        self.frame.append(self.getImage(49,48,14,16))
    
    def handleState(self):
        if self.state == c.STAR_SPAWN:
            self.starSpawn()
        elif self.state == c.STAR_MOVE:
            self.starMove()

    def update(self):
        self.current_update = pg.time.get_ticks()
        self.handleState()
        if self.current_update - self.last_update > 100:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 4
        bottom = self.rect.bottom
        left = self.rect.left
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
    
    def starSpawn(self):
        if self.rect.top > self.max_y:
            self.rect.y += self.vy
        else:
            self.vy = -8
            self.vx = 3
            self.state = c.STAR_MOVE

    def starMove(self):
        self.vy += self.gravity

        if self.rect.x < 0:
            self.kill()
        elif self.rect.y > c.HEIGHT:
            self.kill()
