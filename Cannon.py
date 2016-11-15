import random

from pico2d import *


class cannon:
    image = None
    imagehp=None
    def __init__(self):
        self.x, self.y = 30, 30
        self.hp=100

        if cannon.image == None:
            cannon.image = load_image('cannon.png')
        if cannon.imagehp==None:
            cannon.imagehp=load_image('hpimage.png')

    def draw(self):
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y)
        self.imagehp.clip_draw(0, 0, 40, 10, self.x, self.y + 40)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-100,self.y-100,self.x+100,self.y+100

    def handle_event(self, event):
        pass








