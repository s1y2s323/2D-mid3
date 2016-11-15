import random

from pico2d import *


class Temp:
    image = None
    def __init__(self):
        self.x, self.y = 100, 100

        if Temp.image == None:
            Temp.image = load_image('Castle.png')

    def draw(self):
        self.image.clip_draw(0, 0, 200, 200, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-100,self.y-100,self.x+100,self.y+100

    def handle_event(self, event):
        pass







