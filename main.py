import pygame as pg
from pygame.locals import *
import data.constante as c
from data.state import level,state_load,state_menu,state_timeout,state_gameover



class Game(object):
    def __init__(self,state):
        pg.display.set_caption("Super Mario Bros")
        self.screen = pg.display.set_mode((c.WIDTH,c.HEIGHT))
        self.running = 1
        self.clock = pg.time.Clock()
        self.all_state = {
            c.MAIN_MENU : state_menu.Menu(),
            c.LOAD : state_load.Load(),
            c.LEVEL : level.Level(),
            c.GAMEOVER : state_gameover.GameOver(),
            c.TIMEOUT : state_timeout.timeOut()
        }
        self.keys = pg.key.get_pressed()
        self.state = self.all_state[state]

    def handle_event(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = 0
            elif event.type == KEYDOWN:
                self.keys = pg.key.get_pressed()
            elif event.type == KEYUP:
                self.keys = pg.key.get_pressed()
    
    def update(self):
        self.current_time = pg.time.get_ticks()
        if self.state.done:
            self.flip_state()
        
        self.state.update(self.keys,self.screen,self.current_time)
    
    def flip_state(self):
        state_name = self.state.next
        self.state.cleanup()
        self.state = self.all_state[state_name]
        self.state.startup(self.current_time)
        

    def main(self):
        while self.running:
            self.clock.tick(c.FPS)
            self.handle_event()
            self.update()    
            pg.display.flip()

if __name__ == "__main__":
    pg.init()
    game = Game(c.MAIN_MENU)
    game.main()
    pg.quit()