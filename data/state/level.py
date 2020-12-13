import pygame as pg
from pygame.locals import *
from .. import sound
from .. components import info
from .. components.mario import *
from .. import constante as c
from .. components.collider import *
from .. components.brick import *
from .. components.coin_brick import *
from .. components.power import *
from .. components.ennemy import *
from .. components.checkpoint import *
from . import state

class Level(state.State):
    def __init__(self):
        state.State.__init__(self)
        
    def startup(self,current_time):
        self.next = None
        self.state = c.NOTFREEZE
        self.timeOut = False
        self.current_update = current_time
        self.timeOut_timer = 0
        self.timeEnd_timer = 0
        self.setup_everything()
        self.info = info.Info(c.LEVEL)

    def setup_background(self):
        self.background = pg.image.load("images/fond_0.png")
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,(int(self.back_rect.width * c.BACKGROUND_SIZE_MULTIPLIER),int(self.back_rect.height * c.BACKGROUND_SIZE_MULTIPLIER)))
        self.back_rect = self.background.get_rect()
        self.back_rect.x = 0
        self.back_rect.y = 0
        
    def setup_mario(self):
        self.fireball = pg.sprite.Group()
        self.mario = Mario(50,c.GROUND_HEIGHT,self.fireball)
        self.mario_death_timer = 0

    def setup_ground(self):
        ground_1 = Collider(0,c.GROUND_HEIGHT,1104,24)
        ground_2 = Collider(1136,c.GROUND_HEIGHT,240,24)
        ground_3 = Collider(1424,c.GROUND_HEIGHT,1024,24)
        ground_4 = Collider(2480,c.GROUND_HEIGHT,912,24)
        self.ground = pg.sprite.Group(ground_1,ground_2,ground_3,ground_4)

    def setup_pipe(self):
        pipe_1 = Collider(449,452,30,31)
        pipe_2 = Collider(609,153 * c.BACKGROUND_SIZE_MULTIPLIER,30,47)
        pipe_3 = Collider(737,137 * c.BACKGROUND_SIZE_MULTIPLIER,30,63)
        pipe_4 = Collider(913,137 * c.BACKGROUND_SIZE_MULTIPLIER,30,63)
        pipe_5 = Collider(2609,169 * c.BACKGROUND_SIZE_MULTIPLIER,30,31)
        pipe_6 = Collider(2865,169 * c.BACKGROUND_SIZE_MULTIPLIER,30,31)

        self.pipe = pg.sprite.Group(pipe_1,pipe_2,pipe_3,pipe_4,pipe_5,pipe_6)

    def setup_stair(self):
        stair_1 = Collider(2144,184 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_2 = Collider(2160,168 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_3 = Collider(2176,152 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_4 = Collider(2192,136 * c.BACKGROUND_SIZE_MULTIPLIER,16,64)

        stair_5 = Collider(2240,136 * c.BACKGROUND_SIZE_MULTIPLIER,16,64)
        stair_6 = Collider(2256,152 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_7 = Collider(2272,168 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_8 = Collider(2288,184 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)

        stair_9 = Collider(2368,184 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_10 = Collider(2384,168 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_11 = Collider(2400,152 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_12 = Collider(2416,136 * c.BACKGROUND_SIZE_MULTIPLIER,32,64)
        
        stair_13 = Collider(2480,136 * c.BACKGROUND_SIZE_MULTIPLIER,16,64)
        stair_14 = Collider(2496,152 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_15 = Collider(2512,168 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_16 = Collider(2528,184 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)

        stair_17 = Collider(2896,184 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_18 = Collider(2912,168 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_19 = Collider(2928,152 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_20 = Collider(2944,136 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_21 = Collider(2960,120 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_22 = Collider(2979,104 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_23 = Collider(2992,88 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)
        stair_24 = Collider(3008,72 * c.BACKGROUND_SIZE_MULTIPLIER,32,128)

        bottom_flag = Collider(3168,184 * c.BACKGROUND_SIZE_MULTIPLIER,16,16)

        self.stair = pg.sprite.Group(stair_1,stair_2,stair_3,stair_4,
                                     stair_5,stair_6,stair_7,stair_8,
                                     stair_9,stair_10,stair_11,stair_12,
                                     stair_13,stair_14,stair_15,stair_16,
                                     stair_17,stair_18,stair_19,stair_20,stair_21,stair_22,stair_23,stair_24,bottom_flag)

    def setup_brick(self):
        self.brick_piece = pg.sprite.Group()
        self.coin = pg.sprite.Group()
        self.score = []
        self.score_timer = []

        brick_1 = Brick(320,136)
        brick_2 = Brick(352,136)
        brick_3 = Brick(384,136)
        brick_4 = Brick(1232,136)
        brick_5 = Brick(1264,136)
        brick_6 = Brick(1280,72)
        brick_7 = Brick(1296,72)
        brick_8 = Brick(1312,72)
        brick_9 = Brick(1328,72)
        brick_10 = Brick(1344,72)
        brick_11 = Brick(1360,72)
        brick_12 = Brick(1376,72)
        brick_13 = Brick(1392,72)
        brick_14 = Brick(1456,72)
        brick_15 = Brick(1472,72)
        brick_16 = Brick(1488,72)
        brick_17 = Brick(1504,136,self.coin,"coin")  # coin
        brick_18 = Brick(1600,136)
        brick_19 = Brick(1616,136,self.power,"star") # star
        brick_20 = Brick(1888,136)
        brick_21 = Brick(1936,72)
        brick_22 = Brick(1952,72)
        brick_23 = Brick(1968,72)
        brick_24 = Brick(2048,72)
        brick_25 = Brick(2096,72)
        brick_26 = Brick(2064,136)
        brick_27 = Brick(2080,136)
        brick_28 = Brick(2688,136)
        brick_29 = Brick(2704,136)
        brick_30 = Brick(2736,136)

        self.brick = pg.sprite.Group(brick_1,brick_2,brick_3,brick_4,brick_5,brick_6,brick_7,brick_8,brick_9,
                                        brick_10,brick_11,brick_12,brick_13,brick_14,brick_15,brick_16,brick_17,
                                        brick_18,brick_19,brick_20,brick_21,brick_22,brick_23,brick_24,brick_25,brick_26,
                                        brick_27,brick_28,brick_29,brick_30)    
        

    def setup_coin_brick(self):
        coin_brick_1 = Coin_Brick(256,136,self.coin,"coin")
        coin_brick_2 = Coin_Brick(336,136,self.power,"mush")
        coin_brick_3 = Coin_Brick(368,136,self.coin,"coin")
        coin_brick_4 = Coin_Brick(352,72,self.coin,"coin")
        coin_brick_5 = Coin_Brick(1248,136,self.power,"mush")
        coin_brick_6 = Coin_Brick(1504,72,self.coin,"coin")
        coin_brick_7 = Coin_Brick(1696,136,self.coin,"coin")
        coin_brick_8 = Coin_Brick(1744,136,self.coin,"coin")
        coin_brick_9 = Coin_Brick(1792,136,self.coin,"coin")
        coin_brick_10 = Coin_Brick(1744,72,self.coin,"coin")
        coin_brick_12 = Coin_Brick(2064,72,self.coin,"coin")
        coin_brick_13 = Coin_Brick(2080,72,self.coin,"coin")
        coin_brick_14 = Coin_Brick(2720,136,self.coin,"coin")

        self.coin_brick = pg.sprite.Group(coin_brick_1,coin_brick_2,coin_brick_3,coin_brick_4,coin_brick_5,coin_brick_6,
                                            coin_brick_7,coin_brick_8,coin_brick_9,coin_brick_10,coin_brick_12,
                                            coin_brick_13,coin_brick_14)

    def setup_power(self):
        self.power = pg.sprite.Group()

    def setup_ennemy(self):
        e1 = Gumba(352,184, -1)

        e2 = Gumba(642,184, 1)
        self.ennemy_g1 = pg.sprite.Group(e2)

        e3 = Gumba(820,184,-1)
        e4 = Gumba(845,184,-1)
        self.ennemy_g2 = pg.sprite.Group(e3,e4)

        e5 = Gumba(1300,55,-1)
        e6 = Gumba(1325,55,-1)
        self.ennemy_g3 = pg.sprite.Group(e5,e6)

        e7 = Gumba(1562,184,-1)
        e8 = Gumba(1587,184,-1)
        self.ennemy_g4 = pg.sprite.Group(e7,e8)

        e9 = Koopa(1715,176,-1)
        e10 = Gumba(1830,184,-1)
        e11 = Gumba(1855,184,-1)
        self.ennemy_g5 = pg.sprite.Group(e9,e10,e11)

        e12 = Gumba(1985,184,-1)
        e13 = Gumba(2010,184,-1)
        e14 = Gumba(2050,184,-1)
        e15 = Gumba(2075,184,-1)
        self.ennemy_g6 = pg.sprite.Group(e12,e13,e14,e15)

        e16 = Gumba(2780,184,-1)
        e17 = Gumba(2805,184,-1)
        self.ennemy_g7 = pg.sprite.Group(e16,e17)

        
        self.ennemy = pg.sprite.Group(e1)
        self.ennemy_death = pg.sprite.Group()

        self.all_ennemy = pg.sprite.Group(self.ennemy,self.ennemy_death,self.ennemy_g1,self.ennemy_g2,self.ennemy_g3,self.ennemy_g4,self.ennemy_g5,self.ennemy_g6,self.ennemy_g7)

    def setup_checkpoint(self):
        check1 = checkPoint(470,0,"1")
        check2 = checkPoint(600,0,"2")
        check3 = checkPoint(1100,0,"3")
        check4 = checkPoint(1400,0,"4")
        check5 = checkPoint(1530,0,"5")
        check6 = checkPoint(1830,0,"6")
        check7 = checkPoint(2630,0,"7")
        check8 = checkPoint(3178,32,"8")
        self.checkpoint = pg.sprite.Group(check1,check2,check3,check4,check5,check6,check7,check8)
        self.flag = Flag(3175,40)
        self.flagEnd = FlagEnd(3265,140)
        

    def setup_everything(self):
        self.setup_background()
        self.setup_mario()
        self.setup_ground()
        self.setup_pipe()
        self.setup_stair()
        self.setup_power()
        self.setup_brick()
        self.setup_coin_brick()
        self.setup_ennemy()
        self.setup_checkpoint()

        self.ground_pipe_stair = pg.sprite.Group(self.ground,self.pipe,self.stair)

    def update(self,keys,screen,current_time):
        self.current_update = current_time
        self.handleState(keys)
        self.draw_everything(screen)

    def handleState(self,keys):
        if self.state == c.NOTFREEZE:
            self.update_all_sprites(keys)
        elif self.state == c.FREEZE:
            self.update_while_transition(keys)
        elif self.state == c.INCASTLE:
            self.update_while_castle(keys)
    
    def update_while_castle(self,keys):
        self.info.end_score()
        self.info.update(self.current_update,self.mario.state)
        self.coin_brick.update()
        self.flagEnd.update()
        if int(info.game_info["time"]) == 0 and self.flagEnd.rect.bottom > (121*c.BACKGROUND_SIZE_MULTIPLIER):
            self.flagEnd.state = c.SLIDEFLAG
        
        if self.flagEnd.rect.bottom <= 121 *c.BACKGROUND_SIZE_MULTIPLIER:
            if self.timeEnd_timer == 0:
                self.timeEnd_timer = self.current_update
            elif self.current_update - self.timeEnd_timer > 3000:
                self.done = True
                self.next = c.MAIN_MENU
        
        
    def update_while_transition(self,keys):
        self.mario.update(keys)
        self.coin_brick.update()
        self.info.update(self.current_update,self.mario.state)
        self.check_if_mario_in_transition()
        self.check_if_change_state()
        self.check_if_timeout()


    def update_all_sprites(self,keys):
        self.mario.update(keys)
        self.ground.update()
        self.brick.update()
        self.brick_piece.update()
        self.coin_brick.update()
        self.coin.update()
        self.power.update()
        self.ennemy.update()
        self.ennemy_death.update()
        self.fireball.update()
        self.checkpoint.update()
        self.flag.update()
        self.update_score()
        self.adjust_position_mario()
        self.adjust_position_power()
        self.adjust_position_ennemy()
        self.adjust_position_fireball()
        self.info.update(self.current_update,self.mario.state)
        if abs(self.back_rect.x) < self.back_rect.width - 805:
            self.update_background()
        self.check_if_mario_in_transition()
        self.check_if_change_state()
        self.check_if_timeout()

    def check_if_timeout(self):
        if int(info.game_info["time"]) == 99 and not self.timeOut:
            sound.main.stop()
            sound.time.play()
            self.timeOut = True
        
        if self.timeOut:
            if self.timeOut_timer == 0:
                self.timeOut_timer = self.current_update
            elif (self.current_update - self.timeOut_timer) > 3000:
                self.timeOut = False
                sound.main.play()
        
        if int(info.game_info["time"]) == 0 and not self.mario.dead:
            self.mario.vy = - 8
            self.mario.state = c.JUMPTODEATH
            sound.main.stop()


    def check_if_change_state(self):
        if self.mario.rect.y > c.HEIGHT:
            self.mario.dead = True
            sound.main.stop()

        if self.mario.dead:
            self.play_die_song()

    def play_die_song(self):
        if self.mario_death_timer == 0:
            sound.die.play()
            self.mario_death_timer = self.current_update
        elif (self.current_update - self.mario_death_timer) > 3000:
            self.done = True
            self.set_game_info()

    def set_game_info(self):
        if int(info.game_info["time"]) == 0:
            self.next = c.TIMEOUT
            info.game_info["lives"] -= 1

        elif self.mario.dead:
            info.game_info["lives"] -= 1
            self.next = c.LOAD
        
        if info.game_info["lives"] == 0:
            self.next = c.GAMEOVER
            
    def check_if_mario_in_transition(self):
        if self.mario.state == c.TOBIG or self.mario.state == c.TORED or self.mario.state == c.TOSMALL:
            self.state = c.FREEZE
        elif self.mario.inCastle:
            sound.count_time.play()
            self.state = c.INCASTLE
        else:
            self.state = c.NOTFREEZE

    def draw_everything(self,screen):
        screen.blit(self.background,(self.back_rect.x,self.back_rect.y))
        screen.blit(self.flag.image,self.flag.rect)
        if not self.mario.inCastle:
            screen.blit(self.mario.image,(self.mario.rect.x,self.mario.rect.y))
        if self.flagEnd.rect.top < 121*c.BACKGROUND_SIZE_MULTIPLIER:
            screen.blit(self.flagEnd.image,self.flagEnd.rect)
        self.ground.draw(screen)
        self.power.draw(screen)
        self.brick.draw(screen)
        self.ennemy.draw(screen)
        self.ennemy_death.draw(screen)
        self.coin_brick.draw(screen)
        self.fireball.draw(screen)
        self.checkpoint.draw(screen)
        self.coin.draw(screen)
        self.draw_score(screen)
        self.brick_piece.draw(screen)
        self.info.draw(screen)

        
    def test_score(self,string,x,y):
        score = self.info.create_score(string,x,y)
        timer = self.current_update
        self.score.append(score)
        self.score_timer.append(timer)
    
    def draw_score(self,screen):
        for line in self.score:
            for char in line:
                screen.blit(char.image,char.rect)

    def update_score(self):
        for i,line in enumerate(self.score_timer):
            if self.current_update - line > 1000:
                self.score.pop(i)
                self.score_timer.pop(i)
        
        for line in self.score:
            for char in line:
                char.rect.y -= 1

        
    def update_background(self):
        # Scroll Background si mario dépasse la moitié de l'écran
        if self.mario.rect.x > c.WIDTH / 2 and self.mario.vx > 0: 
            self.mario.rect.x -= round(self.mario.vx)
            self.back_rect.x -= round(self.mario.vx)
            all_sprite = pg.sprite.Group(self.ground_pipe_stair,self.brick,self.brick_piece,self.coin_brick,self.power,self.coin,self.all_ennemy,self.fireball,self.checkpoint,self.flag,self.flagEnd)
            for i in all_sprite:
                i.rect.x -= round(self.mario.vx)
            for line in self.score:
                for char in line:
                    char.rect.x -= round(self.mario.vx /2)

        # Commence le scrolle du backround
        elif self.mario.rect.x > 250 and self.mario.vx > 0:
            self.mario.rect.x -= round(self.mario.vx / 2)
            self.back_rect.x -= round(self.mario.vx / 2)
            all_sprite = pg.sprite.Group(self.ground_pipe_stair,self.brick,self.brick_piece,self.coin_brick,self.power,self.coin,self.all_ennemy,self.fireball,self.checkpoint,self.flag,self.flagEnd)
            for i in all_sprite:
                i.rect.x -= round(self.mario.vx / 2)
            for line in self.score:
                for char in line:
                    char.rect.x -= round(self.mario.vx /2)

    def change_mush_into_flower(self):
        for b in self.brick:
            if b.content == "mush":
                b.content = "flower"
        for b in self.coin_brick:
            if b.content == "mush":
                b.content = "flower"
    
    def change_flower_into_mush(self):
        for b in self.brick:
            if b.content == "flower":
                b.content = "mush"
        for b in self.coin_brick:
            if b.content == "flower":
                b.content = "mush"

    def adjust_position_mario(self):
        self.mario.rect.x += round(self.mario.vx)
        if not self.mario.state == c.JUMPTODEATH:
            self.check_mario_x_collision()

        self.mario.rect.y += round(self.mario.vy)
        if not self.mario.state == c.JUMPTODEATH:
            self.check_mario_y_collision()


  ######### MARIO COLLISION #########

    def check_mario_x_collision(self):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(self.mario,self.ground_pipe_stair)
        hit_block = pg.sprite.spritecollideany(self.mario,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(self.mario,self.coin_brick)
        hit_power = pg.sprite.spritecollideany(self.mario,self.power)



        hit_ennemy = pg.sprite.spritecollideany(self.mario,self.ennemy)

        hit_checkpoint = pg.sprite.spritecollideany(self.mario,self.checkpoint)
        
        if hit_ground_pipe_stair:
            self.adjust_position_x(hit_ground_pipe_stair)
        elif hit_block:
            self.adjust_position_x(hit_block)
        elif hit_coin_brick:
            self.adjust_position_x(hit_coin_brick)
        elif hit_power:
            self.adjust_collision_power(hit_power)
        elif hit_ennemy and not self.mario.wasTouched and not self.mario.state == c.JUMPTODEATH:
            self.adjust_collision_ennemy_x(hit_ennemy)
        elif hit_checkpoint:
            self.adjust_collision_checkpoint(hit_checkpoint)

        if self.mario.rect.x < 0:
            self.mario.rect.x = 0
        elif self.mario.rect.right > c.WIDTH:
            self.mario.rect.right = c.WIDTH
        


    def adjust_collision_checkpoint(self,checkpoint):
        if checkpoint.name == "1":
            self.ennemy.add(self.ennemy_g1)
            checkpoint.kill()
        elif checkpoint.name == "2":
            self.ennemy.add(self.ennemy_g2)
            checkpoint.kill()
        elif checkpoint.name == "3":
            self.ennemy.add(self.ennemy_g3)
            checkpoint.kill()
        elif checkpoint.name == "4":
            self.ennemy.add(self.ennemy_g4)
            checkpoint.kill()
        elif checkpoint.name == "5":
            self.ennemy.add(self.ennemy_g5)
            checkpoint.kill()
        elif checkpoint.name == "6":
            self.ennemy.add(self.ennemy_g6)
            checkpoint.kill()
        elif checkpoint.name == "7":
            self.ennemy.add(self.ennemy_g7)
            checkpoint.kill()
        elif checkpoint.name == "8":
            sound.main.stop()
            sound.flag.play()
            self.mario.state = c.SLIDEFLAG
            self.flag.state = c.SLIDEFLAG
            print(self.mario.rect.centery)
            if self.mario.rect.centery < 125:
                print("1up")
                info.game_info["lives"] += 1
                sound.up.play()

            elif self.mario.rect.centery > 125 and self.mario.rect.centery < 168:
                print("5000")
                info.game_info["scores"] += 5000
                self.test_score("5000",self.mario.rect.x+30,self.mario.rect.y )

            elif self.mario.rect.centery > 168 and self.mario.rect.centery < 302:
                print("2000")
                info.game_info["scores"] += 2000
                self.test_score("2000",self.mario.rect.x+30,self.mario.rect.y)

            elif self.mario.rect.centery > 302 and self.mario.rect.centery < 375:
                print("800")
                info.game_info["scores"] += 800
                self.test_score("800",self.mario.rect.x+30,self.mario.rect.y)

            elif self.mario.rect.centery > 375 and self.mario.rect.centery < 455:
                print("400")
                info.game_info["scores"] += 400
                self.test_score("400",self.mario.rect.x+30,self.mario.rect.y)

            elif self.mario.rect.centery > 455 and self.mario.rect.centery < 493:
                print("200")
                info.game_info["scores"] += 200
                self.test_score("200",self.mario.rect.x+30,self.mario.rect.y)
            checkpoint.kill()

    def adjust_collision_ennemy_x(self,ennemy):
        if self.mario.rect.right > ennemy.rect.left and self.mario.rect.left < ennemy.rect.left:
            if self.mario.invincible:
                if ennemy.name == "gumba":
                    self.test_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy.name == "koopa":
                    self.test_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.test_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.ennemy_death.add(ennemy)
            elif self.mario.isBig:
                if ennemy.name == "shell" and ennemy.vx == 0:
                    
                    self.mario.rect.right = ennemy.rect.left
                    ennemy.vx = 8
                    self.mario.vx -= 3
                else:
                    print("touche droite")
                    self.mario.state = c.TOSMALL
                    self.change_flower_into_mush()
                    self.mario.setWasTouched()
                    sound.pipe.play()
            else:
                if ennemy.name == "shell" and ennemy.vx == 0:
                    
                    self.mario.rect.right = ennemy.rect.left
                    ennemy.vx = 8
                    self.mario.vx -= 3
                else:
                    self.mario.vy = - 8
                    self.mario.state = c.JUMPTODEATH
                    sound.main.stop()
                    

        elif self.mario.rect.left < ennemy.rect.right and self.mario.rect.right > ennemy.rect.right:
            if self.mario.invincible:
                if ennemy.name == "gumba":
                    self.test_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                    
                elif ennemy.name == "koopa":
                    self.test_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.test_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.ennemy_death.add(ennemy)
            elif self.mario.isBig:
                if ennemy.name == "shell" and ennemy.vx == 0:
                    
                    self.mario.rect.left = ennemy.rect.right
                    ennemy.vx = -8
                    self.mario.vx += 3
                else:
                    print("touche gauche")
                    self.mario.state = c.TOSMALL
                    self.change_flower_into_mush()
                    self.mario.setWasTouched()
                    sound.pipe.play()
            else:
                if ennemy.name == "shell" and ennemy.vx == 0:
                    
                    self.mario.rect.left = ennemy.rect.right
                    ennemy.vx = -8
                    self.mario.vx += 3
                else:
                    self.mario.vy = - 8
                    self.mario.state = c.JUMPTODEATH
                    sound.main.stop()
                    
    
    def adjust_position_x(self,collider):
        if self.mario.rect.right > collider.rect.left and self.mario.rect.left < collider.rect.left:
            self.mario.rect.right = collider.rect.left
            self.mario.vx = 0
        elif self.mario.rect.left < collider.rect.right and self.mario.rect.right > collider.rect.right:
            self.mario.rect.left = collider.rect.right
            self.mario.vx = 0
    
    def adjust_collision_power(self,power):
        info.game_info["scores"] += 1000
        self.test_score("1000",power.rect.x,power.rect.y)
        if power.name == "mush":
            power.kill()
            sound.powerup.play()
            self.mario.state = c.TOBIG
            self.change_mush_into_flower()
        elif power.name == "flower":
            power.kill()
            self.mario.state = c.TORED
            sound.powerup.play()
        elif power.name == "star":
            power.kill()
            sound.main.stop()
            sound.powerup.play()
            sound.star.play()
            self.mario.setInvincible()
            
    def prevent_error_collision(self,block1,block2):
        dist_between_block1_and_mario = abs(block1.rect.centerx - self.mario.rect.centerx)
        dist_between_block2_and_mario = abs(block2.rect.centerx - self.mario.rect.centerx)

        # si mario plus proche du block1 retourne Vrai pour block1 et Faux pour block2
        if dist_between_block1_and_mario < dist_between_block2_and_mario:
            return block1,False
        # inversement
        elif dist_between_block1_and_mario > dist_between_block2_and_mario:
            return False, block2
        # si dist entre mario et les 2 blocs sont égale alors par defaut block1 = Vrai et block2 = Faux
        else:
             return block1,False

    def check_mario_y_collision(self):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(self.mario,self.ground_pipe_stair)

        hit_block = pg.sprite.spritecollideany(self.mario,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(self.mario,self.coin_brick)
        
        hit_ennemy = pg.sprite.spritecollideany(self.mario,self.ennemy)

        if hit_block and hit_coin_brick:
            hit_block,hit_coin_brick = self.prevent_error_collision(hit_block,hit_coin_brick)

        if hit_ground_pipe_stair:
            self.adjust_position_collider(hit_ground_pipe_stair)
        
        elif hit_coin_brick:
            self.adjust_position_coin_brick(hit_coin_brick)
        elif hit_block:
            self.adjust_position_brick(hit_block)
        elif hit_ennemy and not self.mario.wasTouched:
            self.adjust_collision_ennemy_y(hit_ennemy)

        self.check_if_mario_is_falling()

    def adjust_collision_ennemy_y(self,ennemy):
        if self.mario.rect.bottom > ennemy.rect.top and self.mario.rect.top < ennemy.rect.top:
            if self.mario.invincible:
                if ennemy.name == "gumba":
                    self.test_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy.name == "koopa":
                    self.test_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.test_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.ennemy_death.add(ennemy)
            else:
                sound.stomp.play()
                self.mario.vy = -7
                self.mario.rect.bottom = ennemy.rect.top
                if ennemy.name == "gumba":
                    self.ennemy.remove(ennemy)
                    self.test_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                    ennemy.startToDeath()
                    self.ennemy_death.add(ennemy)
                elif ennemy.name == "koopa":
                    self.test_score("200",ennemy.rect.x,ennemy.rect.y)
                    self.ennemy.remove(ennemy)
                    info.game_info["scores"] += 200
                    self.ennemy.add(Shell(ennemy.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(ennemy.rect.y / c.BACKGROUND_SIZE_MULTIPLIER)+9,pg.time.get_ticks(),self.ennemy))
                    ennemy.kill()
                elif ennemy.name == "shell":
                    if ennemy.vx == 0:
                        if self.mario.rect.centerx < (ennemy.rect.centerx - (ennemy.rect.width / 4)):
                            ennemy.vx = 8
                        elif self.mario.rect.centerx > (ennemy.rect.centerx + (ennemy.rect.width / 4)):
                            ennemy.vx = -8
                    else:
                        ennemy.vx = 0
            
        elif self.mario.rect.top < ennemy.rect.bottom and self.mario.rect.bottom > ennemy.rect.bottom:
            if self.mario.invincible:
                if ennemy.name == "gumba":
                    self.test_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy.name == "koopa":
                    self.test_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.test_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.ennemy_death.add(ennemy)
            elif self.mario.isBig:
                print("touche bas")
                self.mario.state = c.TOSMALL
                self.change_flower_into_mush()
                self.mario.setWasTouched()
                sound.pipe.play()
            else:
                self.mario.vy = - 8
                self.mario.state = c.JUMPTODEATH
                sound.main.stop()
            

    def adjust_position_collider(self,collider):
        if self.mario.rect.bottom > collider.rect.top and self.mario.rect.top < collider.rect.top:
            self.mario.vy = 0
            self.mario.rect.bottom = collider.rect.top
            if self.mario.state != c.WALKTOCASTLE and self.mario.state != c.WAITFLAG and self.mario.state != c.SLIDEFLAG:
                self.mario.state = c.WALK
            self.mario.isjump = False

        elif self.mario.rect.top < collider.rect.bottom and self.mario.rect.bottom > collider.rect.bottom:
            self.mario.vy = 3
            self.mario.rect.top = collider.rect.bottom
            self.mario.state = c.FALL

    def adjust_position_brick(self,collider):
        if self.mario.rect.bottom > collider.rect.top and self.mario.rect.top < collider.rect.top:
            self.mario.vy = 0
            self.mario.rect.bottom = collider.rect.top
            self.mario.state = c.WALK
            self.mario.isjump = False

        elif self.mario.rect.top < collider.rect.bottom and self.mario.rect.bottom > collider.rect.bottom:
            if self.mario.isBig:
                if collider.content != "coin" and collider.content != "star" and collider.state != c.OPENED:
                    sound.break_sound.play()
                    info.game_info["scores"] += 50
                    self.check_if_ennemy_on_brick(collider)
                    collider.kill()

                    self.brick_piece.add(BrickPiece(collider.rect.x,collider.rect.y,-5,-12,0))
                    self.brick_piece.add(BrickPiece(collider.rect.right-16,collider.rect.y,5,-12,1))
                    self.brick_piece.add(BrickPiece(collider.rect.x,collider.rect.bottom-16,-5,-8,2))
                    self.brick_piece.add(BrickPiece(collider.rect.right-16,collider.rect.bottom-16,5,-8,3))
                else:
                    sound.bump.play()
                    if collider.state != c.OPENED:
                        collider.startBump()
                        self.check_if_ennemy_on_brick(collider)
                        if collider.content == "coin":
                            info.game_info["coin_count"] += 1
                            self.test_score("200",collider.rect.x,collider.rect.y)
                            info.game_info["scores"] += 200
                            sound.coin.play()
                        elif collider.content == "star":
                            sound.power_appear.play()
            else:
                sound.bump.play()
                if collider.state != c.OPENED:
                    collider.startBump()
                    self.check_if_ennemy_on_brick(collider)
                    if collider.content == "coin":
                        info.game_info["coin_count"] += 1
                        self.test_score("200",collider.rect.x,collider.rect.y)
                        info.game_info["scores"] += 200
                        sound.coin.play()
                    elif collider.content == "star":
                        sound.power_appear.play()
            
            self.mario.vy = 3
            self.mario.rect.top = collider.rect.bottom
            self.mario.state = c.FALL
        
    def adjust_position_coin_brick(self,collider):
        if self.mario.rect.bottom > collider.rect.top and self.mario.rect.top < collider.rect.top:
            self.mario.vy = 0
            self.mario.rect.bottom = collider.rect.top
            self.mario.state = c.WALK
            self.mario.isjump = False

        elif self.mario.rect.top < collider.rect.bottom and self.mario.rect.bottom > collider.rect.bottom:
            if collider.state == c.RESTING:
                if collider.content == "coin":
                    info.game_info["coin_count"] += 1
                    info.game_info["scores"] += 200
                    self.test_score("200",collider.rect.x,collider.rect.y)
                    sound.coin.play()
                else:
                    sound.power_appear.play()
                
            else:
                sound.bump.play()
            if collider.state != c.OPENED:
                collider.startBump()
                self.check_if_ennemy_on_brick(collider)
            self.mario.vy = 5
            self.mario.rect.top = collider.rect.bottom
            self.mario.state = c.FALL
    

    def check_if_ennemy_on_brick(self,brick):
        brick.rect.y -= 1
        hit_ennemy = pg.sprite.spritecollideany(brick,self.ennemy)
        if hit_ennemy:
            if hit_ennemy.name == "gumba":
                self.test_score("100",hit_ennemy.rect.x,hit_ennemy.rect.y)
                info.game_info["scores"] += 100
            elif hit_ennemy.name == "koopa":
                self.test_score("200",hit_ennemy.rect.x,hit_ennemy.rect.y)
                info.game_info["scores"] += 200
            elif hit_ennemy.name == "shell":
                self.test_score("200",hit_ennemy.rect.x,hit_ennemy.rect.y)
                info.game_info["scores"] += 200
            self.ennemy.remove(hit_ennemy)
            sound.kick.play()
            hit_ennemy.jumpToDeath()
            self.ennemy_death.add(hit_ennemy)
        brick.rect.y += 1

    def check_if_mario_is_falling(self):
        self.mario.rect.y += 1
        group_collide = pg.sprite.Group(self.brick,self.ground_pipe_stair,self.coin_brick)

        if  pg.sprite.spritecollideany(self.mario,group_collide) is None:
            if self.mario.state != c.JUMP and self.mario.state != c.TOSMALL and self.mario.state != c.TORED and self.mario.state != c.TOBIG and self.mario.state != c.WAITFLAG and self.mario.state != c.JUMPTODEATH and self.mario.state != c.SLIDEFLAG and self.mario.state != c.WALKTOCASTLE:
                self.mario.state = c.FALL

        self.mario.rect.y -= 1



######### POWER COLLISION #########

    def adjust_position_power(self):
        for m in self.power:
            if m.name == "mush" and m.state != c.MUSH_SPAWN:
                self.power.remove(m)
                m.rect.x += round(m.vx)
                self.check_mush_collision_x(m)

                m.rect.y += round(m.vy)
                self.check_mush_collision_y(m)
                self.power.add(m)
            elif m.name == "star" and m.state != c.STAR_SPAWN:
                m.rect.x += round(m.vx)
                self.check_star_collision_x(m)

                m.rect.y += round(m.vy)
                self.check_star_collision_y(m)

    def check_star_collision_x(self,star):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(star,self.ground_pipe_stair)
        hit_brick = pg.sprite.spritecollideany(star,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(star,self.coin_brick)

        if hit_ground_pipe_stair:
            self.adjust_position_power_x(star,hit_ground_pipe_stair)
        elif hit_brick:
            self.adjust_position_power_x(star,hit_brick)
        elif hit_coin_brick:
            self.adjust_position_power_x(star,hit_coin_brick)

    def check_star_collision_y(self,star):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(star,self.ground_pipe_stair)
        hit_brick = pg.sprite.spritecollideany(star,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(star,self.coin_brick)

        if hit_brick and hit_coin_brick:
            hit_brick,hit_coin_brick = self.prevent_error_collision(hit_brick,hit_coin_brick)

        if hit_ground_pipe_stair:
            self.adjust_position_power_y(star,hit_ground_pipe_stair)
        elif hit_brick:
            self.adjust_position_power_y(star,hit_brick)
        elif hit_coin_brick:
            self.adjust_position_power_y(star,hit_coin_brick)


    def check_mush_collision_x(self,mush):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(mush,self.ground_pipe_stair)
        hit_mush = pg.sprite.spritecollideany(mush,self.power)
        hit_brick = pg.sprite.spritecollideany(mush,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(mush,self.coin_brick)

        if hit_ground_pipe_stair:
            self.adjust_position_power_x(mush,hit_ground_pipe_stair)
        elif hit_mush:
            self.adjust_position_power_x(mush,hit_mush)
        elif hit_brick:
            self.adjust_position_power_x(mush,hit_brick)
        elif hit_coin_brick:
            self.adjust_position_power_x(mush,hit_coin_brick)

    def adjust_position_power_x(self,power,collider):
        if power.rect.right > collider.rect.left and power.rect.left < collider.rect.left:
            power.rect.right = collider.rect.left
            power.vx *= -1
        elif power.rect.left < collider.rect.right and power.rect.right > collider.rect.right:
            power.rect.left = collider.rect.right
            power.vx *= -1

    def check_mush_collision_y(self,mush):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(mush,self.ground_pipe_stair)

        hit_brick = pg.sprite.spritecollideany(mush,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(mush,self.coin_brick)

        if hit_brick and hit_coin_brick:
            hit_brick,hit_coin_brick = self.prevent_error_collision(hit_brick,hit_coin_brick)

        if hit_ground_pipe_stair:
            self.adjust_position_power_y(mush,hit_ground_pipe_stair)
        elif hit_brick:
            self.adjust_position_power_y(mush,hit_brick)
        elif hit_coin_brick:
            self.adjust_position_power_y(mush,hit_coin_brick)

    def adjust_position_power_y(self,power,collider):
        if power.rect.bottom > collider.rect.top and power.rect.top < collider.rect.top:
            if power.name == "mush":
                power.vy = 0
            elif power.name == "star":
                power.vy *= -1
            power.rect.bottom = collider.rect.top

        elif power.rect.top < collider.rect.bottom and power.rect.bottom > collider.rect.bottom:
            if power.name == "mush":
                power.vy = 0
            elif power.name == "star":
                power.vy *= -1
            power.rect.top = collider.rect.bottom
            

######### ENNEMY COLLISION #########


    def adjust_position_ennemy(self):
        for e in self.ennemy:
            if e.state != c.DEATH:
                self.ennemy.remove(e)
                e.rect.x += round(e.vx)
                self.check_ennemy_collision_x(e)
                e.rect.y += round(e.vy)
                self.check_ennemy_collision_y(e)
                self.ennemy.add(e)
           
    def check_ennemy_collision_x(self,ennemy):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(ennemy,self.ground_pipe_stair)
        hit_ennemy = pg.sprite.spritecollideany(ennemy,self.ennemy)
        hit_brick = pg.sprite.spritecollideany(ennemy,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(ennemy,self.coin_brick)

        if hit_ground_pipe_stair:
            self.adjust_position_ennemy_x(ennemy,hit_ground_pipe_stair)
        elif hit_ennemy:
            self.adjust_collision_ennemy_to_ennemy_x(ennemy,hit_ennemy)
        elif hit_brick:
            self.adjust_position_ennemy_x(ennemy,hit_brick)
        elif hit_coin_brick:
            self.adjust_position_ennemy_x(ennemy,hit_coin_brick)

    def adjust_collision_ennemy_to_ennemy_x(self,ennemy1,ennemy2):
        if ennemy1.rect.right > ennemy2.rect.left and ennemy1.rect.left < ennemy2.rect.left:
            if ennemy1.name == "shell":
                if ennemy2.name == "gumba":
                    self.test_score("100",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy2.name == "koopa":
                    self.test_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy2.name == "shell":
                    self.test_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy2)
                sound.kick.play()
                ennemy2.jumpToDeath()
                self.ennemy_death.add(ennemy2)
            else:
                ennemy1.rect.right = ennemy2.rect.left
                ennemy1.vx *= -1

        elif ennemy1.rect.left < ennemy2.rect.right and ennemy1.rect.right > ennemy2.rect.right:
            if ennemy1.name == "shell":
                if ennemy2.name == "gumba":
                    self.test_score("100",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy2.name == "koopa":
                    self.test_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy2.name == "shell":
                    self.test_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy2)
                sound.kick.play()
                ennemy2.jumpToDeath()
                self.ennemy_death.add(ennemy2)
            else:
                ennemy1.rect.left = ennemy2.rect.right
                ennemy1.vx *= -1

    def adjust_position_ennemy_x(self,ennemy,collider):
        if ennemy.rect.right > collider.rect.left and ennemy.rect.left < collider.rect.left:
            ennemy.rect.right = collider.rect.left
            ennemy.vx *= -1
        elif ennemy.rect.left < collider.rect.right and ennemy.rect.right > collider.rect.right:
            ennemy.rect.left = collider.rect.right
            ennemy.vx *= -1

    def check_ennemy_collision_y(self,ennemy):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(ennemy,self.ground_pipe_stair)
        hit_ennemy = pg.sprite.spritecollideany(ennemy,self.ennemy)
        hit_brick = pg.sprite.spritecollideany(ennemy,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(ennemy,self.coin_brick)

        if hit_brick and hit_coin_brick:
            hit_brick,hit_coin_brick = self.prevent_error_collision(hit_brick,hit_coin_brick)

        if hit_ground_pipe_stair:
            self.adjust_position_ennemy_y(ennemy,hit_ground_pipe_stair)
        elif hit_ennemy:
            self.adjust_position_ennemy_to_ennemy_y(ennemy,hit_ennemy)
        elif hit_brick:
            self.adjust_position_ennemy_y(ennemy,hit_brick)
        elif hit_coin_brick:
            self.adjust_position_ennemy_y(ennemy,hit_coin_brick)

    def adjust_position_ennemy_y(self,ennemy,collider):
        if ennemy.rect.bottom > collider.rect.top and ennemy.rect.top < collider.rect.top:
            ennemy.vy = 0
            ennemy.rect.bottom = collider.rect.top

        elif ennemy.rect.top < collider.rect.bottom and ennemy.rect.bottom > collider.rect.bottom:
            ennemy.vy = 0
            ennemy.rect.top = collider.rect.bottom
    
    def adjust_position_ennemy_to_ennemy_y(self,ennemy1,ennemy2):
        if ennemy1.rect.bottom > ennemy2.rect.top and ennemy1.rect.top < ennemy2.rect.top:
            if ennemy1.name == "shell":
                if ennemy2.name == "gumba":
                    self.test_score("100",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy2.name == "koopa":
                    self.test_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy2.name == "shell":
                    self.test_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy2)
                sound.kick.play()
                ennemy2.jumpToDeath()
                self.ennemy_death.add(ennemy2)
            else:
                ennemy1.vy = 0
                ennemy1.rect.bottom = ennemy2.rect.top

        elif ennemy1.rect.top < ennemy2.rect.bottom and ennemy1.rect.bottom > ennemy2.rect.bottom:
            if ennemy1.name == "shell":
                if ennemy2.name == "gumba":
                    self.test_score("100",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy2.name == "koopa":
                    self.test_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy2.name == "shell":
                    self.test_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy2)
                sound.kick.play()
                ennemy2.jumpToDeath()
                self.ennemy_death.add(ennemy2)
            else:
                ennemy1.vy = 0
                ennemy1.rect.top = ennemy2.rect.bottom


######### FIREBALL COLLISION ###########
    def adjust_position_fireball(self):
        for b in self.fireball:
            b.rect.x += round(b.vx)
            self.check_fireball_collision_x(b)
            b.rect.y += round(b.vy)
            self.check_fireball_collision_y(b)
        
           
    def check_fireball_collision_x(self,fireball):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(fireball,self.ground_pipe_stair)
        hit_ennemy = pg.sprite.spritecollideany(fireball,self.ennemy)
        hit_brick = pg.sprite.spritecollideany(fireball,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(fireball,self.coin_brick)

        if hit_ground_pipe_stair:
            self.adjust_position_fireball_x(fireball,hit_ground_pipe_stair)
        elif hit_ennemy:
            self.adjust_collision_fireball_to_ennemy_x(fireball,hit_ennemy)
        elif hit_brick:
            self.adjust_position_fireball_x(fireball,hit_brick)
        elif hit_coin_brick:
            self.adjust_position_fireball_x(fireball,hit_coin_brick)

    def adjust_collision_fireball_to_ennemy_x(self,fireball,ennemy):
        if ennemy.name == "gumba":
            self.test_score("100",ennemy.rect.x,ennemy.rect.y)
            info.game_info["scores"] += 100
        elif ennemy.name == "koopa":
            self.test_score("200",ennemy.rect.x,ennemy.rect.y)
            info.game_info["scores"] += 200
        elif ennemy.name == "shell":
            self.test_score("200",ennemy.rect.x,ennemy.rect.y)
            info.game_info["scores"] += 200
        if fireball.rect.right > ennemy.rect.left and fireball.rect.left < ennemy.rect.left:
            self.ennemy.remove(ennemy)
            sound.kick.play()
            ennemy.jumpToDeath()
            fireball.kill()
            self.ennemy_death.add(ennemy)
            
        elif fireball.rect.left < ennemy.rect.right and fireball.rect.right > ennemy.rect.right:
            self.ennemy.remove(ennemy)
            sound.kick.play()
            ennemy.jumpToDeath()
            fireball.kill()
            self.ennemy_death.add(ennemy)

    def adjust_position_fireball_x(self,fireball,collider):
        if fireball.rect.right > collider.rect.left and fireball.rect.left < collider.rect.left:
            fireball.rect.right = collider.rect.left
            fireball.vx = 0
            fireball.kill()

        elif fireball.rect.left < collider.rect.right and fireball.rect.right > collider.rect.right:
            fireball.rect.left = collider.rect.right
            fireball.vx = 0
            fireball.kill()

    def check_fireball_collision_y(self,fireball):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(fireball,self.ground_pipe_stair)
        hit_ennemy = pg.sprite.spritecollideany(fireball,self.ennemy)
        hit_brick = pg.sprite.spritecollideany(fireball,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(fireball,self.coin_brick)

        if hit_brick and hit_coin_brick:
            hit_brick,hit_coin_brick = self.prevent_error_collision(hit_brick,hit_coin_brick)

        if hit_ground_pipe_stair:
            self.adjust_position_fireball_y(fireball,hit_ground_pipe_stair)
        elif hit_ennemy:
            self.adjust_position_fireball_to_ennemy_y(fireball,hit_ennemy)
        elif hit_brick:
            self.adjust_position_fireball_y(fireball,hit_brick)
        elif hit_coin_brick:
            self.adjust_position_fireball_y(fireball,hit_coin_brick)

    def adjust_position_fireball_y(self,fireball,collider):
        
        if fireball.rect.bottom > collider.rect.top and fireball.rect.top < collider.rect.top:
            fireball.vy *= -1
            fireball.rect.bottom = collider.rect.top

        elif fireball.rect.top < collider.rect.bottom and fireball.rect.bottom > collider.rect.bottom:
            fireball.vy *= -1
            fireball.rect.top = collider.rect.bottom
    
    def adjust_position_fireball_to_ennemy_y(self,fireball,ennemy):
        if ennemy.name == "gumba":
            self.test_score("100",ennemy.rect.x,ennemy.rect.y)
            info.game_info["scores"] += 100
        elif ennemy.name == "koopa":
            self.test_score("200",ennemy.rect.x,ennemy.rect.y)
            info.game_info["scores"] += 200
        elif ennemy.name == "shell":
            self.test_score("200",ennemy.rect.x,ennemy.rect.y)
            info.game_info["scores"] += 200
        if fireball.rect.bottom > ennemy.rect.top and fireball.rect.top < ennemy.rect.top:
            self.ennemy.remove(ennemy)
            sound.kick.play()
            ennemy.jumpToDeath()
            fireball.kill()
            self.ennemy_death.add(ennemy)

        elif fireball.rect.top < ennemy.rect.bottom and fireball.rect.bottom > ennemy.rect.bottom:
            self.ennemy.remove(ennemy)
            sound.kick.play()
            ennemy.jumpToDeath()
            fireball.kill()
            self.ennemy_death.add(ennemy)




