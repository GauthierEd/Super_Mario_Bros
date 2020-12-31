from pygame.locals import *

# State Game
MAIN_MENU = "main_menu"
LEVEL_1_1 = "level_1_1"
LEVEL_1_2 = "level_1_2"
LOAD = "load"
GAMEOVER = "gameover"
TIMEOUT = "timeout"

# State Gumba
DEATH = "death"
BORN = "born"

#State Power
POWER_SPAWN = "power_spawn"
POWER_MOVE = "power_move"
POWER_RESTING = "power_resting"


# State Level
FREEZE = "freeze"
NOTFREEZE = "notfreeze"
INCASTLE = "incastle"


# State Brick
BUMPED = "bumped"
OPENED = "opened"
RESTING = "resting"
STAYING = "staying"

# State Mario
STAND = "standing"
WALK = "walking"
JUMP = "jumping"
FALL = "falling"
TOBIG = "tobig"
TOSMALL = "tosmall"
TORED = "tored"
JUMPTODEATH = "jumptodeath"
DEAD = "dead"
SLIDEFLAG = "slideflag"
WAITFLAG = "waitflag"
WALKTOCASTLE = "walktocastle"
CINEMATIC = "cinematic"

MAX_WALK_SPEED = 6
WALK_ACC = 0.15
TURN_AROUD = 0.35
JUMP_VEL = -11
GRAVITY = 1
JUMP_GRAVITY = 0.31
MAX_VEL_Y = 11

inputMario = {
    "saut" : K_UP,
    "bas" : K_DOWN,
    "droite": K_RIGHT,
    "gauche" :K_LEFT,
    "action" : K_SPACE,
}

inputLuigi = {
    "saut" : K_z,
    "bas" : K_s,
    "droite": K_d,
    "gauche": K_q,
    "action" : K_r,
}

WIDTH = 800
HEIGHT = 600
GROUND_HEIGHT = HEIGHT - 62
FPS = 60

BACKGROUND_SIZE_MULTIPLIER = 2.679
SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
PIPE_SIZE_MULTIPLIER = 2.6875