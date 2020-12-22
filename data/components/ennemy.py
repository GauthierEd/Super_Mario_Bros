import pygame as pg
from .. import constante as c
"""
__init__ :  sprite
            load_img
            self.image
            self.rect
            x
            y
            vx # diff for gumba and koopa
            vy = 0 
            gravity
            state
            name
            current_update
            last_update
            death_update
"""

class Ennemy(pg.sprite.Sprite):
    def __init__(self,x,y,direction):
        pg.sprite.Sprite.__init__(self)
        self.name = None
        self.sprite = pg.image.load("images/sprite_ennemy.png").convert()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.vx = 0 
        self.vy = 0
        self.gravity = c.GRAVITY
        self.state = c.WALK
        self.current_update = 0
        self.last_update = 0
        self.death_update = 0
    
    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((255,0,255))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        pass
    
    def update(self,current_time):
        self.current_update = current_time
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
        pass

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

    

class Gumba(Ennemy):
    def __init__(self,x,y,direction):
        Ennemy.__init__(self,x,y,direction)
        self.vx = 1.5 * direction
        self.name = "gumba"

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
    
class GumbaOverworld(Gumba):
    def __init__(self,x,y,direction):
        Gumba.__init__(self,x,y,direction)
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(0,16,16,16)) 
        self.frame.append(self.getImage(16,16,16,16))
        self.frame.append(self.getImage(32,24,16,8)) # death
        self.frame.append(pg.transform.flip(self.getImage(0,16,16,16),True,True))

class GumbaUnderground(Gumba):
    def __init__(self,x,y,direction):
        Gumba.__init__(self,x,y,direction)
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(0,48,16,16)) 
        self.frame.append(self.getImage(16,48,16,16))
        self.frame.append(self.getImage(32,56,16,8)) # death
        self.frame.append(pg.transform.flip(self.getImage(0,48,16,16),True,True))

class Koopa(Ennemy):
    def __init__(self,x,y,direction):
        Ennemy.__init__(self,x,y,direction)
        self.vx = 2 * direction
        self.name = "koopa"
    
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

class KoopaOverworld(Koopa):
    def __init__(self,x,y,direction):
        Koopa.__init__(self,x,y,direction)
        self.type = "green"
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(96,8,15,24)) 
        self.frame.append(self.getImage(112,9,16,23))
        self.frame.append(pg.transform.flip(self.getImage(160,17,16,14),True,True)) # death

class KoopaUnderground(Koopa):
    def __init__(self,x,y,direction):
        Koopa.__init__(self,x,y,direction)
        self.type = "blue"

    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(96,40,15,24)) 
        self.frame.append(self.getImage(112,41,16,23))
        self.frame.append(pg.transform.flip(self.getImage(160,49,16,14),True,True)) # death

class KoopaRed(Koopa):
    def __init__(self,x,y,direction):
        Koopa.__init__(self,x,y,direction)
        self.type = "red"
            
    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(96,72,15,24)) 
        self.frame.append(self.getImage(112,73,16,23))
        self.frame.append(pg.transform.flip(self.getImage(160,81,16,14),True,True)) # death

class Shell(pg.sprite.Sprite):
    def __init__(self,x,y,current,group = None):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images/sprite_ennemy.png").convert()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.vx = 0 
        self.vy = 0
        self.gravity = c.GRAVITY
        self.state = c.WALK
        self.name = "shell"
        self.group = group
        self.current_update = 0
        self.death_update = current
    
    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((255,0,255))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        pass
    
    def update(self,current_time):
        self.current_update = current_time
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
        pass
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

class ShellOverworld(Shell):
    def __init__(self,x,y,current,group = None):
        Shell.__init__(self,x,y,current,group)
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(160,17,16,14)) 
        self.frame.append(self.getImage(176,17,16,15))
        self.frame.append(pg.transform.flip(self.getImage(160,17,16,14),True,True))

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
            self.group.add(KoopaOverworld(self.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(self.rect.y - 9) / c.BACKGROUND_SIZE_MULTIPLIER,-1))
            self.kill()

