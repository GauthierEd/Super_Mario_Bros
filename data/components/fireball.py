import pygame as pg
from .. import constante as c 

class FireBall(pg.sprite.Sprite):
    def __init__(self,x,y,direction):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_object.png")
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y - self.rect.height
        self.gravity = c.GRAVITY
        self.vy = 0
        self.vx = 10 * direction
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

        self.frame.append(self.getImage(96,144,8,8))
        self.frame.append(self.getImage(104,144,8,8))
        self.frame.append(self.getImage(96,152,8,8))
        self.frame.append(self.getImage(104,152,8,8))
    
    def update(self):
        
        self.current_update = pg.time.get_ticks()

        if self.vy < c.MAX_VEL_Y:
            self.vy += self.gravity
        

        if (self.current_update - self.last_update) > 80:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 3
        
        left = self.rect.left
        bottom = self.rect.bottom
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        if self.rect.y > c.HEIGHT:
            self.kill()
        elif self.rect.x < 0:
            self.kill()
        elif self.rect.x > c.WIDTH:
            self.kill()