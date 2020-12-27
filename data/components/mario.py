import pygame as pg
from .. import constante as c
from .. import sound
from .fireball import * 


class Perso(pg.sprite.Sprite):
    def __init__(self,x,y,group = None,name = None):
        pg.sprite.Sprite.__init__(self)
        self.sprite = pg.image.load("images\sprite_perso.png").convert_alpha()
        self.name = name
        self.load_image()
        self.setup_booleen()
        self.setup_force()
        self.setup_timer()
        self.image = self.frame[0][3]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.height
        self.state = c.WALK
        self.group = group
        
        
    def setup_force(self):
        if self.name == "mario":
            self.input = c.inputMario
        elif self.name == "luigi":
            self.input = c.inputLuigi
        self.ax = c.WALK_ACC
        self.vx = 0
        self.vy = 0
        self.gravity = c.GRAVITY

    def setup_booleen(self):
        self.in_transition = False
        self.allowJump = True
        self.right = True
        self.crouch = False
        self.isBig = False
        self.transform = False
        self.power = False
        self.invincible = False
        self.wasTouched = False
        self.dead = False
        self.inCastle = False
        self.canGoUnder = False
        self.inUnder = False
        self.canGoOverworld = False
        self.test_when_die = True

    def setup_timer(self):
        self.last_update = 0
        self.current_update = 0
        self.transition_timer = 0
        self.invincible_timer = 0
        self.invincible_animation = 0
        self.wasTouched_timer = 0
        self.wasTouched_animation = 0
        self.fireball_timer = 0
        self.flag_timer = 0
        self.death_timer = 0

    def load_image(self):
        self.frame_index = 0
        self.frame_invincible_index = 0
        self.frame_wasTouched = 0

        self.small_right_frame = []
        self.small_left_frame = []

        self.big_right_frame = []
        self.big_left_frame = []

        self.red_small_right_frame = []
        self.red_small_left_frame = []
        self.red_big_right_frame = []
        self.red_big_left_frame = []

        self.inv1_small_right_frame = []
        self.inv1_small_left_frame = []
        self.inv1_big_right_frame = []
        self.inv1_big_left_frame = []

        self.inv2_small_right_frame = []
        self.inv2_small_left_frame = []
        self.inv2_big_right_frame = []
        self.inv2_big_left_frame = []
        
        self.inv3_small_right_frame = []
        self.inv3_small_left_frame = []
        self.inv3_big_right_frame = []
        self.inv3_big_left_frame = []

        self.frame = []
        if self.name == "mario":
            # small right frame 
            self.small_right_frame.append(self.getImage(98,35,13,15)) # small right walk [0]
            self.small_right_frame.append(self.getImage(117,34,11,16)) # small right walk [1]
            self.small_right_frame.append(self.getImage(131,34,15,16))  # small right walk [2]
            self.small_right_frame.append(self.getImage(82,34,12,16)) # small right standing 
            self.small_right_frame.append(self.getImage(165,34,16,16)) # small right jump
            self.small_right_frame.append(self.getImage(149,34,13,16)) # small right turn around
            self.small_right_frame.append(self.getImage(201,34,13,16)) # small right flag [0]
            self.small_right_frame.append(self.getImage(218,35,12,15)) # small right flag [1]
            self.small_right_frame.append(self.getImage(183,34,14,14)) # small death

            # small left frame
            for frame in self.small_right_frame:
                self.small_left_frame.append(pg.transform.flip(frame,True,False))

            # big right frame
            self.big_right_frame.append(self.getImage(97,3,16,30)) # big right walk [0]
            self.big_right_frame.append(self.getImage(115,2,14,31)) # big right walk [1]
            self.big_right_frame.append(self.getImage(131,1,16,32)) # big right walk [2]
            self.big_right_frame.append(self.getImage(80,1,16,32)) # big right standing
            self.big_right_frame.append(self.getImage(165,1,16,32)) # big right jump
            self.big_right_frame.append(self.getImage(148,1,16,32)) # big right turn around
            self.big_right_frame.append(self.getImage(201,3,14,30)) # big right flag [0]
            self.big_right_frame.append(self.getImage(218,3,14,27)) # big right flag [0]
            self.big_right_frame.append(self.getImage(182,11,16,22)) # big crouch
            self.big_right_frame.append(self.getImage(335,9,16,24)) # medium

            # big left frame
            for frame in self.big_right_frame:
                self.big_left_frame.append(pg.transform.flip(frame,True,False))
        elif self.name == "luigi":
            # small right frame
            self.small_right_frame.append(self.getImage(98,100,13,15)) # small right walk [0]
            self.small_right_frame.append(self.getImage(117,99,11,16)) # small right walk [1]
            self.small_right_frame.append(self.getImage(131,99,15,16))  # small right walk [2]
            self.small_right_frame.append(self.getImage(82,99,12,16)) # small right standing 
            self.small_right_frame.append(self.getImage(165,99,16,16)) # small right jump
            self.small_right_frame.append(self.getImage(149,99,13,16)) # small right turn around
            self.small_right_frame.append(self.getImage(201,99,13,16)) # small right flag [0]
            self.small_right_frame.append(self.getImage(218,100,12,15)) # small right flag [1]
            self.small_right_frame.append(self.getImage(183,99,14,14)) # small death

            # small left frame
            for frame in self.small_right_frame:
                self.small_left_frame.append(pg.transform.flip(frame,True,False))

            # big right frame
            self.big_right_frame.append(self.getImage(97,68,16,30)) # big right walk [0]
            self.big_right_frame.append(self.getImage(115,67,14,31)) # big right walk [1]
            self.big_right_frame.append(self.getImage(131,66,16,32)) # big right walk [2]
            self.big_right_frame.append(self.getImage(80,66,16,32)) # big right standing
            self.big_right_frame.append(self.getImage(165,66,16,32)) # big right jump
            self.big_right_frame.append(self.getImage(148,66,16,32)) # big right turn around
            self.big_right_frame.append(self.getImage(201,68,14,30)) # big right flag [0]
            self.big_right_frame.append(self.getImage(218,68,14,27)) # big right flag [0]
            self.big_right_frame.append(self.getImage(182,76,16,22)) # big crouch
            self.big_right_frame.append(self.getImage(335,74,16,24)) # medium

            # big left frame
            for frame in self.big_right_frame:
                self.big_left_frame.append(pg.transform.flip(frame,True,False))


        # big red right frame
        self.red_big_right_frame.append(self.getImage(97,131,16,30)) # red right walk [0]
        self.red_big_right_frame.append(self.getImage(115,130,14,31)) # red right walk [1]
        self.red_big_right_frame.append(self.getImage(131,129,16,32)) # red right walk [2]
        self.red_big_right_frame.append(self.getImage(80,129,16,32)) # red right standing
        self.red_big_right_frame.append(self.getImage(165,129,16,32)) # red right jump
        self.red_big_right_frame.append(self.getImage(148,129,16,32)) # red right turn around
        self.red_big_right_frame.append(self.getImage(201,131,14,30)) # red right flag [0]
        self.red_big_right_frame.append(self.getImage(218,131,14,27)) # red right flag [1]
        self.red_big_right_frame.append(self.getImage(182,139,16,22)) # red crouch

        # big red left frame
        for frame in self.red_big_right_frame:
            self.red_big_left_frame.append(pg.transform.flip(frame,True,False))

        # small red right frame
        self.red_small_right_frame.append(self.getImage(98,163,13,15)) # red small right walk [0]
        self.red_small_right_frame.append(self.getImage(117,162,11,16)) # red small right walk [1]
        self.red_small_right_frame.append(self.getImage(131,162,15,16)) # red small right walk [2]
        self.red_small_right_frame.append(self.getImage(82,162,12,16)) # red small right standing
        self.red_small_right_frame.append(self.getImage(165,162,16,16)) # red small right jump
        self.red_small_right_frame.append(self.getImage(149,162,13,16)) # red small right turn around

        # small red left frame
        for frame in self.red_small_right_frame:
            self.red_small_left_frame.append(pg.transform.flip(frame,True,False))

        # big inv1 right frame
        self.inv1_big_right_frame.append(self.getImage(97,194,16,30)) # inv1 big right walk  [0]
        self.inv1_big_right_frame.append(self.getImage(115,193,14,31)) # inv1 big right walk [1]
        self.inv1_big_right_frame.append(self.getImage(131,192,16,32)) # inv1 big right walk [2]
        self.inv1_big_right_frame.append(self.getImage(80,192,16,32)) # inv1 big right standing
        self.inv1_big_right_frame.append(self.getImage(165,192,16,32)) # inv1 big right jump
        self.inv1_big_right_frame.append(self.getImage(148,192,16,32)) # inv1 big right turn around
        self.inv1_big_right_frame.append(self.getImage(182,202,16,22)) # inv1 big crouch

        # big inv1 left frame
        for frame in self.inv1_big_right_frame:
            self.inv1_big_left_frame.append(pg.transform.flip(frame,True,False))

        # small inv1 right frame
        self.inv1_small_right_frame.append(self.getImage(98,226,13,15)) # inv1 small right walk [0]
        self.inv1_small_right_frame.append(self.getImage(117,225,11,16)) # inv1 small right walk [1]
        self.inv1_small_right_frame.append(self.getImage(132,225,14,16)) # inv1 small right walk [2]
        self.inv1_small_right_frame.append(self.getImage(82,225,12,16)) # inv1 small right standing
        self.inv1_small_right_frame.append(self.getImage(165,225,16,16)) # inv1 small right jump
        self.inv1_small_right_frame.append(self.getImage(149,225,13,16)) # inv1 small right turn around

        # small inv1 left frame
        for frame in self.inv1_small_right_frame:
            self.inv1_small_left_frame.append(pg.transform.flip(frame,True,False))

        # big inv2 right frame
        self.inv2_big_right_frame.append(self.getImage(97,257,16,30)) # inv2 big right walk [0]
        self.inv2_big_right_frame.append(self.getImage(115,256,14,31)) # inv2 big right walk [1]
        self.inv2_big_right_frame.append(self.getImage(131,255,16,32)) # inv2 big right walk [2]
        self.inv2_big_right_frame.append(self.getImage(80,255,16,32)) # inv2 big right standing
        self.inv2_big_right_frame.append(self.getImage(165,255,16,32)) # inv2 big right jump
        self.inv2_big_right_frame.append(self.getImage(148,255,16,32)) # inv2 big right turn around
        self.inv2_big_right_frame.append(self.getImage(182,265,16,22)) # inv2 big crouch

        # big inv2 left frame
        for frame in self.inv2_big_right_frame:
            self.inv2_big_left_frame.append(pg.transform.flip(frame,True,False))

        # small inv2 right frame
        self.inv2_small_right_frame.append(self.getImage(98,289,13,15)) # inv2 small right walk [0]
        self.inv2_small_right_frame.append(self.getImage(117,288,11,16)) # inv2 small right walk [1]
        self.inv2_small_right_frame.append(self.getImage(132,288,14,16)) # inv 2 small right walk [2]
        self.inv2_small_right_frame.append(self.getImage(82,288,12,16)) # inv2 small right standing
        self.inv2_small_right_frame.append(self.getImage(165,288,16,16)) # inv2 small right jump
        self.inv2_small_right_frame.append(self.getImage(149,288,13,16)) # inv2 small right turn around

        # small inv2 left frame
        for frame in self.inv2_small_right_frame:
            self.inv2_small_left_frame.append(pg.transform.flip(frame,True,False))

        # big inv3 right frame
        self.inv3_big_right_frame.append(self.getImage(97,320,16,30)) # inv3 big right walk [0]
        self.inv3_big_right_frame.append(self.getImage(115,319,14,31)) # inv3 big right walk [1]
        self.inv3_big_right_frame.append(self.getImage(131,318,16,32)) # inv3 big right walk [2]
        self.inv3_big_right_frame.append(self.getImage(80,318,16,32)) # inv3 big right standing
        self.inv3_big_right_frame.append(self.getImage(165,318,16,32)) # inv3 big right jump
        self.inv3_big_right_frame.append(self.getImage(148,318,16,32)) # inv3 big right turn aroud
        self.inv3_big_right_frame.append(self.getImage(182,328,16,22)) # inv3 big crouch
        

        # big inv3 left frame
        for frame in self.inv3_big_right_frame:
            self.inv3_big_left_frame.append(pg.transform.flip(frame,True,False))
        
        # small inv2 right frame
        self.inv3_small_right_frame.append(self.getImage(98,352,13,15)) # inv3 small right walk [0]
        self.inv3_small_right_frame.append(self.getImage(117,351,11,16)) # inv3 small right walk [1]
        self.inv3_small_right_frame.append(self.getImage(132,351,14,16)) # inv3 small right walk [2]
        self.inv3_small_right_frame.append(self.getImage(82,351,12,16)) # inv3 small right standing
        self.inv3_small_right_frame.append(self.getImage(165,351,16,16)) # inv3 small right jump
        self.inv3_small_right_frame.append(self.getImage(149,351,13,16)) # inv3 small right turn around

        # small inv3 left frame
        for frame in self.inv3_small_right_frame:
            self.inv3_small_left_frame.append(pg.transform.flip(frame,True,False))

        self.small_frame = [self.small_right_frame,self.small_left_frame]
        self.big_frame = [self.big_right_frame,self.big_left_frame]

        self.red_small_frame = [self.red_small_right_frame,self.red_small_left_frame]
        self.red_big_frame = [self.red_big_right_frame,self.red_big_left_frame]

        self.inv1_small_frame = [self.inv1_small_right_frame,self.inv1_small_left_frame]
        self.inv1_big_frame = [self.inv1_big_right_frame,self.inv1_big_left_frame]

        self.inv2_small_frame = [self.inv2_small_right_frame,self.inv2_small_left_frame]
        self.inv2_big_frame = [self.inv2_big_right_frame,self.inv2_big_left_frame]

        self.inv3_small_frame = [self.inv3_small_right_frame,self.inv3_small_left_frame]
        self.inv3_big_frame = [self.inv3_big_right_frame,self.inv3_big_left_frame]

        self.invincible_big_frame = [self.inv2_big_frame,self.red_big_frame,self.inv3_big_frame,self.inv1_big_frame]
        self.invincible_small_frame = [self.inv2_small_frame,self.red_small_frame,self.inv3_small_frame,self.inv1_small_frame]
        
        self.frame = self.small_frame

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((0,0,0))
        image = pg.transform.scale(image,(int(w* c.SIZE_MULTIPLIER),int(h* c.SIZE_MULTIPLIER)))
        return image

    def handleState(self,keys):
        if self.state == c.STAND:
            self.standing(keys)
        elif self.state == c.WALK:
            self.walking(keys)
        elif self.state == c.JUMP:
            self.jump(keys)
        elif self.state == c.FALL:
            self.falling(keys)
        elif self.state == c.TOBIG:
            self.transitionToBig()
        elif self.state == c.TOSMALL:
            self.transitionToSmall()
        elif self.state == c.TORED:
            self.transitionToRed()
        elif self.state == c.JUMPTODEATH:
            self.jumpToDeath()
        elif self.state == c.SLIDEFLAG:
            self.slideFlag()
        elif self.state == c.WAITFLAG:
            self.waitFlag()
        elif self.state == c.WALKTOCASTLE:
            self.walkToCastle()
    
    def slideFlag(self):
        self.vx = 0
        self.vy = 4

        if self.rect.bottom >= 492:
            self.vy = 0
            self.right = False
            self.rect.x = self.rect.right + 5
            self.state = c.WAITFLAG
        else:
            if self.current_update - self.last_update > 100 :
                self.last_update = self.current_update
                self.frame_index = 6 + (self.frame_index + 1) % 2

    def waitFlag(self):
        if self.flag_timer == 0:
            self.flag_timer = self.current_update
            sound.end.play()
        elif self.current_update - self.flag_timer > 700:
            self.vy += self.gravity
            self.vx = 2
            self.right = True
            self.state = c.WALKTOCASTLE
        
    def walkToCastle(self):
        self.vy += self.gravity
        if self.current_update - self.last_update > 130:
            self.last_update = self.current_update 
            self.frame_index = (self.frame_index + 1) % 3
        if self.rect.x > 3265 * c.BACKGROUND_SIZE_MULTIPLIER:
            self.vx = 0
            self.inCastle = True
            

    def jumpToDeath(self):
        self.dead = True
        self.frame_index = 8
        self.vx = 0
        if self.vy < c.MAX_VEL_Y:
            self.vy += self.gravity
    

    def falling(self,keys):
        if self.vy < c.MAX_VEL_Y:
            self.vy += self.gravity

        if keys[self.input["action"]]:
            self.check_if_fireball()

        if keys[self.input["gauche"]]:
            if self.vx > (c.MAX_WALK_SPEED * -1):
                self.vx += -self.ax
        elif keys[self.input["droite"]]:
             if self.vx < c.MAX_WALK_SPEED:
                self.vx += self.ax

    def jump(self,keys):
        self.allowJump = False
        self.gravity = c.JUMP_GRAVITY
        self.vy += self.gravity
        
        self.frame_index = 4

        if self.vy >= 0:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if keys[self.input["action"]]:
            self.check_if_fireball()

        if keys[self.input["gauche"]]:
            if self.vx > (c.MAX_WALK_SPEED * -1):
                self.vx += -self.ax
        elif keys[self.input["droite"]]:
             if self.vx < c.MAX_WALK_SPEED:
                self.vx += self.ax

        if not keys[self.input["saut"]]:
            self.gravity = c.GRAVITY
            self.state = c.FALL

    def check_if_fireball(self):
        if self.power and self.current_update - self.fireball_timer > 200:
            self.fireball_timer = self.current_update
            self.castFireball()

    def check_if_can_jump(self,keys):
        if not keys[self.input["saut"]]:
            self.allowJump = True

    def standing(self,keys):
        self.check_if_can_jump(keys)
        #self.vy = 0
        self.vx = 0
        self.frame_index = 3

        if keys[self.input["action"]]:
            self.check_if_fireball()

        if keys[self.input["gauche"]]:
            self.state = c.WALK
        elif keys[self.input["droite"]]:
            self.state = c.WALK
        elif keys[self.input["saut"]]:
            if  self.allowJump:
                if self.isBig:
                    sound.big_jump.play()
                else:
                    sound.small_jump.play()
                self.state = c.JUMP
                self.vy = c.JUMP_VEL
        elif keys[self.input["bas"]]:
            self.crouch = True
            if self.canGoUnder:
                self.inUnder = True
               

        if not keys[self.input["bas"]]:
            self.crouch = False

    def calculate_speed_animation(self):
        speed = 150
        animation = speed - (abs(self.vx) * 13)
        return animation

    def walking(self,keys):
        self.check_if_can_jump(keys)
        if self.canGoOverworld:
            self.inUnder = False
            
        if self.current_update - self.last_update > self.calculate_speed_animation():
            self.last_update = self.current_update 
            self.frame_index = (self.frame_index + 1) % 3
        
        if keys[self.input["action"]]:
            self.check_if_fireball()

        if keys[self.input["saut"]]:
            if self.allowJump:
                if self.isBig:
                    sound.big_jump.play()
                else:
                    sound.small_jump.play()
                self.state = c.JUMP
                self.vy = c.JUMP_VEL

        if keys[self.input["gauche"]]:
            self.outOfCrouch()
            self.right = False
            if self.vx <= 0:
                self.ax = c.WALK_ACC
            else:
                self.frame_index = 5
                self.ax = c.TURN_AROUD

            if self.vx > (c.MAX_WALK_SPEED * -1):
                self.vx += -self.ax

        elif keys[self.input["droite"]]:
            self.outOfCrouch()
            self.right = True
            if self.vx >= 0:
                self.ax = c.WALK_ACC
            else:
                self.frame_index = 5
                self.ax = c.TURN_AROUD

            if self.vx < c.MAX_WALK_SPEED:
                self.vx += self.ax
        else:
            if self.right:
                if self.vx > 0:
                    self.vx -= (self.ax * 2)
                else:
                    self.vx = 0
                    self.state = c.STAND
            else:
                if self.vx <= 0:
                    self.vx += (self.ax * 2)
                else:
                    self.vx = 0
                    self.state = c.STAND

    def castFireball(self):
        if len(self.group) < 6:
            sound.fireball.play()
            if self.right:
                self.group.add(FireBall(self.rect.x + self.rect.width,self.rect.centery,1))
            else:
                self.group.add(FireBall(self.rect.x,self.rect.centery,-1))

    def transitionToBig(self):
        self.vy = 0
        self.vx = 0
        self.transform = True
        if self.transition_timer == 0:
            self.transition_timer = self.current_update

        elif self.time_between_2_date(150,200):
            self.setToMedium()
        elif self.time_between_2_date(200,250):
            self.setToSmall()

        elif self.time_between_2_date(250,300):
            self.setToMedium()

        elif self.time_between_2_date(300,350):
            self.setToSmall()

        elif self.time_between_2_date(350,400):
            self.setToMedium()

        elif self.time_between_2_date(400,450):
            self.setToBig()

        elif self.time_between_2_date(450,500):
            self.setToSmall()

        elif self.time_between_2_date(500,550):
            self.setToMedium()

        elif self.time_between_2_date(550,600):
            self.setToSmall()
        elif self.time_between_2_date(600,650):
            self.setToBig()
            self.setBigImg()
            self.transform = False
            self.transition_timer = 0
            self.state = c.WALK


    def transitionToSmall(self):
        self.vy = 0
        self.vx = 0
        self.transform = True

        if self.transition_timer == 0:
            self.transition_timer = self.current_update

        elif self.time_between_2_date(150,200):
            self.setToSmall()
        elif self.time_between_2_date(200,250):
            self.setToBig()

        elif self.time_between_2_date(250,300):
            self.setToSmall()

        elif self.time_between_2_date(300,350):
            self.setToBig()

        elif self.time_between_2_date(350,400):
            self.setToSmall()

        elif self.time_between_2_date(400,450):
            self.setToBig()

        elif self.time_between_2_date(450,500):
            self.setToSmall()

        elif self.time_between_2_date(500,550):
            self.setToBig()

        elif self.time_between_2_date(550,600):
            self.setToSmall()

        elif self.time_between_2_date(600,650):
            self.setToBig()

        elif self.time_between_2_date(650,700):
            self.setToSmall()
            self.setSmallImg()
            self.transform = False
            self.transition_timer = 0
            self.state = c.WALK
            


    def transitionToRed(self):
        self.vy = 0
        self.vx = 0
        self.transform = True
        if self.transition_timer == 0:
            self.transition_timer = self.current_update

        elif self.time_between_2_date(50,90):
            self.setToRed()
        elif self.time_between_2_date(90,140):
            self.setToInv2()
        elif self.time_between_2_date(140,180):
            self.setToRed()
        elif self.time_between_2_date(180,220):
            self.setToInv3()
        elif self.time_between_2_date(220,260):
            self.setToInv1()
        elif self.time_between_2_date(260,300):
            self.setToInv2()
        elif self.time_between_2_date(300,340): # long
            self.setToRed()
        elif self.time_between_2_date(420,460):
            self.setToInv3()
        elif self.time_between_2_date(460,500):
            self.setToInv1()
        elif self.time_between_2_date(500,540):
            self.setToInv2()
        elif self.time_between_2_date(540,580):
            self.setToRed()
        elif self.time_between_2_date(580,620):
            self.setToInv3()
        elif self.time_between_2_date(620,660):
            self.setToInv1()
        elif self.time_between_2_date(660,700):
            self.setToRed()
            self.setRedImg()
            self.transform = False
            self.transition_timer = 0
            self.state = c.WALK
           


    def time_between_2_date(self,t1,t2):
        if (self.current_update - self.transition_timer) >= t1 and (self.current_update - self.transition_timer) < t2:
            return True
        

    def outOfCrouch(self):
        self.crouch = False
        if self.right:
            self.image = self.frame[0][3]
        else:
            self.image = self.frame[1][3]
        self.set_rect()

    def setInv1Img(self):
        if self.isBig:
            self.frame = self.inv1_big_frame
        else:
            self.frame = self.inv1_small_frame
        self.set_rect()
    
    def setInv2Img(self):
        if self.isBig:
            self.frame = self.inv2_big_frame
        else:
            self.frame = self.inv2_small_frame
        self.set_rect()
    
    def setInv3Img(self):
        if self.isBig:
            self.frame = self.inv3_big_frame
        else:
            self.frame = self.inv3_small_frame
        self.set_rect()

    def setRedImg(self):
        if self.isBig:
            self.frame = self.red_big_frame
        else:
            self.frame = self.red_small_frame
        self.set_rect()
        self.power = True

    def setBigImg(self):
        self.frame = self.big_frame
        self.set_rect()
        self.isBig = True

    def setSmallImg(self):
        self.frame = self.small_frame
        self.set_rect()
        self.isBig = False
        self.power = False

    def setToSmall(self):
        if self.right:
            self.image = self.small_right_frame[3]
        else:
            self.image = self.small_left_frame[3]
        self.set_rect()

    def setToMedium(self):
        if self.right:
            self.image = self.big_right_frame[9]
        else:
            self.image = self.big_left_frame[9]
        self.set_rect()

    def setToBig(self):
        if self.right:
            self.image = self.big_right_frame[3]
        else:
            self.image = self.big_left_frame[3]
        self.set_rect()
    
    def setToRed(self):
        if self.right:
            self.image = self.red_big_right_frame[self.frame_index]
        else:
            self.image = self.red_big_left_frame[self.frame_index]
        self.set_rect()
    
    def setToInv1(self):
        if self.right:
            self.image = self.inv1_big_right_frame[self.frame_index]
        else:
            self.image = self.inv1_big_left_frame[self.frame_index]
        self.set_rect()
    
    def setToInv2(self):
        if self.right:
            self.image = self.inv2_big_right_frame[self.frame_index]
        else:
            self.image = self.inv2_big_left_frame[self.frame_index]
        self.set_rect()
    
    def setToInv3(self):
        if self.right:
            self.image = self.inv3_big_right_frame[self.frame_index]
        else:
            self.image = self.inv3_big_left_frame[self.frame_index]
        self.set_rect()

    def animation(self):
        if self.state == c.TOSMALL or self.state == c.TOBIG or self.state == c.TORED: 
            pass
        else:
            if self.right:
                self.image = self.frame[0][self.frame_index]
            else:
                self.image = self.frame[1][self.frame_index]

            if self.frame_wasTouched == 0 and self.wasTouched:
                s = pg.Surface((self.rect.width,self.rect.height), pg.SRCALPHA, 32)
                self.image = s  
                    
            self.set_rect()

    def set_rect(self):
        left = self.rect.left
        bottom = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

    def check_if_crouching(self):
        if self.crouch and self.isBig:
            self.frame_index = 8
        
    def check_if_invincible(self):
        if self.invincible:
            if self.current_update - self.invincible_timer > 10000:
                sound.star.stop()
                sound.main.play(-1)
                self.invincible = False
                if self.power:
                    self.frame = self.red_big_frame
                elif self.isBig:
                    self.frame = self.big_frame
                else:
                    self.frame = self.small_frame

        
            if self.current_update - self.invincible_animation > 85:
                self.invincible_animation = self.current_update
                self.frame_invincible_index = (self.frame_invincible_index + 1) % 4
                
                if self.isBig:
                    self.frame = self.invincible_big_frame[self.frame_invincible_index]
                else:
                    self.frame = self.invincible_small_frame[self.frame_invincible_index]

                
    def setInvincible(self):
        self.invincible = True
        self.invincible_timer = self.current_update

    def setWasTouched(self):
        self.wasTouched = True
        self.wasTouched_timer = self.current_update

    def check_if_wasTouched(self):
        if self.current_update - self.wasTouched_timer > 2700:
            self.wasTouched = False
        
        if self.wasTouched:
            if self.current_update - self.wasTouched_animation > 100:
                self.wasTouched_animation = self.current_update
                self.frame_wasTouched = (self.frame_wasTouched + 1) % 2
                

    def update(self,keys):
        self.current_update = pg.time.get_ticks()
        self.handleState(keys)
        self.check_if_crouching()
        self.check_if_invincible()
        self.check_if_wasTouched()
        self.animation()

class Mario(Perso):
    def __init__(self,x,y,group =None,name = "mario"):
        Perso.__init__(self,x,y,group,name)
        

class Luigi(Perso):
    def __init__(self,x,y,group =None,name = "luigi"):
        Perso.__init__(self,x,y,group,name)
    
    
        
        
        

        
    

