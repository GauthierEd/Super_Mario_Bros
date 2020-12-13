import pygame as pg

""" FICHIER SOUND """

pg.mixer.init()

small_jump = pg.mixer.Sound("sounds/jump_small.ogg")
big_jump = pg.mixer.Sound("sounds/jump_big.ogg")
bump = pg.mixer.Sound("sounds/bump.ogg")
break_sound = pg.mixer.Sound("sounds/break.ogg")
coin = pg.mixer.Sound("sounds/coin.ogg")
power_appear = pg.mixer.Sound("sounds/power_appear.ogg")
powerup = pg.mixer.Sound("sounds/powerup.ogg")
stomp = pg.mixer.Sound("sounds/stomp.ogg")
pipe = pg.mixer.Sound("sounds/pipe.ogg")
kick = pg.mixer.Sound("sounds/kick.ogg")
fireball = pg.mixer.Sound("sounds/fireball.ogg")
die = pg.mixer.Sound("sounds/die.ogg")
up = pg.mixer.Sound("sounds/1up.ogg")
flag = pg.mixer.Sound("sounds/flag.ogg")
count_time = pg.mixer.Sound("sounds/count_down.ogg")

main = pg.mixer.Sound("sounds/main.ogg")
star = pg.mixer.Sound("sounds/star.ogg")
time = pg.mixer.Sound("sounds/time.ogg")
end = pg.mixer.Sound("sounds/end.ogg")
gameover = pg.mixer.Sound("sounds/gameover.ogg")