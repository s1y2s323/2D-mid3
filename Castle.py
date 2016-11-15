import random

from pico2d import *


class Castle:
    image = None
    imagehp=None
    def __init__(self):
        self.x, self.y = 100, 100
        self.hp=100

        if Castle.image == None:
            Castle.image = load_image('Castle.png')
        if Castle.imagehp==None:
            Castle.imagehp=load_image('hpimage.png')

    def draw(self):
        self.image.clip_draw(0, 0, 200, 200, self.x, self.y)
        self.imagehp.clip_draw(0, 0, 40, 10, self.x, self.y + 150)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-100,self.y-100,self.x+100,self.y+100

    def handle_event(self, event):
        pass








