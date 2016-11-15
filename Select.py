from pico2d import *


class Select:
    image = None
    def __init__(self):
        self.x, self.y = 100, 550
        self.type=5
        if Select.image == None:
            Select.image = load_image('Select.png')

    def draw(self):
        self.image.clip_draw(0, 0, 200, 100, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-50,self.y-50,self.x+50,self.y+50


    def handle_event(self,event):
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            self.select(event.x,599-event.y)


    def get_type(self):
        return self.type


    def select(self,a, b):
        if a > 0 and a <100 and b >500 and b<600:
            self.type=1
        elif a >100 and a<200 and b>500 and b<600:
            self.type=2











