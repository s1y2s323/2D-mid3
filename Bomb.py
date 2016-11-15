import random

from pico2d import *


class bomb:
    image = None
    imagehp=None
    def __init__(self):
        self.x, self.y = 50, 50
        self.hp=100
        self.t=0
        self.px1,self.py1=50,50
        self.px2, self.py2 = 500, 500
        self.px3, self.py3 = 700, 100
        self.onoff=False

        if bomb.image == None:
            bomb.image = load_image('bomb.png')
        if bomb.imagehp==None:
            bomb.imagehp=load_image('hpimage.png')

    def update(self, frame_time,px2,py2,px3,py3):
        if self.t>1:
            self.x=200
            self.y=50
            self.t=0
            self.onoff=True
        self.t+=0.005
        self.x=(1-self.t)*(1-self.t)*self.px1 + 2*self.t*(1-self.t)*px2 + self.t*self.t*px3
        self.y = (1 - self.t) * (1 - self.t) * self.py1 + 2 * self.t * (
        1 - self.t) * py2 + self.t * self.t * py3


    def get_t(self):
        return self.t


    def draw(self):
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y)
        self.imagehp.clip_draw(0, 0, 40, 10, self.x, self.y + 40)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x-25,self.y-25,self.x+25,self.y+25

    def handle_event(self, event):
        pass








