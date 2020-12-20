import pygame as pg
from .. import constante as c

class Gumba(pg.sprite.Sprite):
    def __init__(self,x,y,direction,name = "gumba"):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_ennemy.png").convert_alpha()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.vx = 1.5 * direction
        self.vy = 0
        self.gravity = c.GRAVITY
        self.state = c.WALK
        self.name = name
        self.current_update = 0
        self.last_update = 0
        self.death_update = 0

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((255,255,255))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(0,16,16,16)) 
        self.frame.append(self.getImage(16,16,16,16))
        self.frame.append(self.getImage(32,24,16,8)) # death
        self.frame.append(pg.transform.flip(self.getImage(0,16,16,16),True,True))

    def update(self):
        self.current_update = pg.time.get_ticks()
        self.handleState()

    def handleState(self):
        if self.state == c.WALK:
            self.move()
        elif self.state == c.DEATH:
            self.death()

    def startToDeath(self):
        self.frame_index = 2
        self.state = c.DEATH
        self.vx = 0
        self.vy = 0
        self.gravity = 0
        self.death_update = self.current_update
        left = self.rect.left
        bottom = self.rect.bottom
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def jumpToDeath(self):
        self.frame_index = 3
        self.vx = 5
        self.vy = -10
        self.death_update = self.current_update
        self.state = c.DEATH
        left = self.rect.left
        bottom = self.rect.bottom
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def death(self):
        self.vy += self.gravity
        self.rect.y += round(self.vy)
        self.rect.x += round(self.vx)
        if self.current_update - self.death_update > 500:
            self.kill()

    def move(self):
        if self.vy < c.MAX_VEL_Y:
            self.vy += self.gravity

        if self.current_update - self.last_update > 110:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 2

        left = self.rect.left
        bottom = self.rect.bottom
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        if self.rect.y > c.HEIGHT:
            self.kill()
        


class Koopa(pg.sprite.Sprite):
    def __init__(self,x,y,direction,name = "koopa"):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_ennemy.png").convert_alpha()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.vx = 2 * direction
        self.vy = 0
        self.gravity = c.GRAVITY
        self.state = c.WALK
        self.name = name
        self.current_update = 0
        self.last_update = 0
        self.death_update = 0

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(96,8,15,24)) 
        self.frame.append(self.getImage(112,9,16,23))
        self.frame.append(pg.transform.flip(self.getImage(160,17,16,14),True,True)) # death
    
    def update(self):
        self.current_update = pg.time.get_ticks()
        self.handleState()

    def handleState(self):
        if self.state == c.WALK:
            self.move()
        elif self.state == c.DEATH:
            self.death()

    def jumpToDeath(self):
        self.frame_index = 2
        self.vx = 5
        self.vy = -10
        self.death_update = self.current_update
        self.state = c.DEATH
        left = self.rect.left
        bottom = self.rect.bottom
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def death(self):
        self.vy += self.gravity
        self.rect.y += round(self.vy)
        self.rect.x += round(self.vx)
        if self.current_update - self.death_update > 500:
            self.kill()


    def move(self):
        if self.vy < c.MAX_VEL_Y:
            self.vy += self.gravity

        if self.current_update - self.last_update > 110:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 2

        left = self.rect.left
        bottom = self.rect.bottom
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        if self.rect.y > c.HEIGHT:
            self.kill()
        

class Shell(pg.sprite.Sprite):
    def __init__(self,x,y,current,group = None,name = "shell"):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_ennemy.png").convert_alpha()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.vx = 0 
        self.vy = 0
        self.gravity = c.GRAVITY
        self.state = c.WALK
        self.name = name
        self.group = group
        self.current_update = 0
        self.death_update = current
    
    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(160,17,16,14)) 
        self.frame.append(self.getImage(176,17,16,15))
        self.frame.append(pg.transform.flip(self.getImage(160,17,16,14),True,True))
    
    def update(self):
        self.current_update = pg.time.get_ticks()
        self.handleState()

    def handleState(self):
        if self.state == c.WALK:
            self.move()
        elif self.state == c.DEATH:
            self.death()
        elif self.state == c.BORN:
            self.born()
        elif self.state == c.RESTING:
            self.rest()

    def jumpToDeath(self):
        self.frame_index = 2
        self.vx = 5
        self.vy = -10
        self.death_update = self.current_update
        self.state = c.DEATH
        left = self.rect.left
        bottom = self.rect.bottom
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
    


    def born(self):
        if self.vx != 0:
            self.state = c.WALK
            self.frame_index = 0
            left = self.rect.left
            bottom = self.rect.bottom
            self.image = self.frame[self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.left = left
            self.rect.bottom = bottom

        if (self.current_update - self.death_update > 100) and (self.current_update - self.death_update < 150):
            self.rect.x += 1
        elif (self.current_update - self.death_update > 400) and (self.current_update - self.death_update < 450):
            self.rect.x -= 1
        elif (self.current_update - self.death_update > 800) and (self.current_update - self.death_update < 850):
            self.rect.x += 1
        elif (self.current_update - self.death_update > 1200) and (self.current_update - self.death_update < 1250):
            self.rect.x -= 1
        elif (self.current_update - self.death_update > 1600) and (self.current_update - self.death_update < 1650):
            self.group.add(Koopa(self.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(self.rect.y - 9) / c.BACKGROUND_SIZE_MULTIPLIER,-1))
            self.kill()

    def rest(self):
        if self.vx != 0:
            self.state = c.WALK
            self.frame_index = 0
            left = self.rect.left
            bottom = self.rect.bottom
            self.image = self.frame[self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.left = left
            self.rect.bottom = bottom

        if self.current_update - self.death_update > 5000:
            self.death_update = self.current_update
            self.frame_index = 1
            left = self.rect.left
            bottom = self.rect.bottom
            self.image = self.frame[self.frame_index]
            self.rect = self.image.get_rect()
            self.rect.left = left
            self.rect.bottom = bottom
            self.state = c.BORN
    
    def move(self):
        self.death_update = self.current_update
        if self.vy < c.MAX_VEL_Y:
            self.vy += self.gravity

        if self.vx == 0:
            self.state = c.RESTING

        if self.rect.y > c.HEIGHT:
            self.kill()
        
    def death(self):
        self.vy += self.gravity
        self.rect.y += round(self.vy)
        self.rect.x += round(self.vx)
        if self.current_update - self.death_update > 500:
            self.kill()