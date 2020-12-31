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
from .. components.collision import *
from . import state
from .. import setup

class Level_1_1(state.State):
    def __init__(self):
        state.State.__init__(self)
        
    def startup(self,current_time):
        self.collision = Collision(self)
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
        self.info = info.Info(c.LEVEL_1_1)

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

        self.player = pg.sprite.Group()
        self.mario = Mario(100,c.GROUND_HEIGHT,self.fireball_mario)
        self.player.add(self.mario)
        if info.game_info["multi"]:
            self.luigi = Luigi(50,c.GROUND_HEIGHT,self.fireball_luigi)
            self.player.add(self.luigi)

    def setup_ground(self):
        ground_1 = Collider(0,200,1104,24)
        ground_2 = Collider(1136,200,240,24)
        ground_3 = Collider(1424,200,1024,24)
        ground_4 = Collider(2480,200,912,24)
        ground_5 = Collider(3392,200,256,24)

        self.ground = pg.sprite.Group(ground_1,ground_2,ground_3,ground_4,ground_5)

    def setup_pipe(self):
        pipe_1 = Pipe(448,168,32,32)
        pipe_2 = Pipe(608,152,32,48)
        pipe_3 = Pipe(736,136,32,64)
        pipe_4 = Pipe(912,136,32,64)
        pipe_5 = Pipe(2608,168,32,32)
        pipe_6 = Pipe(2864,168,32,32)
        pipe_7 = Collider(3635,168,40,32)
        pipe_8 = Collider(3675,24,16,176)

        self.pipe = pg.sprite.Group(pipe_1,pipe_2,pipe_3,pipe_4,pipe_5,pipe_6,pipe_7,pipe_8)

    def setup_stair(self):
        stair_1 = Collider(2144,184,16,16)
        stair_2 = Collider(2160,168,16,16)
        stair_3 = Collider(2176,152,16,16)
        stair_4 = Collider(2192,136,16,64)

        stair_5 = Collider(2240,136,16,64)
        stair_6 = Collider(2256,152,16,16)
        stair_7 = Collider(2272,168,16,16)
        stair_8 = Collider(2288,184,16,16)

        stair_9 = Collider(2368,184,16,16)
        stair_10 = Collider(2384,168,16,16)
        stair_11 = Collider(2400,152,16,16)
        stair_12 = Collider(2416,136,32,64)
        
        stair_13 = Collider(2480,136,16,64)
        stair_14 = Collider(2496,152,16,16)
        stair_15 = Collider(2512,168,16,16)
        stair_16 = Collider(2528,184,16,16)

        stair_17 = Collider(2896,184,16,16)
        stair_18 = Collider(2912,168,16,16)
        stair_19 = Collider(2928,152,16,16)
        stair_20 = Collider(2944,136,16,16)
        stair_21 = Collider(2960,120,16,16)
        stair_22 = Collider(2979,104,16,16)
        stair_23 = Collider(2992,88,16,16)
        stair_24 = Collider(3008,72,32,128)

        bottom_flag = Collider(3168,184,16,16)

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
        e1 = GumbaOverworld(352,184, -1)

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


        e9 = KoopaOverworld(1715,176,-1)
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
        check1 = checkPoint(470,0,1,224,"1")
        check2 = checkPoint(600,0,1,224,"2")
        check3 = checkPoint(1100,0,1,224,"3")
        check4 = checkPoint(1400,0,1,224,"4")
        check5 = checkPoint(1530,0,1,224,"5")
        check6 = checkPoint(1830,0,1,224,"6")
        check7 = checkPoint(2630,0,1,224,"7")
        check8 = checkPoint(3178,32,2,152,"8")
        check9 = checkPoint(912,130,32,70,"pipe")
        check10 = checkPoint(3634,168,1,32,"pipe2")
        check11 = checkPoint(3168,184,7,16,"9")
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
        if self.state != c.INCASTLE:
            for player in self.player:
                self.level.blit(player.image,player.rect)
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
            self.fireball = pg.sprite.Group(self.fireball_mario,self.fireball_luigi)
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
        for player in self.player:
            player.update(keys)
        self.brick.update()
        self.brick_piece.update()
        self.coin_brick.update(self.current_update)
        self.coin.update(self.current_update)
        self.bigCoin.update(self.current_update)
        self.power.update(self.current_update)
        self.ennemy.update()
        self.ennemy_death.update()
        if self.multi:
            self.fireball = pg.sprite.Group(self.fireball_mario,self.fireball_luigi)
        else:
            self.fireball = pg.sprite.Group(self.fireball_mario)
        self.fireball.update()
        self.checkpoint.update()
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
        self.coin_brick.update(self.current_update)
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
        for player in self.player:
            player.update(keys)
        self.coin_brick.update(self.current_update)
        self.coin.update(self.current_update)
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
        if int(info.game_info["time"]) == 0:
            for player in self.player:
                if not player.dead:
                    player.vy = -8
                    player.state = c.JUMPTODEATH
            sound.main.stop()


    def check_if_change_state(self):
        for player in self.player:
            if player.rect.y > c.HEIGHT:
                player.dead = True
            if player.dead and player.test_when_die:
                if player.name == "mario":
                    self.play_die_song_mario()
                elif player.name == "luigi":
                    self.play_die_song_luigi()

    def play_die_song_mario(self):
        if self.mario.death_timer == 0:
            if not self.multi:
                sound.main.stop()
                sound.die.play()
            else:
                if self.luigi.dead:
                    sound.main.stop()
                    sound.die.play()
            self.mario.death_timer = self.current_update
        elif (self.current_update - self.mario.death_timer)>3000:
            if self.multi:
                if self.luigi.dead:
                    self.done = True
            else:
                self.done = True
            self.set_game_info()
            self.mario.test_when_die = False
            self.player.remove(self.mario)

    def play_die_song_luigi(self):
        if self.luigi.death_timer == 0:
            if not self.multi:
                sound.main.stop()
                sound.die.play()
            else:
                if self.mario.dead:
                    sound.main.stop()
                    sound.die.play()
            self.luigi.death_timer = self.current_update
        elif (self.current_update - self.luigi.death_timer)>3000:
            if self.multi:
                if self.mario.dead:
                    self.done = True
            else:
                self.done = True
            self.set_game_info()
            self.luigi.test_when_die = False
            self.player.remove(self.luigi)

    def set_game_info(self):
        if int(info.game_info["time"]) == 0:
            self.next = c.TIMEOUT
            for player in self.player:
                info.game_info[player.name+"_lifes"] -= 1

        for player in self.player:
            if player.dead and player.test_when_die:
                self.next = c.LOAD
                info.game_info[player.name+"_lifes"] -= 1

        if info.game_info["multi"]:
            if info.game_info["mario_lifes"] == 0 and info.game_info["luigi_lifes"] == 0:
                self.next = c.GAMEOVER
                self.done = True
        else:
            if info.game_info["mario_lifes"] == 0:
                self.next = c.GAMEOVER
                self.done = True   

    def check_if_mario_in_transition(self):
        for player in self.player:
            if player.transform:
                self.state = c.FREEZE
            elif player.inCastle:
                self.state = c.INCASTLE
                sound.count_time.play()
            elif player.inUnder and not self.under:
                self.state = c.FREEZE
                self.transition = True
            elif player.canGoOverworld and self.under:
                self.state = c.FREEZE
                self.transition = True
            else:
                self.state = c.NOTFREEZE

    def set_in_underground(self):
        self.viewport.x = 3392 * c.BACKGROUND_SIZE_MULTIPLIER
        y = 0
        for player in self.player:
            player.rect.x = 3425 * c.BACKGROUND_SIZE_MULTIPLIER
            player.rect.y = (y + 40) * c.BACKGROUND_SIZE_MULTIPLIER
            y -= 20

    
    def set_in_overworld(self):
        self.viewport.x = 2476 * c.BACKGROUND_SIZE_MULTIPLIER
        x = 0
        for player in self.player:
            player.inUnder = False
            player.vx = 0
            player.rect.bottom = 168 * c.BACKGROUND_SIZE_MULTIPLIER
            player.rect.centerx = (x + 2625) * c.BACKGROUND_SIZE_MULTIPLIER
            x -= 7
        
