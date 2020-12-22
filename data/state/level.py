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
from .. import setup

class Level(state.State):
    def __init__(self):
        state.State.__init__(self)
        
    def startup(self,current_time):
        self.next = None
        self.state = c.NOTFREEZE
        self.timeOut = False
        self.transition = False
        self.under = False
        self.multi = info.game_info["multi"]
        self.current_update = current_time
        self.timeOut_timer = 0
        self.timeEnd_timer = 0
        self.under_timer = 0
        self.setup_everything()
        self.info = info.Info(c.LEVEL)

    def setup_background(self):
        self.background = pg.image.load("images/fond_1.png").convert()
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,(int(self.back_rect.width * c.BACKGROUND_SIZE_MULTIPLIER),int(self.back_rect.height * c.BACKGROUND_SIZE_MULTIPLIER)))
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height

        self.level = pg.Surface((width,height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = setup.SCREEN.get_rect(bottom = self.level_rect.bottom)
        self.viewport.x = 0
        
        
    def setup_mario(self):
        self.fireball_mario = pg.sprite.Group()
        self.fireball_luigi = pg.sprite.Group()
       

        if not info.game_info["multi"]:
            self.mario = Mario(100,c.GROUND_HEIGHT,self.fireball_mario)
            self.mario_death_timer = 0
            self.player = [self.mario]
            self.mario_test = True
        else:
            self.player = []
            if info.game_info["mario_lifes"] > 0:
                self.mario = Mario(100,c.GROUND_HEIGHT,self.fireball_mario)
                self.mario_death_timer = 0
                self.mario_test = True
                self.player.append(self.mario)
            if info.game_info["luigi_lifes"] > 0:
                self.luigi = Luigi(50,c.GROUND_HEIGHT,self.fireball_luigi)
                self.luigi_death_timer = 0
                self.luigi_test = True
                self.player.append(self.luigi)
            

    def setup_ground(self):
        ground_1 = Collider(0,c.GROUND_HEIGHT,1104,24)
        ground_2 = Collider(1136,c.GROUND_HEIGHT,240,24)
        ground_3 = Collider(1424,c.GROUND_HEIGHT,1024,24)
        ground_4 = Collider(2480,c.GROUND_HEIGHT,912,24)
        ground_5 = Collider(3392,c.GROUND_HEIGHT,256,24)
        self.ground = pg.sprite.Group(ground_1,ground_2,ground_3,ground_4,ground_5)

    def setup_pipe(self):
        pipe_1 = Pipe(448,168,32,32)
        pipe_2 = Pipe(608,152,32,48)
        pipe_3 = Pipe(736,136,32,64)
        pipe_4 = Pipe(912,136,32,64)
        pipe_5 = Pipe(2608,168,32,32)
        pipe_6 = Pipe(2864,168,32,32)
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

        brick_1 = BrickOverWorld(320,136)
        brick_2 = BrickOverWorld(352,136)
        brick_3 = BrickOverWorld(384,136)
        brick_4 = BrickOverWorld(1232,136)
        brick_5 = BrickOverWorld(1264,136)
        brick_6 = BrickOverWorld(1280,72)
        brick_7 = BrickOverWorld(1296,72)
        brick_8 = BrickOverWorld(1312,72)
        brick_9 = BrickOverWorld(1328,72)
        brick_10 = BrickOverWorld(1344,72)
        brick_11 = BrickOverWorld(1360,72)
        brick_12 = BrickOverWorld(1376,72)
        brick_13 = BrickOverWorld(1392,72)
        brick_14 = BrickOverWorld(1456,72)
        brick_15 = BrickOverWorld(1472,72)
        brick_16 = BrickOverWorld(1488,72)
        brick_17 = BrickOverWorld(1504,136,self.coin,"coin")  # coin
        brick_18 = BrickOverWorld(1600,136)
        brick_19 = BrickOverWorld(1616,136,self.power,"star") # star
        brick_20 = BrickOverWorld(1888,136)
        brick_21 = BrickOverWorld(1936,72)
        brick_22 = BrickOverWorld(1952,72)
        brick_23 = BrickOverWorld(1968,72)
        brick_24 = BrickOverWorld(2048,72)
        brick_25 = BrickOverWorld(2096,72)
        brick_26 = BrickOverWorld(2064,136)
        brick_27 = BrickOverWorld(2080,136)
        brick_28 = BrickOverWorld(2688,136)
        brick_29 = BrickOverWorld(2704,136)
        brick_30 = BrickOverWorld(2736,136)
        brick_74 = BrickInvisible(1021,120,self.power,"mushLife") # mushLife invisible
        # underGround
        brick_31 = BrickUnderground(3392,184)
        brick_32 = BrickUnderground(3392,168)
        brick_33 = BrickUnderground(3392,152)
        brick_34 = BrickUnderground(3392,136)
        brick_35 = BrickUnderground(3392,120)
        brick_36 = BrickUnderground(3392,104)
        brick_37 = BrickUnderground(3392,88)
        brick_38 = BrickUnderground(3392,72)
        brick_39 = BrickUnderground(3392,56)
        brick_40 = BrickUnderground(3392,40)
        brick_41 = BrickUnderground(3392,24)
        brick_42 = BrickUnderground(3467,24)
        brick_43 = BrickUnderground(3483,24)
        brick_44 = BrickUnderground(3499,24)
        brick_45 = BrickUnderground(3515,24)
        brick_46 = BrickUnderground(3531,24)
        brick_47 = BrickUnderground(3547,24)
        brick_48 = BrickUnderground(3563,24)
        brick_49 = BrickUnderground(3579,24)

        brick_50 = BrickUnderground(3467,152)
        brick_51 = BrickUnderground(3467,168)
        brick_52 = BrickUnderground(3467,184)
        brick_53 = BrickUnderground(3483,152)
        brick_54 = BrickUnderground(3483,168)
        brick_55 = BrickUnderground(3483,184)
        brick_56 = BrickUnderground(3499,152)
        brick_57 = BrickUnderground(3499,168)
        brick_58 = BrickUnderground(3499,184)
        brick_59 = BrickUnderground(3515,152)
        brick_60 = BrickUnderground(3515,168)
        brick_61 = BrickUnderground(3515,184)
        brick_62 = BrickUnderground(3531,152)
        brick_63 = BrickUnderground(3531,168)
        brick_64 = BrickUnderground(3531,184)
        brick_65 = BrickUnderground(3547,152)
        brick_66 = BrickUnderground(3547,168)
        brick_67 = BrickUnderground(3547,184)
        brick_68 = BrickUnderground(3563,152)
        brick_69 = BrickUnderground(3563,168)
        brick_70 = BrickUnderground(3563,184)
        brick_71 = BrickUnderground(3579,152)
        brick_72 = BrickUnderground(3579,168)
        brick_73 = BrickUnderground(3579,184)

        self.brick = pg.sprite.Group(brick_1,brick_2,brick_3,brick_4,brick_5,brick_6,brick_7,brick_8,brick_9,
                                        brick_10,brick_11,brick_12,brick_13,brick_14,brick_15,brick_16,brick_17,
                                        brick_18,brick_19,brick_20,brick_21,brick_22,brick_23,brick_24,brick_25,brick_26,
                                        brick_27,brick_28,brick_29,brick_30,brick_31,brick_32,brick_33,brick_34,brick_35,
                                        brick_36,brick_37,brick_38,brick_39,brick_40,brick_41,brick_42,brick_43,brick_44,
                                        brick_45,brick_46,brick_47,brick_48,brick_49,brick_50,brick_51,brick_52,brick_53,
                                        brick_54,brick_55,brick_56,brick_57,brick_58,brick_59,brick_60,brick_61,brick_62,
                                        brick_63,brick_64,brick_65,brick_66,brick_67,brick_68,brick_69,brick_70,brick_71,
                                        brick_72,brick_73,brick_74)
       
        
    def setup_coin(self):
        coin1 = BigCoin(3470,106)
        coin2 = BigCoin(3470,138)
        coin3 = BigCoin(3489,106)
        coin4 = BigCoin(3489,138)
        coin5 = BigCoin(3508,106)
        coin6 = BigCoin(3508,138)
        coin7 = BigCoin(3526,106)
        coin8 = BigCoin(3526,138)
        coin9 = BigCoin(3545,106)
        coin10 = BigCoin(3545,138)
        coin11 = BigCoin(3564,106)
        coin12 = BigCoin(3564,138)
        coin13 = BigCoin(3582,106)
        coin14 = BigCoin(3582,138)
        coin15 = BigCoin(3489,74)
        coin16 = BigCoin(3508,74)
        coin17 = BigCoin(3526,74)
        coin18 = BigCoin(3545,74)
        coin19 = BigCoin(3564,74)
        self.bigCoin = pg.sprite.Group(coin1,coin2,coin3,coin4,coin5,coin6,coin7,coin8,coin9,coin10,coin11,coin12,coin13,coin14,coin15,coin16,coin17,coin18,coin19)

    def setup_coin_brick(self):
        coin_brick_1 = CoinBrickOverworld(256,136,self.coin,"coin")
        coin_brick_2 = CoinBrickOverworld(336,136,self.power,"mush")
        coin_brick_3 = CoinBrickOverworld(368,136,self.coin,"coin")
        coin_brick_4 = CoinBrickOverworld(352,72,self.coin,"coin")
        coin_brick_5 = CoinBrickOverworld(1248,136,self.power,"mush")
        coin_brick_6 = CoinBrickOverworld(1504,72,self.coin,"coin")
        coin_brick_7 = CoinBrickOverworld(1696,136,self.coin,"coin")
        coin_brick_8 = CoinBrickOverworld(1744,136,self.coin,"coin")
        coin_brick_9 = CoinBrickOverworld(1792,136,self.coin,"coin")
        coin_brick_10 = CoinBrickOverworld(1744,72,self.coin,"coin")
        coin_brick_12 = CoinBrickOverworld(2064,72,self.coin,"coin")
        coin_brick_13 = CoinBrickOverworld(2080,72,self.coin,"coin")
        coin_brick_14 = CoinBrickOverworld(2720,136,self.coin,"coin")

        self.coin_brick = pg.sprite.Group(coin_brick_1,coin_brick_2,coin_brick_3,coin_brick_4,coin_brick_5,coin_brick_6,
                                            coin_brick_7,coin_brick_8,coin_brick_9,coin_brick_10,coin_brick_12,
                                            coin_brick_13,coin_brick_14)

    def setup_power(self):
        self.power = pg.sprite.Group()

    def setup_ennemy(self):
        e1 = GumbaUnderground(352,184, -1)

        e2 = GumbaOverworld(642,184, 1)
        self.ennemy_g1 = pg.sprite.Group(e2)

        e3 = GumbaOverworld(820,184,-1)
        e4 = GumbaOverworld(845,184,-1)
        self.ennemy_g2 = pg.sprite.Group(e3,e4)

        e5 = GumbaOverworld(1300,55,-1)
        e6 = GumbaOverworld(1325,55,-1)
        self.ennemy_g3 = pg.sprite.Group(e5,e6)

        e7 = GumbaOverworld(1562,184,-1)
        e8 = GumbaOverworld(1587,184,-1)
        self.ennemy_g4 = pg.sprite.Group(e7,e8)

        e9 = KoopaUnderground(1715,176,-1)
        e10 = GumbaOverworld(1830,184,-1)
        e11 = GumbaOverworld(1855,184,-1)
        self.ennemy_g5 = pg.sprite.Group(e9,e10,e11)

        e12 = GumbaOverworld(1985,184,-1)
        e13 = GumbaOverworld(2010,184,-1)
        e14 = GumbaOverworld(2050,184,-1)
        e15 = GumbaOverworld(2075,184,-1)
        self.ennemy_g6 = pg.sprite.Group(e12,e13,e14,e15)

        e16 = GumbaOverworld(2780,184,-1)
        e17 = GumbaOverworld(2805,184,-1)
        self.ennemy_g7 = pg.sprite.Group(e16,e17)

        
        self.ennemy = pg.sprite.Group(e1)
        self.ennemy_death = pg.sprite.Group()

        self.all_ennemy = pg.sprite.Group(self.ennemy,self.ennemy_death,self.ennemy_g1,self.ennemy_g2,self.ennemy_g3,self.ennemy_g4,self.ennemy_g5,self.ennemy_g6,self.ennemy_g7)

    def setup_checkpoint(self):
        check1 = checkPoint(470,0,1,c.HEIGHT,"1")
        check2 = checkPoint(600,0,1,c.HEIGHT,"2")
        check3 = checkPoint(1100,0,1,c.HEIGHT,"3")
        check4 = checkPoint(1400,0,1,c.HEIGHT,"4")
        check5 = checkPoint(1530,0,1,c.HEIGHT,"5")
        check6 = checkPoint(1830,0,1,c.HEIGHT,"6")
        check7 = checkPoint(2630,0,1,c.HEIGHT,"7")
        check8 = checkPoint(3175,32,1,152,"8")
        check9 = checkPoint(912,130,32,c.HEIGHT,"pipe")
        check10 = checkPoint(3633,168,1,c.HEIGHT,"pipe2")
        check11 = checkPoint(3168,183,9,10,"9")
        self.checkpoint = pg.sprite.Group(check1,check2,check3,check4,check5,check6,check7,check8,check9,check10,check11)
        self.flag = Flag(3175,40)
        self.flagEnd = FlagEnd(3265,140)
        

    def setup_everything(self):
        self.setup_background()
        self.setup_mario()
        self.setup_ground()
        self.setup_pipe()
        self.setup_stair()
        self.setup_power()
        self.setup_coin()
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
            self.update_while_transition_mario(keys)
        elif self.state == c.INCASTLE:
            self.update_while_castle(keys)
    
    def draw_everything(self,screen):
        self.level.blit(self.background, self.viewport,self.viewport)
        self.level.blit(self.flag.image,self.flag.rect)
        if self.multi:
            if not self.luigi.inCastle and self.luigi_test and not self.mario.inCastle:
                self.level.blit(self.luigi.image,self.luigi.rect)
            if not self.mario.inCastle and self.mario_test and not self.luigi.inCastle:
                self.level.blit(self.mario.image,(self.mario.rect.x,self.mario.rect.y))
        else:
            if not self.mario.inCastle and self.mario_test:
                self.level.blit(self.mario.image,(self.mario.rect.x,self.mario.rect.y))
        if self.flagEnd.rect.top < 121 * c.BACKGROUND_SIZE_MULTIPLIER:
            self.level.blit(self.flagEnd.image,self.flagEnd.rect)
        self.ground.draw(self.level)
        self.pipe.draw(self.level)
        self.bigCoin.draw(self.level)
        self.power.draw(self.level)
        self.brick.draw(self.level)
        self.ennemy.draw(self.level)
        self.ennemy_death.draw(self.level)
        self.coin_brick.draw(self.level)
        if self.multi:
             self.fireball = pg.sprite.Group(self.fireball_mario,self.fireball_mario)
        else:
            self.fireball = pg.sprite.Group(self.fireball_mario)
        self.fireball.draw(self.level)
        #self.checkpoint.draw(self.level)
        self.coin.draw(self.level)
        self.draw_score(self.level)
        self.brick_piece.draw(self.level)

        if not self.transition:
            screen.blit(self.level,(0,0),self.viewport)
            self.info.draw(screen)
        else:
            screen.fill((0,0,0))
    
    def update_all_sprites(self,keys):
        self.mario.update(keys)
        if self.multi:
            self.luigi.update(keys)
        self.brick.update()
        self.brick_piece.update()
        self.coin_brick.update(self.current_update)
        self.coin.update(self.current_update)
        self.bigCoin.update(self.current_update)
        self.power.update(self.current_update)
        self.ennemy.update(self.current_update)
        self.ennemy_death.update(self.current_update)
        if self.multi:
             self.fireball = pg.sprite.Group(self.fireball_mario,self.fireball_mario)
        else:
            self.fireball = pg.sprite.Group(self.fireball_mario)
        self.fireball.update()
        self.flag.update()
        self.update_score()
        self.adjust_position_player()
        self.adjust_position_power()
        self.adjust_position_ennemy()
        self.adjust_position_fireball()
        self.info.update(self.current_update,self.mario.state)
        self.update_viewport()
        self.check_if_mario_in_transition()
        self.check_if_change_state()
        self.check_if_timeout()
        self.check_if_transition()

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
        
    def update_while_transition_mario(self,keys):
        self.mario.update(keys)
        if self.multi:
            self.luigi.update(keys)
        self.coin_brick.update(self.current_update)
        self.bigCoin.update(self.current_update)
        self.info.update(self.current_update,self.mario.state)
        self.check_if_mario_in_transition()
        self.check_if_change_state()
        self.check_if_timeout()
        self.check_if_transition()

    def check_if_transition(self):
        if self.transition:
            if self.under_timer == 0:
                sound.pipe.play()
                self.under = not self.under
                self.under_timer = self.current_update
            elif self.current_update - self.under_timer > 1000:
                self.under_timer = 0
                self.state = c.NOTFREEZE
                self.transition = False
                if self.under:
                    self.set_in_underground()
                elif not self.under:
                    self.set_in_overworld()

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

        if not self.multi:
            if int(info.game_info["time"]) == 0 and not self.mario.dead:
                self.mario.vy = - 8
                self.mario.state = c.JUMPTODEATH
                sound.main.stop()
        else:
            if int(info.game_info["time"]) == 0 and not self.mario.dead and not self.luigi.dead:
                self.mario.vy = - 8
                self.mario.state = c.JUMPTODEATH
                self.luigi.vy = -8
                self.luigi.state = c.JUMPTODEATH
                sound.main.stop()


    def check_if_change_state(self):
        if not self.multi:
            if self.mario.rect.y > c.HEIGHT:
                self.mario.dead = True
                sound.main.stop()

            if self.mario.dead:
                self.play_die_song_mario()
        else:
            if self.mario.rect.y > c.HEIGHT:
                self.mario.dead = True
                

            if self.luigi.rect.y > c.HEIGHT:
                self.luigi.dead = True
                

            if self.mario.dead and self.mario_test:
                self.play_die_song_mario()
            
            if self.luigi.dead and self.luigi_test:
                self.play_die_song_luigi()

    def play_die_song_mario(self):
        if not self.multi:
            if self.mario_death_timer == 0:
                sound.main.stop()
                sound.die.play()
                self.mario_death_timer = self.current_update
            elif (self.current_update - self.mario_death_timer) > 3000:
                self.done = True
                self.set_game_info()
        else:
            if self.mario_death_timer == 0:
                if self.luigi.dead:
                    sound.main.stop()
                    sound.die.play()
                self.mario_death_timer = self.current_update
            elif (self.current_update - self.mario_death_timer) > 3000:
                if self.luigi.dead:
                    self.done = True
                self.set_game_info()
                self.mario_test = False

    def play_die_song_luigi(self):
            if self.luigi_death_timer == 0:
                if self.mario.dead:
                    sound.main.stop()
                    sound.die.play()
                self.luigi_death_timer = self.current_update
            elif (self.current_update - self.luigi_death_timer) > 3000:
                if self.mario.dead:
                    self.done = True
                self.set_game_info()
                self.luigi_test = False 

    def set_game_info(self):
        if not self.multi:
            if int(info.game_info["time"]) == 0:
                self.next = c.TIMEOUT
                info.game_info["mario_lifes"] -= 1

            elif self.mario.dead:
                info.game_info["mario_lifes"] -= 1
                self.next = c.LOAD
            
            if info.game_info["mario_lifes"] == 0:
                self.next = c.GAMEOVER
        else:
            if int(info.game_info["time"]) == 0:
                self.next = c.TIMEOUT
                info.game_info["mario_lifes"] -= 1
                info.game_info["luigi_lifes"] -= 1

            if self.mario.dead and self.mario_test:
                info.game_info["mario_lifes"] -= 1
                self.next = c.LOAD
            if self.luigi.dead and self.luigi_test:
                info.game_info["luigi_lifes"] -= 1
                self.next = c.LOAD
            
            if info.game_info["mario_lifes"] == 0 and info.game_info["luigi_lifes"] == 0:
                self.next = c.GAMEOVER
                self.done = True
            
    def check_if_mario_in_transition(self):
        if not self.multi:
            if self.mario.transform:
                self.state = c.FREEZE
            elif self.mario.inCastle:
                self.state = c.INCASTLE
                sound.count_time.play()
            elif self.mario.inUnder and not self.under:
                self.state = c.FREEZE
                self.transition = True
            elif self.mario.canGoOverworld and self.under:
                self.state = c.FREEZE
                self.transition = True
            else:
                self.state = c.NOTFREEZE
        else:
            if self.mario.transform or self.luigi.transform:
                self.state = c.FREEZE
            elif self.mario.inCastle or self.luigi.inCastle:
                self.state = c.INCASTLE
                sound.count_time.play()
            elif (self.mario.inUnder or self.luigi.inUnder) and not self.under:
                self.state = c.FREEZE
                self.transition = True
            elif (self.mario.canGoOverworld or self.luigi.canGoOverworld) and self.under:
                self.state = c.FREEZE
                self.transition = True
            else:
                self.state = c.NOTFREEZE

    def set_in_underground(self):
        self.mario.rect.x = 3425 * c.BACKGROUND_SIZE_MULTIPLIER
        self.mario.rect.y = 40 * c.BACKGROUND_SIZE_MULTIPLIER
        self.viewport.x = 3392 * c.BACKGROUND_SIZE_MULTIPLIER
        if self.multi:
            self.luigi.rect.x = 3425 * c.BACKGROUND_SIZE_MULTIPLIER
            self.luigi.rect.y = 20 * c.BACKGROUND_SIZE_MULTIPLIER
    
    def set_in_overworld(self):
        if self.multi:
            self.luigi.inUnder = False
            self.luigi.vx = 0
            self.luigi.rect.centerx = 2618 * c.BACKGROUND_SIZE_MULTIPLIER
            self.luigi.rect.bottom = 168 * c.BACKGROUND_SIZE_MULTIPLIER
        self.mario.inUnder = False
        self.mario.vx = 0
        self.mario.rect.centerx = 2625 * c.BACKGROUND_SIZE_MULTIPLIER
        self.mario.rect.bottom = 168 * c.BACKGROUND_SIZE_MULTIPLIER
        self.viewport.x = 2476 * c.BACKGROUND_SIZE_MULTIPLIER
        
    def set_score(self,string,x,y):
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

    def update_viewport(self):
        if not self.multi:
            if self.viewport.x < 3092 * c.BACKGROUND_SIZE_MULTIPLIER:
                third = self.viewport.x + self.viewport.w / 3
                mario_center = self.mario.rect.centerx
                mario_right = self.mario.rect.right

                if self.mario.vx > 0 and mario_center >= third:
                    if mario_right < self.viewport.centerx:
                        mult = 0.5
                    else:
                        mult = 1
                    new = self.viewport.x + mult * self.mario.vx
                    highest = self.level_rect.w - self.viewport.w
                    self.viewport.x = min(highest,new)
        elif self.multi:
            if self.viewport.x < 3092 * c.BACKGROUND_SIZE_MULTIPLIER:
                third = self.viewport.x + self.viewport.w / 3
                mario_center = self.mario.rect.centerx
                mario_right = self.mario.rect.right
                luigi_center = self.luigi.rect.centerx
                luigi_right = self.luigi.rect.right

                if (self.mario.vx > 0 and mario_center >= third):
                    if (mario_right < self.viewport.centerx):
                        mult = 0.5
                    else:
                        mult = 1
                    new = self.viewport.x + mult * self.mario.vx
                    highest = self.level_rect.w - self.viewport.w
                    self.viewport.x = min(highest,new)
                elif (self.luigi.vx > 0 and luigi_center >= third):
                    if (luigi_right < self.viewport.centerx):
                        mult = 0.5
                    else:
                        mult = 1
                    new = self.viewport.x + mult * self.luigi.vx
                    highest = self.level_rect.w - self.viewport.w
                    self.viewport.x = min(highest,new)
                    
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

    def adjust_position_player(self):
        for player in self.player:
            player.rect.x += round(player.vx)
            if not player.state == c.JUMPTODEATH:
                player.canGoUnder = False
                player.canGoOverworld = False
                self.check_mario_x_collision(player)

            player.rect.y += round(player.vy)
            if not player.state == c.JUMPTODEATH and player.transform == False:
                self.check_mario_y_collision(player)

  ######### MARIO COLLISION #########

    def check_mario_x_collision(self,player):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(player,self.ground_pipe_stair)
        hit_block = pg.sprite.spritecollideany(player,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(player,self.coin_brick)
        hit_power = pg.sprite.spritecollideany(player,self.power)
        hit_coin = pg.sprite.spritecollideany(player,self.bigCoin)

        hit_ennemy = pg.sprite.spritecollideany(player,self.ennemy)

        hit_checkpoint = pg.sprite.spritecollideany(player,self.checkpoint)
        
        if hit_ground_pipe_stair:
            self.adjust_position_x(hit_ground_pipe_stair,player)
        elif hit_block:
            self.adjust_position_x(hit_block,player)
        elif hit_coin_brick:
            self.adjust_position_x(hit_coin_brick,player)
        elif hit_power:
            self.adjust_collision_power(hit_power,player)
        elif hit_coin:
            sound.coin.play()
            info.game_info["coin_count"] += 1
            hit_coin.kill()
        elif hit_ennemy and not player.wasTouched and not player.state == c.JUMPTODEATH:
            self.adjust_collision_ennemy_x(hit_ennemy,player)
        elif hit_checkpoint:
            self.adjust_collision_checkpoint(hit_checkpoint,player)

        if player.rect.x < self.viewport.x:
            player.rect.x = self.viewport.x
        
        


    def adjust_collision_checkpoint(self,checkpoint,player):
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
        elif checkpoint.name == "8" and player.state != c.SLIDEFLAG and player.state != c.WAITFLAG:
            if self.multi:
                if self.luigi.state != c.SLIDEFLAG and self.luigi.state != c.WAITFLAG and self.mario.state != c.SLIDEFLAG and self.mario.state != c.WAITFLAG:
                    sound.main.stop()
                    sound.flag.play()
            else:
                sound.main.stop()
                sound.flag.play()
            player.state = c.SLIDEFLAG
            player.rect.right = checkpoint.rect.x + 10
            if self.flag.state != c.SLIDEFLAG:
                self.flag.state = c.SLIDEFLAG
            if player.rect.centery < 125:
                info.game_info[str(player.name)+"_lifes"] += 1
                sound.up.play()

            elif player.rect.centery > 125 and player.rect.centery < 168:
                info.game_info["scores"] += 5000
                self.set_score("5000",player.rect.x+30,player.rect.y )

            elif player.rect.centery > 168 and player.rect.centery < 302:
                info.game_info["scores"] += 2000
                self.set_score("2000",player.rect.x+30,player.rect.y)

            elif player.rect.centery > 302 and player.rect.centery < 375:
                info.game_info["scores"] += 800
                self.set_score("800",player.rect.x+30,player.rect.y)

            elif player.rect.centery > 375 and player.rect.centery < 455:
                info.game_info["scores"] += 400
                self.set_score("400",player.rect.x+30,player.rect.y)

            elif player.rect.centery > 455 and player.rect.centery < 493:
                info.game_info["scores"] += 200
                self.set_score("200",player.rect.x+30,player.rect.y)
            if self.multi:
                if (self.luigi.state == c.SLIDEFLAG and self.mario.state == c.SLIDEFLAG) or (self.luigi.state == c.WAITFLAG and self.mario.state == c.SLIDEFLAG) or (self.luigi.state == c.SLIDEFLAG and self.mario.state == c.WAITFLAG):
                    checkpoint.kill()
            else:
                checkpoint.kill()
        elif checkpoint.name == "9" and player.state == c.SLIDEFLAG:
            
            player.rect.x = player.rect.right + 5
            player.right = False
            player.vy = 0
            if self.multi:
                if self.mario.state != c.WAITFLAG and self.mario.state != c.WALKTOCASTLE and self.luigi.state != c.WAITFLAG and self.luigi.state != c.WALKTOCASTLE:
                    sound.end.play()
            else:
                sound.end.play()
            player.state = c.WAITFLAG
        elif checkpoint.name == "pipe":
            player.canGoUnder = True
        elif checkpoint.name == "pipe2":
            player.canGoOverworld = True

    def adjust_collision_ennemy_x(self,ennemy,player):
        if player.rect.right > ennemy.rect.left and player.rect.left < ennemy.rect.left:
            if player.invincible:
                if ennemy.name == "gumba":
                    self.set_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy.name == "koopa":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "pirana":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.ennemy_death.add(ennemy)
            elif player.isBig:
                if ennemy.name == "shell" and ennemy.vx == 0:
                    
                    player.rect.right = ennemy.rect.left
                    ennemy.vx = 8
                    player.vx -= 3
                else:
                    player.state = c.TOSMALL
                    player.transform = True
                    self.change_flower_into_mush()
                    player.setWasTouched()
                    sound.pipe.play()
            else:
                if ennemy.name == "shell" and ennemy.vx == 0:
                    player.rect.right = ennemy.rect.left
                    ennemy.vx = 8
                    player.vx -= 3
                else:
                    player.vy = - 8
                    player.state = c.JUMPTODEATH
                    
                    

        elif player.rect.left < ennemy.rect.right and player.rect.right > ennemy.rect.right:
            if player.invincible:
                if ennemy.name == "gumba":
                    self.set_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy.name == "koopa":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "pirana":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.ennemy_death.add(ennemy)
            elif player.isBig:
                if ennemy.name == "shell" and ennemy.vx == 0:
                    player.rect.left = ennemy.rect.right
                    ennemy.vx = -8
                    player.vx += 3
                else:
                    player.state = c.TOSMALL
                    player.transform = True
                    self.change_flower_into_mush()
                    player.setWasTouched()
                    sound.pipe.play()
            else:
                if ennemy.name == "shell" and ennemy.vx == 0:
                    player.rect.left = ennemy.rect.right
                    ennemy.vx = -8
                    player.vx += 3
                else:
                    player.vy = - 8
                    player.state = c.JUMPTODEATH
                    
                    
    
    def adjust_position_x(self,collider,player):
        if player.rect.right > collider.rect.left and player.rect.left < collider.rect.left:
            if collider.name == "invisible":
                pass
            player.rect.right = collider.rect.left
            player.vx = 0
        elif player.rect.left < collider.rect.right and player.rect.right > collider.rect.right:
            if collider.name == "invisible":
                pass
            player.rect.left = collider.rect.right
            player.vx = 0
    
    def adjust_collision_power(self,power,player):
        info.game_info["scores"] += 1000
        self.set_score("1000",power.rect.x,power.rect.y)
        if power.name == "mush":
            power.kill()
            sound.powerup.play()
            player.state = c.TOBIG
            player.transform = True
            self.change_mush_into_flower()
        elif power.name == "flower":
            power.kill()
            player.state = c.TORED
            player.transform = True
            sound.powerup.play()
        elif power.name == "star":
            power.kill()
            sound.main.stop()
            sound.powerup.play()
            sound.star.play()
            player.setInvincible()
        elif power.name == "mushLife":
            power.kill()
            sound.up.play()
            info.game_info[str(player.name)+"_lifes"] += 1
            
    def prevent_error_collision(self,block1,block2,player):
        dist_between_block1_and_mario = abs(block1.rect.centerx - player.rect.centerx)
        dist_between_block2_and_mario = abs(block2.rect.centerx - player.rect.centerx)

        # si mario plus proche du block1 retourne Vrai pour block1 et Faux pour block2
        if dist_between_block1_and_mario < dist_between_block2_and_mario:
            return block1,False
        # inversement
        elif dist_between_block1_and_mario > dist_between_block2_and_mario:
            return False, block2
        # si dist entre mario et les 2 blocs sont égale alors par defaut block1 = Vrai et block2 = Faux
        else:
             return block1,False

    def check_mario_y_collision(self,player):
        hit_ground_pipe_stair = pg.sprite.spritecollideany(player,self.ground_pipe_stair)

        hit_block = pg.sprite.spritecollideany(player,self.brick)
        hit_coin_brick = pg.sprite.spritecollideany(player,self.coin_brick)
        
        hit_ennemy = pg.sprite.spritecollideany(player,self.ennemy)

        if hit_block and hit_coin_brick:
            hit_block,hit_coin_brick = self.prevent_error_collision(hit_block,hit_coin_brick,player)

        if hit_ground_pipe_stair:
            self.adjust_position_collider(hit_ground_pipe_stair,player)
        
        elif hit_coin_brick:
            self.adjust_position_coin_brick(hit_coin_brick,player)
        elif hit_block:
            self.adjust_position_brick(hit_block,player)
        elif hit_ennemy and not player.wasTouched:
            self.adjust_collision_ennemy_y(hit_ennemy,player)

        self.check_if_mario_is_falling(player)

    def adjust_collision_ennemy_y(self,ennemy,player):
        if player.rect.bottom > ennemy.rect.top and player.rect.top < ennemy.rect.top:
            if player.invincible:
                if ennemy.name == "gumba":
                    self.set_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy.name == "koopa":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "pirana":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.ennemy_death.add(ennemy)
            else:
                if ennemy.name == "pirana":
                    if player.isBig:
                        player.state = c.TOSMALL
                        player.transform = True
                        self.change_flower_into_mush()
                        player.setWasTouched()
                        sound.pipe.play()
                    else:
                        player.vy = - 8
                        player.state = c.JUMPTODEATH
                else:
                    sound.stomp.play()
                    player.vy = -7
                    player.rect.bottom = ennemy.rect.top
                    if ennemy.name == "gumba":
                        self.ennemy.remove(ennemy)
                        self.set_score("100",ennemy.rect.x,ennemy.rect.y)
                        info.game_info["scores"] += 100
                        ennemy.startToDeath()
                        self.ennemy_death.add(ennemy)
                    elif ennemy.name == "koopa":
                        self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                        self.ennemy.remove(ennemy)
                        info.game_info["scores"] += 200
                        if ennemy.type == "green":
                            self.ennemy.add(ShellOverworld(ennemy.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(ennemy.rect.y / c.BACKGROUND_SIZE_MULTIPLIER)+9,pg.time.get_ticks(),self.ennemy))
                        elif ennemy.type == "blue":
                            self.ennemy.add(ShellUnderground(ennemy.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(ennemy.rect.y / c.BACKGROUND_SIZE_MULTIPLIER)+9,pg.time.get_ticks(),self.ennemy))
                        elif ennemy.type == "red":
                            self.ennemy.add(ShellRed(ennemy.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(ennemy.rect.y / c.BACKGROUND_SIZE_MULTIPLIER)+9,pg.time.get_ticks(),self.ennemy))
                        ennemy.kill()
                    elif ennemy.name == "shell":
                        if ennemy.vx == 0:
                            if player.rect.centerx < (ennemy.rect.centerx - (ennemy.rect.width / 4)):
                                ennemy.vx = 8
                            elif player.rect.centerx > (ennemy.rect.centerx + (ennemy.rect.width / 4)):
                                ennemy.vx = -8
                        else:
                            ennemy.vx = 0
            
        elif player.rect.top < ennemy.rect.bottom and player.rect.bottom > ennemy.rect.bottom:
            if player.invincible:
                if ennemy.name == "gumba":
                    self.set_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy.name == "koopa":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.ennemy_death.add(ennemy)
            elif player.isBig:
                player.state = c.TOSMALL
                player.transform = True
                self.change_flower_into_mush()
                player.setWasTouched()
                sound.pipe.play()
            else:
                player.vy = - 8
                player.state = c.JUMPTODEATH
               
            

    def adjust_position_collider(self,collider,player):
        if player.rect.bottom > collider.rect.top and player.rect.top < collider.rect.top:
            player.vy = 0
            player.rect.bottom = collider.rect.top
            if player.state != c.WALKTOCASTLE and player.state != c.WAITFLAG and player.state != c.SLIDEFLAG:
                player.state = c.WALK
            player.isjump = False

        elif player.rect.top < collider.rect.bottom and player.rect.bottom > collider.rect.bottom:
            player.vy = 3
            player.rect.top = collider.rect.bottom
            player.state = c.FALL

    def adjust_position_brick(self,collider,player):
        if player.rect.bottom > collider.rect.top and player.rect.top < collider.rect.top:
            if collider.name == "invisible":
                pass
            player.vy = 0
            player.rect.bottom = collider.rect.top
            player.state = c.WALK
            player.isjump = False

        elif player.rect.top < collider.rect.bottom and player.rect.bottom > collider.rect.bottom:
            if player.isBig:
                if collider.content != "coin" and collider.content != "star" and collider.content != "mushLife" and collider.state != c.OPENED:
                    sound.break_sound.play()
                    info.game_info["scores"] += 50
                    self.check_if_ennemy_on_brick(collider)
                    collider.kill()

                    if collider.name == "overworld":
                        self.brick_piece.add(BrickPieceOverworld(collider.rect.x,collider.rect.y,-5,-12,0))
                        self.brick_piece.add(BrickPieceOverworld(collider.rect.right-16,collider.rect.y,5,-12,1))
                        self.brick_piece.add(BrickPieceOverworld(collider.rect.x,collider.rect.bottom-16,-5,-8,2))
                        self.brick_piece.add(BrickPieceOverworld(collider.rect.right-16,collider.rect.bottom-16,5,-8,3))
                    elif collider.name == "underground":  
                        self.brick_piece.add(BrickPieceUnderground(collider.rect.x,collider.rect.y,-5,-12,0))
                        self.brick_piece.add(BrickPieceUnderground(collider.rect.right-16,collider.rect.y,5,-12,1))
                        self.brick_piece.add(BrickPieceUnderground(collider.rect.x,collider.rect.bottom-16,-5,-8,2))
                        self.brick_piece.add(BrickPieceUnderground(collider.rect.right-16,collider.rect.bottom-16,5,-8,3))
                else:
                    sound.bump.play()
                    if collider.state != c.OPENED:
                        collider.startBump()
                        self.check_if_ennemy_on_brick(collider)
                        if collider.content == "coin":
                            info.game_info["coin_count"] += 1
                            self.set_score("200",collider.rect.x,collider.rect.y)
                            info.game_info["scores"] += 200
                            sound.coin.play()
                        elif collider.content == "star":
                            sound.power_appear.play()
                        elif collider.content == "mushLife":
                            sound.power_appear.play()
            else:
                sound.bump.play()
                if collider.state != c.OPENED:
                    collider.startBump()
                    self.check_if_ennemy_on_brick(collider)
                    if collider.content == "coin":
                        info.game_info["coin_count"] += 1
                        self.set_score("200",collider.rect.x,collider.rect.y)
                        info.game_info["scores"] += 200
                        sound.coin.play()
                    elif collider.content == "star":
                        sound.power_appear.play()
                    elif collider.content == "mushLife":
                        sound.power_appear.play()
            
            player.vy = 3
            player.rect.top = collider.rect.bottom
            player.state = c.FALL
        
    def adjust_position_coin_brick(self,collider,player):
        if player.rect.bottom > collider.rect.top and player.rect.top < collider.rect.top:
            player.vy = 0
            player.rect.bottom = collider.rect.top
            player.state = c.WALK
            player.isjump = False

        elif player.rect.top < collider.rect.bottom and player.rect.bottom > collider.rect.bottom:
            if collider.state == c.RESTING:
                if collider.content == "coin":
                    info.game_info["coin_count"] += 1
                    info.game_info["scores"] += 200
                    self.set_score("200",collider.rect.x,collider.rect.y)
                    sound.coin.play()
                else:
                    sound.power_appear.play()
                
            else:
                sound.bump.play()
            if collider.state != c.OPENED:
                collider.startBump()
                self.check_if_ennemy_on_brick(collider)
            player.vy = 5
            player.rect.top = collider.rect.bottom
            player.state = c.FALL
    

    def check_if_ennemy_on_brick(self,brick):
        brick.rect.y -= 1
        hit_ennemy = pg.sprite.spritecollideany(brick,self.ennemy)
        if hit_ennemy:
            if hit_ennemy.name == "gumba":
                self.set_score("100",hit_ennemy.rect.x,hit_ennemy.rect.y)
                info.game_info["scores"] += 100
            elif hit_ennemy.name == "koopa":
                self.set_score("200",hit_ennemy.rect.x,hit_ennemy.rect.y)
                info.game_info["scores"] += 200
            elif hit_ennemy.name == "shell":
                self.set_score("200",hit_ennemy.rect.x,hit_ennemy.rect.y)
                info.game_info["scores"] += 200
            self.ennemy.remove(hit_ennemy)
            sound.kick.play()
            hit_ennemy.jumpToDeath()
            self.ennemy_death.add(hit_ennemy)
        brick.rect.y += 1

    def check_if_mario_is_falling(self,player):
        player.rect.y += 1
        group_collide = pg.sprite.Group(self.brick,self.ground_pipe_stair,self.coin_brick)

        if  pg.sprite.spritecollideany(player,group_collide) is None:
            if player.state != c.JUMP and player.state != c.TOSMALL and player.state != c.TORED and player.state != c.TOBIG and player.state != c.WAITFLAG and player.state != c.JUMPTODEATH and player.state != c.SLIDEFLAG and player.state != c.WALKTOCASTLE:
                player.state = c.FALL

        player.rect.y -= 1



######### POWER COLLISION #########

    def adjust_position_power(self):
        for m in self.power:
            if (m.name == "mush" or m.name == "mushLife") and m.state != c.POWER_SPAWN:
                self.power.remove(m)
                m.rect.x += round(m.vx)
                self.check_mush_collision_x(m)

                m.rect.y += round(m.vy)
                self.check_mush_collision_y(m)
                self.power.add(m)
            elif m.name == "star" and m.state != c.POWER_SPAWN:
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
            hit_brick,hit_coin_brick = self.prevent_error_collision(hit_brick,hit_coin_brick,star)

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
            hit_brick,hit_coin_brick = self.prevent_error_collision(hit_brick,hit_coin_brick,mush)

        if hit_ground_pipe_stair:
            self.adjust_position_power_y(mush,hit_ground_pipe_stair)
        elif hit_brick:
            self.adjust_position_power_y(mush,hit_brick)
        elif hit_coin_brick:
            self.adjust_position_power_y(mush,hit_coin_brick)

    def adjust_position_power_y(self,power,collider):
        if power.rect.bottom > collider.rect.top and power.rect.top < collider.rect.top:
            if power.name == "mush" or power.name == "mushLife":
                power.vy = 0
            elif power.name == "star":
                power.vy *= -1
            power.rect.bottom = collider.rect.top

        elif power.rect.top < collider.rect.bottom and power.rect.bottom > collider.rect.bottom:
            if power.name == "mush" or power.name == "mushLife":
                power.vy = 0
            elif power.name == "star":
                power.vy *= -1
            power.rect.top = collider.rect.bottom
            

######### ENNEMY COLLISION #########
    def adjust_position_ennemy(self):
        for e in self.ennemy:
            if e.name == "pirana":
                e.rect.x += e.vx
                e.rect.y += e.vy
            elif e.state != c.DEATH:
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
                    self.set_score("100",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy2.name == "koopa":
                    self.set_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy2.name == "shell":
                    self.set_score("200",ennemy2.rect.x,ennemy2.rect.y)
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
                    self.set_score("100",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy2.name == "koopa":
                    self.set_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy2.name == "shell":
                    self.set_score("200",ennemy2.rect.x,ennemy2.rect.y)
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
            hit_brick,hit_coin_brick = self.prevent_error_collision(hit_brick,hit_coin_brick,ennemy)

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
                    self.set_score("100",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy2.name == "koopa":
                    self.set_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy2.name == "shell":
                    self.set_score("200",ennemy2.rect.x,ennemy2.rect.y)
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
                    self.set_score("100",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy2.name == "koopa":
                    self.set_score("200",ennemy2.rect.x,ennemy2.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy2.name == "shell":
                    self.set_score("200",ennemy2.rect.x,ennemy2.rect.y)
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
        if self.multi:
             self.fireball = pg.sprite.Group(self.fireball_mario,self.fireball_mario)
        else:
            self.fireball = pg.sprite.Group(self.fireball_mario)
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
            self.set_score("100",ennemy.rect.x,ennemy.rect.y)
            info.game_info["scores"] += 100
        elif ennemy.name == "koopa":
            self.set_score("200",ennemy.rect.x,ennemy.rect.y)
            info.game_info["scores"] += 200
        elif ennemy.name == "shell":
            self.set_score("200",ennemy.rect.x,ennemy.rect.y)
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
            hit_brick,hit_coin_brick = self.prevent_error_collision(hit_brick,hit_coin_brick,fireball)

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
            self.set_score("100",ennemy.rect.x,ennemy.rect.y)
            info.game_info["scores"] += 100
        elif ennemy.name == "koopa":
            self.set_score("200",ennemy.rect.x,ennemy.rect.y)
            info.game_info["scores"] += 200
        elif ennemy.name == "shell":
            self.set_score("200",ennemy.rect.x,ennemy.rect.y)
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




