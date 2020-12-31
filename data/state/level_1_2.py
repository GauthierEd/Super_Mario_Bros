import pygame as pg
from . import state
from .. import setup
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

class Level_1_2(state.State):
    def __init__(self):
        state.State.__init__(self)
    
    def startup(self,current_time):
        self.collision = Collision(self)
        self.next = None
        self.state = c.CINEMATIC
        self.timeOut = False
        self.transition = False
        self.under = False
        self.overworld = False
        self.multi = info.game_info["multi"]
        self.current_update = current_time
        self.timeOut_timer = 0
        self.timeEnd_timer = 0
        self.under_timer = 0
        self.setup_everything()
        self.info = info.Info(c.LEVEL_1_1)
    
    def setup_background(self):
        self.background = pg.image.load("images/fond_lvl2.png").convert()
        self.back_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,(int(self.back_rect.width * c.BACKGROUND_SIZE_MULTIPLIER),int(self.back_rect.height * c.BACKGROUND_SIZE_MULTIPLIER)))
        self.back_rect = self.background.get_rect()
        width = self.back_rect.width
        height = self.back_rect.height

        self.level = pg.Surface((width,height)).convert()
        self.level_rect = self.level.get_rect()
        self.viewport = setup.SCREEN.get_rect(bottom = self.level_rect.bottom)
        self.viewport.x = 0 * c.BACKGROUND_SIZE_MULTIPLIER
    
    def setup_player(self):
        self.fireball_mario = pg.sprite.Group()
        self.fireball_luigi = pg.sprite.Group()

        self.player = pg.sprite.Group()
        self.mario = Mario(56*c.BACKGROUND_SIZE_MULTIPLIER,200*c.BACKGROUND_SIZE_MULTIPLIER,self.fireball_mario)
        self.mario.state = c.CINEMATIC
        self.player.add(self.mario)
        if info.game_info["multi"]:
            self.luigi = Luigi(45*c.BACKGROUND_SIZE_MULTIPLIER,200*c.BACKGROUND_SIZE_MULTIPLIER,self.fireball_luigi)
            self.luigi.state = c.CINEMATIC
            self.player.add(self.luigi)
    
    def setup_ground(self):
        ground_1 = Collider(0,200,1579,24)
        ground_2 = Collider(1627,200,592,24)
        ground_3 = Collider(2251,200,32,24)
        ground_4 = Collider(2315,200,192,24)
        ground_5 = Collider(2619,200,128,24)
        ground_6 = Collider(2859,200,1419,24)

        self.ground = pg.sprite.Group(ground_1,ground_2,ground_3,ground_4,ground_5,ground_6)
    
    def setup_pipe(self):
        pipe_1 = Pipe(1947,152,32,48)
        pipe_2 = Pipe(2043,136,32,64)
        pipe_3 = Pipe(2136,168,32,32)
        pipe_4 = Pipe(3147,152,32,48)
        pipe_5 = Pipe(3211,152,32,48)
        pipe_6 = Pipe(3275,152,32,48)
        pipe_7 = Pipe(3419,168,32,32)
        pipe_8 = Collider(2955,120,34,32)
        pipe_9 = Collider(2989,24,28,128)
        pipe_10 = Collider(4222,168,40,32)
        pipe_11 = Collider(4262,24,16,176)

        self.pipe = pg.sprite.Group(pipe_1,pipe_2,pipe_3,pipe_4,pipe_5,pipe_6,pipe_7,pipe_8,pipe_9,pipe_10,pipe_11)
    
    def setup_stair(self):
        stair_1 = Collider(571,184,16,16)
        stair_2 = Collider(603,168,16,32)
        stair_3 = Collider(635,152,16,48)
        stair_4 = Collider(667,136,16,64)
        stair_5 = Collider(699,136,16,64)
        stair_6 = Collider(731,152,16,48)
        stair_7 = Collider(795,152,16,48)
        stair_8 = Collider(827,168,16,32)

        stair_9 = Collider(2427,184,16,16)
        stair_10 = Collider(2443,168,16,16)
        stair_11 = Collider(2459,152,16,16)
        stair_12 = Collider(2475,136,16,16)
        stair_13 = Collider(2491,136,16,64)

        stair_14 = Collider(3451,184,16,16)
        stair_15 = Collider(3467,168,16,16)
        stair_16 = Collider(3483,152,16,16)
        stair_17 = Collider(3499,136,16,16)
        stair_18 = Collider(3515,120,16,16)
        stair_19 = Collider(3531,104,16,16)
        stair_20 = Collider(3547,88,16,16)
        stair_21 = Collider(3563,72,16,16)
        stair_22 = Collider(3579,72,16,128)

        stair_23 = Collider(3723,184,16,16)

        self.stair = pg.sprite.Group(stair_1,stair_2,stair_3,stair_4,stair_5,stair_6,stair_7,stair_8,stair_9,stair_10,stair_11,
                                        stair_12,stair_13,stair_14,stair_15,stair_16,stair_17,stair_18,stair_19,stair_20,stair_21,
                                        stair_22,stair_23)
    
    def setup_brick(self):
        self.brick_piece = pg.sprite.Group()
        self.coin = pg.sprite.Group()
        self.brick = pg.sprite.Group()
        self.score = []
        self.score_timer = []

        for i in range(11):
            brick = BrickUnderground(299,24 + (i*16))
            self.brick.add(brick)

        for i in range(83):
            brick = BrickUnderground(395+(16*i),24)
            self.brick.add(brick)
        for i in range(48):
            brick = BrickUnderground(1739+(16*i),24)
            self.brick.add(brick)
        
        brick_26 = BrickUnderground(1723,24,self.power,"mushLife")

        brick_1 = BrickUnderground(763,120,self.coin,"coin")
        brick_2 = BrickUnderground(923,104)
        brick_3 = BrickUnderground(923,120)
        brick_4 = BrickUnderground(923,136)
        brick_5 = BrickUnderground(939,136)
        brick_6 = BrickUnderground(955,104)
        brick_7 = BrickUnderground(955,120)
        brick_8 = BrickUnderground(955,136)
        brick_9 = BrickUnderground(971,104)
        brick_10 = BrickUnderground(987,104)
        brick_11 = BrickUnderground(1003,104)
        brick_12 = BrickUnderground(1003,120)
        brick_13 = BrickUnderground(1003,136)
        brick_14 = BrickUnderground(1019,136)
        brick_15 = BrickUnderground(1035,104,self.power,"star")
        brick_16 = BrickUnderground(1035,120)
        brick_17 = BrickUnderground(1035,136)

        brick_18 = BrickUnderground(1163,40)
        brick_19 = BrickUnderground(1163,56)
        brick_20 = BrickUnderground(1179,40)
        brick_21 = BrickUnderground(1179,56)


        for i in range(5):
            for j in range(2):
                brick = BrickUnderground(1131 + (j*16),72+(i*16))
                self.brick.add(brick)  
        for i in range(3):
            for j in range(2):
                brick = BrickUnderground(1163 + (j*16),136+(i*16))
                self.brick.add(brick)
        for i in range(6):
            for j in range(2):
                brick = BrickUnderground(1227 + (j*16),40+(i*16))
                self.brick.add(brick)
        for i in range(5):
            for j in range(2):
                brick = BrickUnderground(1291 + (j*16),72+(i*16))
                self.brick.add(brick)
        for i in range(4):
            brick = BrickUnderground(1227+(i*16),136)
            self.brick.add(brick)
        for i in range(4):
            for j in range(2):
                brick = BrickUnderground(1355 + (j*16),40+(i*16))
                self.brick.add(brick)
        for i in range(5):
            brick = BrickUnderground(1371,72+(i*16))
            self.brick.add(brick)
        
        brick_22 = BrickUnderground(1387,136)
        brick_23 = BrickUnderground(1403,136)
        brick_24 = BrickUnderground(1403,120,self.power,"mush")

        for i in range(5):
            for j in range(2):
                brick = BrickUnderground(1451 + (j*16),72+(i*16))
                self.brick.add(brick) 
        for i in range(2):
            for j in range(4):
                if i == 1 and j == 3:
                    brick = BrickUnderground(1515+(j*16),40+(i*16),self.coin,"coin")
                else:
                    brick = BrickUnderground(1515 + (j*16),40+(i*16))
                self.brick.add(brick)
        for i in range(4):
            brick = BrickUnderground(1515+(i*16),136)
            self.brick.add(brick)
        for i in range(2):
            for j in range(6):
                brick = BrickUnderground(1643 + (j*16),104+(i*16))
                self.brick.add(brick)
        for i in range(4):
            for j in range(2):
                brick = BrickUnderground(2251 + (j*16),152+(i*16))
                self.brick.add(brick)
        for i in range(5):
            brick = BrickUnderground(2619+(i*16),120)
            self.brick.add(brick)
        brick_25 = BrickUnderground(2699,120,self.power,"mush")
        for i in range(7):
            brick = BrickUnderground(2875+(i*16),24)
            self.brick.add(brick)
        for i in range(3):
            for j in range(17):
                brick = BrickUnderground(2859 + (j*16),152+(i*16))
                self.brick.add(brick)
        for i in range(8):
            for j in range(7):
                brick = BrickUnderground(3019 + (j*16),24+(i*16))
                self.brick.add(brick)
        for i in range(10):
            brick = BrickUnderground(3131+(i*16),24)
            self.brick.add(brick)
        for i in range(11):
            for j in range(2):
                brick = BrickUnderground(3339 + (j*16),24+(i*16))
                self.brick.add(brick)
        for i in range(11):
            brick = BrickUnderground(3979,24+(i*16))
            self.brick.add(brick)
        for i in range(4):
            for j in range(12):
                brick = BrickUnderground(4035 + (j*16),24+(i*16))
                self.brick.add(brick)
        for i in range(9):
            for j in range(2):
                brick = BrickUnderground(4227 + (j*16),24+(i*16))
                self.brick.add(brick)
        for i in range(11):
            brick = BrickUnderground(4035+(i*16),136)
            self.brick.add(brick)
        brick_27 = BrickUnderground(4211,136,self.coin,"coin")
        
        
        self.brick.add(brick_1,brick_2,brick_3,brick_4,brick_5,brick_6,brick_7,brick_8,brick_9,brick_10,brick_11,brick_12,brick_13,
                        brick_14,brick_15,brick_16,brick_17,brick_18,brick_19,brick_20,brick_21,brick_22,brick_23,brick_24,brick_25,brick_26,brick_27)

    def setup_coin_brick(self):
        coin_brick_1 = CoinBrickUnderground(459,136,self.power,"mush")
        coin_brick_2 = CoinBrickUnderground(475,136,self.coin,"coin")
        coin_brick_3 = CoinBrickUnderground(491,136,self.coin,"coin")
        coin_brick_4 = CoinBrickUnderground(507,136,self.coin,"coin")
        coin_brick_5 = CoinBrickUnderground(523,136,self.coin,"coin")

        self.coin_brick = pg.sprite.Group(coin_brick_1,coin_brick_2,coin_brick_3,coin_brick_4,coin_brick_5)
    
    def setup_power(self):
        self.power = pg.sprite.Group()
    
    def setup_coin(self):
        coin_1 = BigCoin(943,120)
        coin_2 = BigCoin(1023,120)
        coin_3 = BigCoin(958,84)
        coin_4 = BigCoin(974,84)
        coin_5 = BigCoin(990,84)
        coin_6 = BigCoin(1006,84)
        coin_7 = BigCoin(1230,121)
        coin_8 = BigCoin(1246,121)
        coin_9 = BigCoin(1262,121)
        coin_10 = BigCoin(1278,121)
        coin_11 = BigCoin(1391,121)

        coin_12 = BigCoin(1646,84)
        coin_13 = BigCoin(1662,84)
        coin_14 = BigCoin(1678,84)
        coin_15 = BigCoin(1694,84)
        coin_16 = BigCoin(1710,84)
        coin_17 = BigCoin(1726,84)

        coin_18 = BigCoin(4054,121)
        coin_19 = BigCoin(4070,121)
        coin_20 = BigCoin(4086,121)
        coin_21 = BigCoin(4102,121)
        coin_22 = BigCoin(4118,121)
        coin_23 = BigCoin(4134,121)
        coin_24 = BigCoin(4150,121)
        coin_25 = BigCoin(4166,121)

        coin_26 = BigCoin(4038,185)
        coin_27 = BigCoin(4054,185)
        coin_28 = BigCoin(4070,185)
        coin_29 = BigCoin(4086,185)
        coin_30 = BigCoin(4102,185)
        coin_31 = BigCoin(4118,185)
        coin_32 = BigCoin(4134,185)
        coin_33 = BigCoin(4150,185)
        coin_34 = BigCoin(4166,185)
        
        self.bigCoin = pg.sprite.Group(coin_1,coin_2,coin_3,coin_4,coin_5,coin_6,coin_7,coin_8,coin_9,coin_10,
                                        coin_11,coin_12,coin_13,coin_14,coin_15,coin_16,coin_17,coin_18,coin_19,coin_20,coin_21,coin_22,coin_23,
                                        coin_24,coin_25,coin_26,coin_27,coin_28,coin_29,coin_30,coin_31,coin_32,coin_33,coin_34)

    def setup_lift(self):
        lift_1 = Lift(2535,200,-1)
        lift_2 = Lift(2535,100,-1)
        lift_3 = Lift(2535,10,-1)

        lift_4 = Lift(2775,200,-1)
        lift_5 = Lift(2775,100,-1)
        lift_6 = Lift(2775,10,-1)
        self.lift = pg.sprite.Group(lift_1,lift_2,lift_3,lift_4,lift_5,lift_6)

    def setup_ennemy(self):
        self.ennemy = pg.sprite.Group()
        self.ennemy_death = pg.sprite.Group()

    def setup_checkpoint(self):
        check_1 = checkPoint(1947,150,32,50,"pipe")
        check_2 = checkPoint(4221,168,1,32,"pipe2")
        check_3 = checkPoint(2954,120,1,32,"pipe3")
        self.checkpoint = pg.sprite.Group(check_1,check_2,check_3)

    def setup_everything(self):
        self.setup_background()
        self.setup_player()
        self.setup_ground()
        self.setup_pipe()
        self.setup_stair()
        self.setup_power()
        self.setup_coin()
        self.setup_brick()
        self.setup_coin_brick()
        self.setup_lift()
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
        elif self.state == c.CINEMATIC:
            self.update_while_cinematic(keys)
    
    def draw_everything(self,screen):
        self.level.blit(self.background, self.viewport,self.viewport)
        #self.level.blit(self.flag.image,self.flag.rect)
        if self.state != c.INCASTLE:
            for player in self.player:
                self.level.blit(player.image,player.rect)
        """if self.flagEnd.rect.top < 121 * c.BACKGROUND_SIZE_MULTIPLIER:
            self.level.blit(self.flagEnd.image,self.flagEnd.rect)"""
        self.ground.draw(self.level)
        self.pipe.draw(self.level)
        self.bigCoin.draw(self.level)
        self.power.draw(self.level)
        self.brick.draw(self.level)
        self.lift.draw(self.level)
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
    
    def update_while_cinematic(self,keys):
        for player in self.player:
            player.update(keys)
            if player.rect.right > 184 * c.BACKGROUND_SIZE_MULTIPLIER:
                self.transition = True
        self.adjust_position_player()
        self.info.update(self.current_update,self.mario.state)
        self.check_if_transition()

    def update_all_sprites(self,keys):
        for player in self.player:
            player.update(keys)
        self.brick.update()
        self.brick_piece.update()
        self.coin_brick.update(self.current_update)
        self.coin.update(self.current_update)
        self.bigCoin.update(self.current_update)
        self.power.update(self.current_update)
        self.lift.update()
        self.ennemy.update()
        self.ennemy_death.update()
        if self.multi:
            self.fireball = pg.sprite.Group(self.fireball_mario,self.fireball_luigi)
        else:
            self.fireball = pg.sprite.Group(self.fireball_mario)
        self.fireball.update()
        #self.flag.update()
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
        """self.flagEnd.update()
        if int(info.game_info["time"]) == 0 and self.flagEnd.rect.bottom > (121*c.BACKGROUND_SIZE_MULTIPLIER):
            self.flagEnd.state = c.SLIDEFLAG
        
        if self.flagEnd.rect.bottom <= 121 *c.BACKGROUND_SIZE_MULTIPLIER:
            if self.timeEnd_timer == 0:
                self.timeEnd_timer = self.current_update
            elif self.current_update - self.timeEnd_timer > 3000:
                self.done = True
                self.next = c.MAIN_MENU"""
        
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
                if self.state == c.CINEMATIC:
                    pass
                else:
                    self.under = not self.under
                self.under_timer = self.current_update
            elif self.current_update - self.under_timer > 1000:
                self.under_timer = 0
                if self.state == c.CINEMATIC:
                    self.set_in_level()
                else:
                    if self.under:
                        self.set_in_underground()
                    elif not self.under:
                        self.set_in_underground_level()
                    
                    if self.overworld:
                        self.set_in_overworld()
                self.state = c.NOTFREEZE
                self.transition = False

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
            elif player.canGoOverworld and self.overworld:
                self.state = c.FREEZE  
                self.transition = True
            else:
                self.state = c.NOTFREEZE
    
    def set_in_level(self):
        self.viewport.x = 299 * c.BACKGROUND_SIZE_MULTIPLIER
        y = 0
        for player in self.player:
            player.state = c.STAND
            player.vx = 0
            player.vy = 0
            player.rect.x = 340 * c.BACKGROUND_SIZE_MULTIPLIER
            player.rect.y = (40 - y) * c.BACKGROUND_SIZE_MULTIPLIER
            y -= 20

    def set_in_overworld(self):
        self.viewport.x = 3371 * c.BACKGROUND_SIZE_MULTIPLIER
        x = 0
        for player in self.player:
            player.rect.centerx = (3436 + x) * c.BACKGROUND_SIZE_MULTIPLIER
            player.rect.bottom = 168 * c.BACKGROUND_SIZE_MULTIPLIER
            x -= 8

    def set_in_underground(self):
        self.viewport.x = 3980 * c.BACKGROUND_SIZE_MULTIPLIER
        y = 0
        for player in self.player:
            player.rect.x = 4005 * c.BACKGROUND_SIZE_MULTIPLIER
            player.rect.y = (40 - y) * c.BACKGROUND_SIZE_MULTIPLIER
            y -= 20

    def set_in_underground_level(self):
        self.viewport.x = 2006 * c.BACKGROUND_SIZE_MULTIPLIER
        x = 0
        for player in self.player:
            player.rect.centerx = (2155 + x) * c.BACKGROUND_SIZE_MULTIPLIER
            player.rect.bottom = 168 * c.BACKGROUND_SIZE_MULTIPLIER
            x -= 8
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
        if self.viewport.x >= int(299 * c.BACKGROUND_SIZE_MULTIPLIER) and self.viewport.x < 3678 * c.BACKGROUND_SIZE_MULTIPLIER:
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
        group_collide = pg.sprite.Group(self.brick,self.ground_pipe_stair,self.coin_brick,self.lift)

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