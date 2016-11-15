import random

from pico2d import *

class zombie:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 8.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None

    DEAD, LEFT_ATTACK, LEFT_RUN= 0, 1, 2

    def __init__(self):
        self.x, self.y = 1000,random.randint(30,120)
        self.hp=100
        self.frameimage=0
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dirX = -1
        self.dirY=0
        self.state = self.LEFT_RUN

        if zombie.image == None:
            zombie.image = load_image('zombie.png')


    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = zombie.RUN_SPEED_PPS * frame_time
        self.total_frames += zombie.FRAMES_PER_ACTION * zombie.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        self.x += (self.dirX * distance)

        self.x = clamp(0, self.x, 1000)

    def get_state(self):
        return self.state


    def draw(self):
        self.image.clip_draw(self.frame * 40, self.state * 40, 40, 40, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def set_state(self, x, y):
        if x == self.LEFT_ATTACK:
            self.state = self.LEFT_ATTACK
            self.dirX = 0
            if (self.frame == 7):
                y.hp -= 1
        elif x == self.LEFT_RUN:
            self.state = self.LEFT_RUN
            self.dirX = -1



    def get_bb(self):
        return self.x-20,self.y-20,self.x+20,self.y+20


    def handle_event(self, event):
        pass