class ShellUnderground(Shell):
    def __init__(self,x,y,current,group = None):
        Shell.__init__(self,x,y,current,group)
    
    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(160,49,16,14)) 
        self.frame.append(self.getImage(176,49,16,15))
        self.frame.append(pg.transform.flip(self.getImage(160,49,16,14),True,True))
    
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
            self.group.add(KoopaUnderground(self.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(self.rect.y - 9) / c.BACKGROUND_SIZE_MULTIPLIER,-1))
            self.kill()

class ShellRed(Shell):
    def __init__(self,x,y,current,group = None):
        Shell.__init__(self,x,y,current,group)

    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(160,81,16,14)) 
        self.frame.append(self.getImage(176,81,16,15))
        self.frame.append(pg.transform.flip(self.getImage(160,81,16,14),True,True))
    
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
            self.group.add(KoopaRed(self.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(self.rect.y - 9) / c.BACKGROUND_SIZE_MULTIPLIER,-1))
            self.kill()

class Pirana(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.name = "pirana"
        self.sprite = pg.image.load("images/sprite_ennemy.png").convert()
        self.load_img()
        self.image = self.frame[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x * c.BACKGROUND_SIZE_MULTIPLIER
        self.rect.y = y * c.BACKGROUND_SIZE_MULTIPLIER
        self.max_y = int(y * c.BACKGROUND_SIZE_MULTIPLIER - self.rect.h)
        self.min_y = self.rect.y + 10
        self.vy = -1
        self.vx = 0
        self.state = c.MOVEUP
        self.current_update = 0
        self.last_update = 0
        self.move_update = 0
        self.death_update = 0

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((255,0,255))
        image = pg.transform.scale(image,(int(w* c.BRICK_SIZE_MULTIPLIER),int(h* c.BRICK_SIZE_MULTIPLIER)))
        return image

    def load_img(self):
        self.frame = []
        self.frame_index = 0

        self.frame.append(self.getImage(192,41,16,23)) 
        self.frame.append(self.getImage(208,40,16,24))
        self.frame.append(pg.transform.flip(self.getImage(192,41,16,23),True,True))
    
    def update(self,current_time):
        self.current_update = current_time
        self.handleState()
       
        
    def handleState(self):
        if self.state == c.MOVEUP:
            self.moveUp()
        elif self.state == c.MOVEDOWN:
            self.moveDown()
        elif self.state == c.RESTING:
            self.rest()
        elif self.state == c.DEATH:
            self.death()
    
    def moveUp(self):
        if self.current_update - self.last_update > 200:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 2
        self.set_rect()
        if self.rect.y <= self.max_y:
            self.move_update = self.current_update
            self.vy = 0
            self.state = c.RESTING

    def moveDown(self):
        if self.current_update - self.last_update > 200:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 2

        self.set_rect()

        if self.rect.y >= self.min_y:
            self.move_update = self.current_update
            self.vy = 0
            self.state = c.RESTING

    def rest(self):
        if self.current_update - self.last_update > 200:
            self.last_update = self.current_update
            self.frame_index = (self.frame_index + 1) % 2
        self.set_rect()
        if self.current_update - self.move_update > 3000:
            if self.rect.y == self.min_y:
                self.state = c.MOVEUP
                self.vy = -1
            elif self.rect.y == self.max_y:
                self.state = c.MOVEDOWN
                self.vy = 1
    
    def set_rest(self):
        self.state = c.RESTING
        self.move_update = self.current_update
    
    def set_rect(self):
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

    def jumpToDeath(self):
        self.frame_index = 2
        self.vx = 5
        self.vy = -10
        self.death_update = self.current_update
        self.state = c.DEATH
        self.set_rect()
        