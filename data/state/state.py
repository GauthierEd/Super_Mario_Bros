class State(object):
    def __init__(self):
        self.done = False
        self.next = None

    def startup(self,current_time):
        self.current_update = current_time

    def cleanup(self):
        self.done = False
    
    def update(self,keys,screen,current_time):
        pass

    def draw_everything(self,screen):
        pass