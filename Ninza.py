import random

from pico2d import *

class ninza:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 12.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 10

    image = None
    imagehp=None

    DEAD, RIGHT_ATTACK, RIGHT_RUN= 0, 1, 2

    def __init__(self):
        self.x, self.y = 0, random.randint(30,120)
        self.hp=100
        self.frameimage=0
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dirX = 1
        self.dirY=0
        self.state = self.RIGHT_RUN

        if ninza.image == None:
            ninza.image = load_image('Ninza.png')
        if ninza.imagehp==None:
            ninza.imagehp=load_image('hpimage.png')




    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))
        self.life_time += frame_time
        distance = ninza.RUN_SPEED_PPS * frame_time
        self.total_frames += ninza.FRAMES_PER_ACTION * ninza.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        self.x += (self.dirX * distance)
        self.y+=(self.dirY*distance)

        self.x = clamp(0, self.x, 1000)
        print(self.frame)

    def set_dirY(self,n):
        if n==1:
            self.dirY=1
        elif n == 0:
            self.dirY = -1
        elif n == 2:
            self.dirY = 0


    def draw(self):
        self.image.clip_draw(self.frame * 40, self.state * 40, 40, 40, self.x, self.y)
        self.imagehp.clip_draw(0, 0, int((40*self.hp)/100), 10, self.x, self.y+25)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x-20,self.y-20,self.x+20,self.y+20

    def set_state(self,x,y):
        if x==self.RIGHT_ATTACK:
            self.state=self.RIGHT_ATTACK
            self.dirX=0
            if(self.frame==9):
                y.hp -= 1
        elif x==self.RIGHT_RUN:
            self.state=self.RIGHT_RUN
            self.dirX=1

    def get_state(self):
        return self.state





           # print(self.total_frames)


    def ai(self):
        pass



    def handle_event(self, event):
        pass







