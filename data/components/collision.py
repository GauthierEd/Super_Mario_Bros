import pygame as pg
from .  import info
from .. import sound
from .. import constante as c 
from . brick import *
from . ennemy import *
from . coin import *
from . power import *
from . checkpoint import *

class Collision(object):
    def __init__(self,game):
        self.game = game

    
    def check_mario_x_collision(self,player):
        # ///   GROUND PIPE STAIR COLLISION X   ///
        try:
            hit_ground_pipe_stair = pg.sprite.spritecollideany(player,self.game.ground_pipe_stair)
            if hit_ground_pipe_stair:
                self.adjust_position_x(hit_ground_pipe_stair,player)
        except AttributeError:
            pass
        # ///   BRICK COLLISION X   ///
        try:
            hit_brick = pg.sprite.spritecollideany(player,self.game.brick)
            if hit_brick:
                self.adjust_position_x(hit_brick,player)
        except AttributeError:
            pass

        # ///   COIN BRICK COLLISION X   ///
        try:
            hit_coin_brick = pg.sprite.spritecollideany(player,self.game.coin_brick)
            if hit_coin_brick:
                self.adjust_position_x(hit_coin_brick,player)
        except AttributeError:
            pass

        # ///   POWER COLLISION X   ///
        try:
            hit_power = pg.sprite.spritecollideany(player,self.game.power)
            if hit_power:
                self.adjust_collision_power(hit_power,player)
        except AttributeError:
           pass

        # ///   COIN COLLISION X   ///
        try:
            hit_coin = pg.sprite.spritecollideany(player,self.game.bigCoin)
            if hit_coin:
                sound.coin.play()
                info.game_info["coin_count"] += 1
                hit_coin.kill()
        except AttributeError:
            pass

        # ///   ENNEMY COLLISION X   ///
        try:
            hit_ennemy = pg.sprite.spritecollideany(player,self.game.ennemy)
            if hit_ennemy and not player.wasTouched and not player.state == c.JUMPTODEATH:
                self.adjust_collision_ennemy_x(hit_ennemy,player)        
        except AttributeError:
            pass

        # ///   CHECKPOINT COLLISION X   ///
        try:
            hit_checkpoint = pg.sprite.spritecollideany(player,self.game.checkpoint)
            if hit_checkpoint:
                self.adjust_collision_checkpoint(hit_checkpoint,player)
        except AttributeError:
            pass


        if player.rect.x < self.game.viewport.x:
            player.rect.x = self.game.viewport.x

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
        self.game.set_score("1000",power.rect.x,power.rect.y)
        if power.name == "mush":
            power.kill()
            sound.powerup.play()
            if player.isBig:
                pass
            else:
                player.state = c.TOBIG
                player.transform = True
            if not self.game.multi:
                self.game.change_mush_into_flower()
            elif self.game.multi:
                if self.game.mario.isBig or self.game.luigi.isBig:
                    self.game.change_mush_into_flower()
        elif power.name == "flower":
            power.kill()
            sound.powerup.play()
            if player.power:
                pass
            else:
                player.state = c.TORED
                player.transform = True
        elif power.name == "star":
            power.kill()
            sound.main.stop()
            sound.powerup.play()
            sound.star.play()
            player.setInvincible()
        elif power.name == "mushLife":
            power.kill()
            sound.up.play()
            info.game_info[str(player.name)+"_lives"] += 1

    def adjust_collision_ennemy_x(self,ennemy,player):
        if player.rect.right > ennemy.rect.left and player.rect.left < ennemy.rect.left:
            if player.invincible:
                if ennemy.name == "gumba":
                    self.game.set_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy.name == "koopa":
                    self.game.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.game.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.game.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.game.ennemy_death.add(ennemy)
            elif player.isBig:
                if ennemy.name == "shell" and ennemy.vx == 0:
                    
                    player.rect.right = ennemy.rect.left
                    ennemy.vx = 8
                    player.vx -= 3
                else:
                    player.state = c.TOSMALL
                    player.transform = True
                    self.game.change_flower_into_mush()
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
                    self.game.set_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                    
                elif ennemy.name == "koopa":
                    self.game.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.game.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.game.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.game.ennemy_death.add(ennemy)
            elif player.isBig:
                if ennemy.name == "shell" and ennemy.vx == 0:
                    player.rect.left = ennemy.rect.right
                    ennemy.vx = -8
                    player.vx += 3
                else:
                    player.state = c.TOSMALL
                    player.transform = True
                    self.game.change_flower_into_mush()
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

    def adjust_collision_checkpoint(self,checkpoint,player):
        if checkpoint.name == "1":
            self.game.ennemy.add(self.game.ennemy_g1)
            checkpoint.kill()
        elif checkpoint.name == "2":
            self.game.ennemy.add(self.game.ennemy_g2)
            checkpoint.kill()
        elif checkpoint.name == "3":
            self.game.ennemy.add(self.game.ennemy_g3)
            checkpoint.kill()
        elif checkpoint.name == "4":
            self.game.ennemy.add(self.game.ennemy_g4)
            checkpoint.kill()
        elif checkpoint.name == "5":
            self.game.ennemy.add(self.game.ennemy_g5)
            checkpoint.kill()
        elif checkpoint.name == "6":
            self.game.ennemy.add(self.game.ennemy_g6)
            checkpoint.kill()
        elif checkpoint.name == "7":
            self.game.ennemy.add(self.game.ennemy_g7)
            checkpoint.kill()
        elif checkpoint.name == "8" and player.state != c.SLIDEFLAG and player.state != c.WAITFLAG:
            
            if self.game.multi:
                if self.game.luigi.state != c.SLIDEFLAG and self.game.luigi.state != c.WAITFLAG and self.game.mario.state != c.SLIDEFLAG and self.game.mario.state != c.WAITFLAG:
                    sound.main.stop()
                    sound.flag.play()
            else:
                sound.main.stop()
                sound.flag.play()
            player.state = c.SLIDEFLAG
            if self.game.flag.state != c.SLIDEFLAG:
                self.game.flag.state = c.SLIDEFLAG
            if player.rect.centery < 125:
                info.game_info[str(player.name)+"_lifes"] += 1
                sound.up.play()

            elif player.rect.centery > 125 and player.rect.centery < 168:
                info.game_info["scores"] += 5000
                self.game.set_score("5000",player.rect.x+30,player.rect.y )

            elif player.rect.centery > 168 and player.rect.centery < 302:
                info.game_info["scores"] += 2000
                self.game.set_score("2000",player.rect.x+30,player.rect.y)

            elif player.rect.centery > 302 and player.rect.centery < 375:
                info.game_info["scores"] += 800
                self.game.set_score("800",player.rect.x+30,player.rect.y)

            elif player.rect.centery > 375 and player.rect.centery < 455:
                info.game_info["scores"] += 400
                self.game.set_score("400",player.rect.x+30,player.rect.y)

            elif player.rect.centery > 455 and player.rect.centery < 493:
                info.game_info["scores"] += 200
                self.game.set_score("200",player.rect.x+30,player.rect.y)
            checkpoint.kill()
            if len(self.game.player) > 1:
                self.game.checkpoint.add(checkPoint(checkpoint.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,checkpoint.rect.y / c.BACKGROUND_SIZE_MULTIPLIER,checkpoint.rect.w/ c.BACKGROUND_SIZE_MULTIPLIER,checkpoint.rect.h/ c.BACKGROUND_SIZE_MULTIPLIER,"8"))
            
        elif checkpoint.name == "9" and player.state == c.SLIDEFLAG:
            player.rect.x = player.rect.right + 5
            player.right = False
            player.vy = 0
            if self.game.multi:
                if self.game.mario.state != c.WAITFLAG and self.game.mario.state != c.WALKTOCASTLE and self.game.luigi.state != c.WAITFLAG and self.game.luigi.state != c.WALKTOCASTLE:
                    sound.end.play()
            else:
                sound.end.play()
            player.state = c.WAITFLAG
        elif checkpoint.name == "pipe":
            player.canGoUnder = True
        elif checkpoint.name == "pipe2":
            player.canGoOverworld = True

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
        # ///   LIFT COLLISION Y   ///
        try:
            hit_lift = pg.sprite.spritecollideany(player,self.game.lift)
            if hit_lift:
                self.adjust_position_lift_y(hit_lift,player)
        except AttributeError:
            pass

        # ///   GROUND PIPE STAIR COLLISION Y   ///
        try:
            hit_ground_pipe_stair = pg.sprite.spritecollideany(player,self.game.ground_pipe_stair)
            if hit_ground_pipe_stair:
                self.adjust_position_collider_y(hit_ground_pipe_stair,player)
        except AttributeError:
            pass

        # ///   BRICK COLLISION Y   ///
        try:
            hit_brick = pg.sprite.spritecollideany(player,self.game.brick)
        except AttributeError:
            pass

        # ///   COIN BRICK COLLISION Y   ///
        try:
            hit_coin_brick = pg.sprite.spritecollideany(player,self.game.coin_brick)
        except AttributeError:
            pass


        # ///   ENNEMY COLLISION Y   ///
        try:
            hit_ennemy = pg.sprite.spritecollideany(player,self.game.ennemy)
            if hit_ennemy and not player.wasTouched:
                self.adjust_collision_ennemy_y(hit_ennemy,player)        
        except AttributeError:
            pass

        if hit_brick and hit_coin_brick:
            hit_brick,hit_coin_brick = self.prevent_error_collision(hit_brick,hit_coin_brick,player)

        if hit_brick:
            self.adjust_position_brick(hit_brick,player)
        elif hit_coin_brick:
            self.adjust_position_coin_brick(hit_coin_brick,player)

    def adjust_position_lift_y(self,lift,player):
        if player.rect.bottom > lift.rect.top and player.rect.top < lift.rect.top:
            player.vy = lift.vy
            player.rect.bottom = lift.rect.top
            if player.state != c.WALKTOCASTLE and player.state != c.WAITFLAG and player.state != c.SLIDEFLAG:
                player.state = c.WALK
            player.isjump = False

        elif player.rect.top < lift.rect.bottom and player.rect.bottom > lift.rect.bottom:
            player.vy = 3
            player.rect.top = lift.rect.bottom
            player.state = c.FALL 

    def adjust_position_collider_y(self,collider,player):
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
    
    def adjust_collision_ennemy_y(self,ennemy,player):
        if player.rect.bottom > ennemy.rect.top and player.rect.top < ennemy.rect.top:
            if player.invincible:
                if ennemy.name == "gumba":
                    self.game.set_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy.name == "koopa":
                    self.game.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.game.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.game.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.game.ennemy_death.add(ennemy)
            else:
                sound.stomp.play()
                player.vy = -7
                player.rect.bottom = ennemy.rect.top
                if ennemy.name == "gumba":
                    self.game.ennemy.remove(ennemy)
                    self.game.set_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                    ennemy.startToDeath()
                    self.game.ennemy_death.add(ennemy)
                elif ennemy.name == "koopa":
                    self.game.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    self.game.ennemy.remove(ennemy)
                    info.game_info["scores"] += 200
                    if ennemy.type == "overworld":
                        self.game.ennemy.add(ShellOverworld(ennemy.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(ennemy.rect.y / c.BACKGROUND_SIZE_MULTIPLIER)+9,pg.time.get_ticks(),self.ennemy))
                    elif ennemy.type == "underground":
                        self.game.ennemy.add(ShellUnderground(ennemy.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(ennemy.rect.y / c.BACKGROUND_SIZE_MULTIPLIER)+9,pg.time.get_ticks(),self.ennemy))
                    elif ennemy.type == "red":
                        self.game.ennemy.add(ShellRed(ennemy.rect.x / c.BACKGROUND_SIZE_MULTIPLIER,(ennemy.rect.y / c.BACKGROUND_SIZE_MULTIPLIER)+9,pg.time.get_ticks(),self.ennemy))
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
                    self.game.set_score("100",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 100
                elif ennemy.name == "koopa":
                    self.game.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                elif ennemy.name == "shell":
                    self.game.set_score("200",ennemy.rect.x,ennemy.rect.y)
                    info.game_info["scores"] += 200
                self.game.ennemy.remove(ennemy)
                ennemy.jumpToDeath()
                sound.kick.play()
                self.game.ennemy_death.add(ennemy)
            elif player.isBig:
                player.state = c.TOSMALL
                player.transform = True
                self.game.change_flower_into_mush()
                player.setWasTouched()
                sound.pipe.play()
            else:
                player.vy = - 8
                player.state = c.JUMPTODEATH
    
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
                    self.game.check_if_ennemy_on_brick(collider)
                    collider.kill()
                    if collider.name == "overworld":
                        self.game.brick_piece.add(BrickPieceOverworld(collider.rect.x,collider.rect.y,-5,-12,0))
                        self.game.brick_piece.add(BrickPieceOverworld(collider.rect.right-16,collider.rect.y,5,-12,1))
                        self.game.brick_piece.add(BrickPieceOverworld(collider.rect.x,collider.rect.bottom-16,-5,-8,2))
                        self.game.brick_piece.add(BrickPieceOverworld(collider.rect.right-16,collider.rect.bottom-16,5,-8,3))
                    elif collider.name == "underground":  
                        self.game.brick_piece.add(BrickPieceUnderground(collider.rect.x,collider.rect.y,-5,-12,0))
                        self.game.brick_piece.add(BrickPieceUnderground(collider.rect.right-16,collider.rect.y,5,-12,1))
                        self.game.brick_piece.add(BrickPieceUnderground(collider.rect.x,collider.rect.bottom-16,-5,-8,2))
                        self.game.brick_piece.add(BrickPieceUnderground(collider.rect.right-16,collider.rect.bottom-16,5,-8,3))
                else:
                    sound.bump.play()
                    if collider.state != c.OPENED:
                        collider.startBump()
                        self.game.check_if_ennemy_on_brick(collider)
                        if collider.content == "coin":
                            info.game_info["coin_count"] += 1
                            self.game.set_score("200",collider.rect.x,collider.rect.y)
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
                    self.game.check_if_ennemy_on_brick(collider)
                    if collider.content == "coin":
                        info.game_info["coin_count"] += 1
                        self.game.set_score("200",collider.rect.x,collider.rect.y)
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
                    self.game.set_score("200",collider.rect.x,collider.rect.y)
                    sound.coin.play()
                else:
                    sound.power_appear.play()
                
            else:
                sound.bump.play()
            if collider.state != c.OPENED:
                collider.startBump()
                self.game.check_if_ennemy_on_brick(collider)
            player.vy = 5
            player.rect.top = collider.rect.bottom
            player.state = c.FALL


