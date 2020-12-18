import pygame as pg
from pygame.locals import *
from .. import constante as c 
from . import mario
from .. import sound
from .coin import flash_coin

game_info = {
    "coin_count" : 0,
    "mario_lifes" : 3,
    "luigi_lifes" : 3,
    "time" : 401,
    "scores": 0,
    "multi": False,
}


class Character(pg.sprite.Sprite):
    def __init__(self,image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        

class Info(object):
    def __init__(self,state):
        self.sprite = pg.image.load("images/sprite_text.png")
        self.setup_letter()
        self.state = state
        self.setup_main_menu()
        self.setup_info()
        self.setup_count_coin()
        self.setup_mario_life()
        self.setup_mario()
        self.setup_luigi()
        self.setup_luigi_life()
        self.setup_load_world()
        self.setup_gameover()
        self.setup_timeout()
        self.setup_timer()
        self.setup_score()

    def setup_letter(self):
        self.character = []
        self.list_of_character = {}

        self.character.append(self.getImage(3,460,7,7)) # 0
        self.character.append(self.getImage(12,460,7,7)) # 1
        self.character.append(self.getImage(19,460,7,7)) # 2
        self.character.append(self.getImage(27,460,7,7)) # 3
        self.character.append(self.getImage(35,460,7,7)) # 4
        self.character.append(self.getImage(43,460,7,7)) # 5
        self.character.append(self.getImage(51,460,7,7)) # 6
        self.character.append(self.getImage(59,460,7,7)) # 7
        self.character.append(self.getImage(67,460,7,7)) # 8 
        self.character.append(self.getImage(75,460,7,7)) # 9
        self.character.append(self.getImage(83,460,7,7)) # A  
        self.character.append(self.getImage(91,460,7,7)) # B
        self.character.append(self.getImage(99,460,7,7)) # C
        self.character.append(self.getImage(107,460,7,7)) # D
        self.character.append(self.getImage(115,460,7,7)) # E
        self.character.append(self.getImage(123,460,7,7)) # F
        self.character.append(self.getImage(3,468,7,7)) # G
        self.character.append(self.getImage(11,468,7,7)) # H
        self.character.append(self.getImage(20,468,7,7)) # I
        self.character.append(self.getImage(27,468,7,7)) # J
        self.character.append(self.getImage(35,468,7,7)) # K
        self.character.append(self.getImage(43,468,7,7)) # L
        self.character.append(self.getImage(51,468,7,7)) # M
        self.character.append(self.getImage(59,468,7,7)) # N
        self.character.append(self.getImage(67,468,7,7)) # O
        self.character.append(self.getImage(75,468,7,7)) # P
        self.character.append(self.getImage(83,468,7,7)) # Q
        self.character.append(self.getImage(91,468,7,7)) # R
        self.character.append(self.getImage(99,468,7,7)) # S
        self.character.append(self.getImage(107,468,7,7)) # T
        self.character.append(self.getImage(115,468,7,7)) # U
        self.character.append(self.getImage(123,468,7,7)) # V
        self.character.append(self.getImage(3,476,7,7)) # W
        self.character.append(self.getImage(11,476,7,7)) # X
        self.character.append(self.getImage(20,476,7,7)) # Y
        self.character.append(self.getImage(27,476,7,7)) # Z
        self.character.append(self.getImage(58,477,7,7)) # 
        self.character.append(self.getImage(68,477,7,7)) # - 
        self.character.append(self.getImage(75,477,7,7)) # x

        character_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*"
        
        for char,image in zip(character_string,self.character):
            self.list_of_character[char] = image

    def getImage(self,x,y,w,h):
        image = pg.Surface((w,h))
        image.blit(self.sprite,(0,0),(x,y,w,h))
        image.set_colorkey((92,148,252))
        image = pg.transform.scale(image,(int(w* 3.4),int(h* 3.4)))
        return image

    def create_sentence(self,list_char,string,x,y):
        for char in string:
            list_char.append(Character(self.list_of_character[char]))

        for i,char in enumerate(list_char):
            char.rect.y = y
            char.rect.x = x + (char.rect.width + 3) * i
    
    def setup_info(self):
        world = []
        level = []
        time = []
        
        self.create_sentence(world,"WORLD",450,30)
        self.create_sentence(level,"1-1",480,60)
        self.create_sentence(time,"TIME",650,30)

        self.info = [world,level,time]

    def setup_mario(self):
        self.mario_word = []
        self.create_sentence(self.mario_word,"MARIO",60,30)
    
    def setup_luigi(self):
        self.luigi_word = []
        self.create_sentence(self.luigi_word,"LUIGI",60,30)

    def setup_load_world(self):
        self.load_world = []
        self.create_sentence(self.load_world,"WORLD 1-1",270,220)

    def setup_mario_life(self):
        self.mario_life = []
        self.create_sentence(self.mario_life,"*   " + str(game_info["mario_lifes"]),350,300)
        self.mario = mario.Mario(280,325)

    def setup_luigi_life(self):
        self.luigi_life = []
        self.create_sentence(self.luigi_life,"*  " + str(game_info["luigi_lifes"]),350,300)
        self.luigi = mario.Luigi(280,325)

    def setup_gameover(self):
        self.gameover = []
        self.create_sentence(self.gameover,"GAME OVER",270,250)

    def setup_timeout(self):
        self.timeout = []
        self.create_sentence(self.timeout,"TIME UP",270,250)

    def setup_score(self):
        self.score = []
        score = str(game_info["scores"])
        if len(score) == 1:
            score = "00000"+score
        elif len(score) == 2:
            score = "0000"+score
        elif len(score) == 3:
            score = "000"+score
        elif len(score) == 4:
            score = "00"+score
        elif len(score) == 5:
            score = "0"+score
       
        self.create_sentence(self.score,score,60,60)

    def create_score(self,string,x,y):
        score = []
        self.create_sentence(score,string,x,y)
        return score
    
    

    def setup_timer(self):
        self.timer = []
        time = int(game_info["time"])
        time_count = str(time)
        if len(time_count) == 3:
            time = time_count
        elif len(time_count) == 2:
            time = "0"+time_count
        elif len(time_count) == 1:
            time = "00"+time_count
        self.create_sentence(self.timer,time,670,60)

    def setup_count_coin(self):
        count_coin = str(game_info["coin_count"])

        if len(count_coin) == 1:
            coin = "*0" + count_coin
        elif len(count_coin) == 2:
            coin = "*" + count_coin
        else:
            coin = "*00"
        
        self.coin_total =  []
        self.create_sentence(self.coin_total,coin,270,60)
        self.flash_coin = flash_coin()

    def setup_main_menu(self):
        player1 = []
        player2 = []
        self.create_sentence(player1,"1 PLAYER GAME",300,380)
        self.create_sentence(player2,"2 PLAYER GAME",300,430)

        self.main_menu = [player1,player2]

    def update(self,current_time,state = None):
        if self.state == c.MAIN_MENU:
            self.flash_coin.update()
            self.setup_count_coin()
        elif self.state == c.LEVEL:
            self.timeUpdate(current_time,state)
            self.setup_timer()
            self.setup_score()
            self.setup_count_coin()
            self.update_coin()
            self.flash_coin.update()
        elif self.state == c.LOAD:
            self.flash_coin.update()
        elif self.state == c.GAMEOVER:
            self.flash_coin.update()
        elif self.state == c.TIMEOUT:
            self.flash_coin.update()
    
    def timeUpdate(self,current_time,state):
        if state != c.SLIDEFLAG and state != c.WAITFLAG and state != c.WALKTOCASTLE and int(game_info["time"] >= 0):
            game_info["time"] -= 1/c.FPS

    def update_coin(self):
        if game_info["coin_count"] == 100:
            sound.up.play()
            game_info["coin_count"] = 0
            game_info["mario_lifes"] += 1
            if game_info["multi"]:
                game_info["luigi_lifes"] += 1

    def end_score(self):
        if game_info["time"] > 0:
            game_info["time"] -= 1
            game_info["scores"] += 50
        else:
            sound.count_time.stop()

    def draw(self,screen):
        if self.state == c.MAIN_MENU:
            self.draw_main_menu(screen)
        elif self.state == c.LEVEL:
            self.draw_level(screen)
        elif self.state == c.GAMEOVER:
            self.draw_gameover(screen)
        elif self.state == c.TIMEOUT:
            self.draw_timeout(screen)

    def draw_timeout(self,screen):
        for text in self.info:
            for char in text:
                screen.blit(char.image,char.rect)

        for char in self.mario_word:
            screen.blit(char.image,char.rect)

        for char in self.coin_total:
            screen.blit(char.image,char.rect)
            
        for char in self.timeout:
            screen.blit(char.image,char.rect)

        for char in self.timer:
            screen.blit(char.image,char.rect)
        
        for char in self.score:
            screen.blit(char.image,char.rect)

        screen.blit(self.flash_coin.image,self.flash_coin.rect)

    def draw_gameover(self,screen):
        for text in self.info:
            for char in text:
                screen.blit(char.image,char.rect)
        
        for char in self.mario_word:
            screen.blit(char.image,char.rect)

        for char in self.coin_total:
            screen.blit(char.image,char.rect)
            
        for char in self.gameover:
            screen.blit(char.image,char.rect)
        
        for char in self.score:
            screen.blit(char.image,char.rect)

        screen.blit(self.flash_coin.image,self.flash_coin.rect)

    def draw_main_menu(self,screen):
        for text in self.main_menu:
            for char in text:
                screen.blit(char.image,char.rect)
            
        for text in self.info:
            for char in text:
                screen.blit(char.image,char.rect)
        
        for char in self.mario_word:
            screen.blit(char.image,char.rect)

        for char in self.coin_total:
            screen.blit(char.image,char.rect)
            
        screen.blit(self.flash_coin.image,self.flash_coin.rect)

    def draw_level(self,screen):
        for text in self.info:
            for char in text:
                screen.blit(char.image,char.rect)
        
        for char in self.mario_word:
            screen.blit(char.image,char.rect)

        for char in self.coin_total:
            screen.blit(char.image,char.rect)
        
        for char in self.timer:
            screen.blit(char.image,char.rect)
        
        for char in self.score:
            screen.blit(char.image,char.rect)

        screen.blit(self.flash_coin.image,self.flash_coin.rect)

    def draw_load_mario(self,screen):
        for text in self.info:
            for char in text:
                screen.blit(char.image,char.rect)
        for char in self.mario_word:
             screen.blit(char.image,char.rect)

        for char in self.coin_total:
            screen.blit(char.image,char.rect)
        
        for char in self.score:
            screen.blit(char.image,char.rect)
        
        for char in self.load_world:
            screen.blit(char.image,char.rect)
        
        screen.blit(self.flash_coin.image,self.flash_coin.rect)

        screen.blit(self.mario.image,self.mario.rect)
        for char in self.mario_life:
            screen.blit(char.image,char.rect)
        
    def draw_load_luigi(self,screen):
        for text in self.info:
            for char in text:
                screen.blit(char.image,char.rect)

        for char in self.luigi_word:
             screen.blit(char.image,char.rect)

        for char in self.coin_total:
            screen.blit(char.image,char.rect)
        
        for char in self.score:
            screen.blit(char.image,char.rect)
        
        for char in self.load_world:
            screen.blit(char.image,char.rect)
        
        screen.blit(self.flash_coin.image,self.flash_coin.rect)

        screen.blit(self.luigi.image,self.mario.rect)
        for char in self.luigi_life:
            screen.blit(char.image,char.rect)
