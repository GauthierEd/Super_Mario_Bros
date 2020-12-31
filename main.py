import pygame as pg
from pygame.locals import *
import data.constante as c
import data.setup
from data.state import level_1_1,level_1_2,state_load,state_menu,state_timeout,state_gameover


class Game(object):
    def __init__(self,state):
        self.screen = pg.display.get_surface()
        self.running = 1
        self.show_fps = False
        self.clock = pg.time.Clock()
        self.all_state = {
            c.MAIN_MENU : state_menu.Menu(),
            c.LOAD : state_load.Load(),
            c.LEVEL_1_1 : level_1_1.Level_1_1(),
            c.LEVEL_1_2 : level_1_2.Level_1_2(),
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
                self.toggle_fps(event.key)
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
        
    def toggle_fps(self,key):
        if key == K_F5:
            self.show_fps = not self.show_fps
            if not self.show_fps:
                pg.display.set_caption("Super Mario Bros")

    def main(self):
        while self.running:
            self.clock.tick(c.FPS)
            self.handle_event()
            self.update()    
            pg.display.flip()
            if self.show_fps:
                fps = self.clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format("Super Mario Bros", fps)
                pg.display.set_caption(with_fps)


if __name__ == "__main__":
    game = Game(c.MAIN_MENU)
    game.main()
    pg.quit()