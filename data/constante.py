from pygame.locals import *

# State Game
MAIN_MENU = "main_menu"
LEVEL = "level"
LOAD = "load"
GAMEOVER = "gameover"
TIMEOUT = "timeout"
# State Gumba
DEATH = "death"
BORN = "born"

# State Star
STAR_SPAWN = "star_spawn"
STAR_MOVE = "star_move"

# State Flower
FLOWER_SPAWN = "flower_spawn"
FLOWER_RESTING = "flower_resting"

# State Mush
MUSH_SPAWN = "mush_spawn"
MUSH_MOVE = "mush_move"

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

MAX_WALK_SPEED = 6
WALK_ACC = 0.15
TURN_AROUD = 0.35
JUMP_VEL = -11
GRAVITY = 1
JUMP_GRAVITY = 0.31
MAX_VEL_Y = 11

handleInput = {
    "saut" : K_UP,
    "bas" : K_DOWN,
    "droite": K_RIGHT,
    "gauche" :K_LEFT,
    "action" : K_SPACE,
}

WIDTH = 800
HEIGHT = 600
GROUND_HEIGHT = HEIGHT - 62
FPS = 60

BACKGROUND_SIZE_MULTIPLIER = 2.679
SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69