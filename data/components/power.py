import pygame as pg
from .. import constante as c

class Power(pg.sprite.Sprite):
    def __init__(self,x,y,name):
        pg.sprite.Sprite.__init__(self)
        self.name = name
        self.sprite = pg.image.load("images/sprite_object.png").convert_alpha()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.max_y = y - self.rect.height
        self.vx = 0
        self.state = c.POWER_SPAWN
        self.current_update = 0
    
    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image
    
    def load_img(self):
        pass

    def handleState(self):
        if self.state == c.POWER_SPAWN:
            self.powerSpawn()
        elif self.state == c.POWER_MOVE:
            self.powerMove()
        elif self.state == c.POWER_RESTING:
            self.powerResting()

    def update(self,current_time):
        self.current_update = current_time
        self.handleState()
    
    def powerSpawn(self):
        pass

    def powerMove(self):
        pass

    def powerResting(self):
        pass


class Mushroom(Power):
    def __init__(self,x,y,name = "mush"):
        Power.__init__(self,x,y,name)
        self.vy = -1

    def load_img(self):
        self.frame = []
        self.frame_index = 0
        self.frame.append(self.getImage(0,0,16,16))
    
    def powerSpawn(self): 
        if self.rect.top > self.max_y:
            self.rect.y += self.vy
        else:
            self.vy = 0
            self.vx = 4
            self.state = c.POWER_MOVE

    def powerMove(self): 
        self.vy += c.GRAVITY

        if self.rect.x < 0:
            self.kill()
        elif self.rect.y > c.HEIGHT:
            self.kill()
        
class MushroomLife(Mushroom):
    def __init__(self,x,y,name = "mushLife"):
        Mushroom.__init__(self,x,y,name)

    def load_img(self):
        self.frame = []
        self.frame_index = 0
        self.frame.append(self.getImage(16,0,16,16))

class Flower(Power):
    def __init__(self,x,y,name = "flower"):
        Power.__init__(self,x,y,name)
        self.vy = -1
        self.last_update = 0
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0
        self.frame.append(self.getImage(0,32,16,16))
        self.frame.append(self.getImage(16,32,16,16))
        self.frame.append(self.getImage(32,32,16,16))
        self.frame.append(self.getImage(48,32,16,16))
    
    def powerSpawn(self):
        if self.rect.top > self.max_y:
            self.rect.y += self.vy
        else:
            self.vy = 0
            self.state = c.POWER_RESTING
        self.powerAnimation()

    def powerResting(self):
        self.powerAnimation()

    def powerAnimation(self):
        if self.current_update - self.last_update > 100:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 4
        bottom = self.rect.bottom
        left = self.rect.left
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

class Star(Power):
    def __init__(self,x,y,name = "star"):
        Power.__init__(self,x,y,name)
        self.rect.centerx = x
        self.vy = -0.5
        self.last_update = 0
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0
        self.frame.append(self.getImage(1,48,14 ,16))
        self.frame.append(self.getImage(17,48,14,16))
        self.frame.append(self.getImage(33,48,14,16))
        self.frame.append(self.getImage(49,48,14,16))
    
    def powerSpawn(self):
        if self.rect.top > self.max_y:
            self.rect.y += self.vy
        else:
            self.vy = -8
            self.vx = 3
            self.state = c.POWER_MOVE
        self.powerAnimation()

    def powerMove(self):
        self.vy += c.GRAVITY
        if self.rect.x < 0:
            self.kill()
        elif self.rect.y > c.HEIGHT:
            self.kill()
        self.powerAnimation()

    def powerAnimation(self):
        if self.current_update - self.last_update > 100:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 4
        bottom = self.rect.bottom
        left = self.rect.left
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