######### SCORE  #########

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
                

######### UPDATE VIEWPORT #########

    def update_viewport(self):
        if self.viewport.x < 3092 * c.BACKGROUND_SIZE_MULTIPLIER:
            for player in self.player:
                third = self.viewport.x + self.viewport.w / 3
                player_center = player.rect.centerx
                player_right = player.rect.right
                if player.vx > 0 and player_center >= third:
                    if player_right < self.viewport.centerx:
                        mult = 0.5
                    else:
                        mult = 1
                    new = self.viewport.x + mult * player.vx
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

######### PLAYER COLLISION #########

    def adjust_position_player(self):
        for player in self.player:
            player.rect.x += round(player.vx)
            if not player.state == c.JUMPTODEATH:
                player.canGoUnder = False
                player.canGoOverworld = False
                self.collision.check_mario_x_collision(player)

            player.rect.y += round(player.vy)
            if not player.state == c.JUMPTODEATH and player.transform == False:
                self.collision.check_mario_y_collision(player)
                self.check_if_mario_is_falling(player)

    def check_if_mario_is_falling(self,player):
        player.rect.y += 1
        group_collide = pg.sprite.Group(self.brick,self.ground_pipe_stair,self.coin_brick)

        if  pg.sprite.spritecollideany(player,group_collide) is None:
            if player.state != c.JUMP and player.state != c.TOSMALL and player.state != c.TORED and player.state != c.TOBIG and player.state != c.WAITFLAG and player.state != c.JUMPTODEATH and player.state != c.SLIDEFLAG and player.state != c.WALKTOCASTLE:
                player.state = c.FALL

        player.rect.y -= 1
    
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

    


######### POWER COLLISION #########

    def adjust_position_power(self):
        for m in self.power:
            if m.state != c.POWER_SPAWN:
                self.power.remove(m)
                m.rect.x += round(m.vx)
                self.collision.check_power_collision_x(m)
                m.rect.y += round(m.vy)
                self.collision.check_power_collision_y(m)
                self.power.add(m)

######### ENNEMY COLLISION #########

    def adjust_position_ennemy(self):
        for e in self.ennemy:
            if e.name == "pirana":
                e.rect.x += round(e.vx)
                e.rect.y += round(e.vy)
            elif e.state != c.DEATH:
                self.ennemy.remove(e)
                e.rect.x += round(e.vx)
                self.collision.check_ennemy_collision_x(e)
                e.rect.y += round(e.vy)
                self.collision.check_ennemy_collision_y(e)
                self.ennemy.add(e)

######### FIREBALL COLLISION ###########

    def adjust_position_fireball(self):
        for b in self.fireball:
            b.rect.x += round(b.vx)
            self.collision.check_fireball_collision_x(b)
            b.rect.y += round(b.vy)
            self.collision.check_fireball_collision_y(b)