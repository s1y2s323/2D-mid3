from pico2d import *

import game_framework



from Knight import knight # import Boy class from boy.py
from Castle import Castle
from Select import Select
from Zombie import zombie
from Ninza import ninza
from Bomb import bomb
from Cannon import cannon
import time



name = "collision"

pX2=0
pY2=0
pX3=0
pY3=0

def create_world():
    global boy,castle,select,boy2,boy3,bom,can

    pX2=None
    pY2=None
    pX3=None
    pY3=None
    boy=[]
    boy2=[]
    boy3=[]
    castle=Castle()
    select=Select()
    bom=bomb()
    can=cannon()

def destroy_world():
    global boy,castle,select,boy2,boy3,bom
    for Knight in boy:
        del(Knight)
    for Zombie in boy2:
        del(Zombie)
    for Ninza in boy3:
        del(Ninza)

    del(castle)
    del(select)
    del(bom)
    del(can)




def enter():
    open_canvas(1000,600)
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.button)== (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
                select.handle_event(event)
                if select.type==1:
                    boy.append(knight())
                    boy2.append(zombie())
                    boy2.append(zombie())
                elif select.type==2:
                    boy.append(ninza())



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a <left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def createobject():

    c_time =time.clock()
    temp_time=int(c_time)
    temp_time = int(c_time)%10
   # print(c_time)
   # print(temp_time)

   # if temp_time % 5 ==0:

      #  boy.append(knight())





def update(frame_time):
    global pX2, pY2, pX3, pY3
    for Knight in boy:
        Knight.update(frame_time)
    for Zombie in boy2:
        Zombie.update(frame_time)
    for Ninza in boy3:
        Ninza.update(frame_time)
    for boys2 in boy2:
        if boys2.x <1000 and boys2.x>500:
            pX3=boys2.x
            pY3=boys2.y
            pX2=(pX3+50)/2
            pY2=300
            bom.update(frame_time, pX2, pY2, pX3, pY3)
            break





    #bom.update(frame_time)



    for boys in boy:
        boys.set_state(boys.RIGHT_RUN, None)
        for boys2 in boy2:
            if collide(boys,boys2)==False:# and boys.get_state()==boys.RIGHT_ATTACK:
                boys.set_state(boys.RIGHT_RUN, None)
            elif(collide(boys,boys2)):
                boys.set_state(boys.RIGHT_ATTACK,boys2)
                if (boys2.hp < 0):
                    boy2.remove(boys2)
                break
            if boys.y > boys2.y and boys.get_state==boys.RIGHT_RUN:
                boys.set_dirY(0)
                break
            elif boys.y < boys2.y and boys.get_state==boys.RIGHT_RUN:
                boys.set_dirY(1)
                break

    for boys2 in boy2:
        boys2.set_state(boys2.LEFT_RUN, None)
        for boys in boy:
            if collide(boys2, boys) == False:# and boys2.get_state() == boys2.LEFT_ATTACK:
                boys2.set_state(boys2.LEFT_RUN,None)
            elif(collide(boys2,boys)):
                boys2.set_state(boys2.LEFT_ATTACK,boys)
                if(boys.hp<0):
                    boy.remove(boys)
                break

    for boys2 in boy2:
        if collide(boys2,castle) == True:
            boys2.set_state(boys2.LEFT_ATTACK, castle)


def draw(frame_time):
    clear_canvas()

    for Knight in boy:
        Knight.draw()
        Knight.draw_bb()

    for Zombie in boy2:
        Zombie.draw()
        Zombie.draw_bb()

    for Ninza in boy3:
        Ninza.draw()
        Ninza.draw_bb()

    can.draw()
    can.draw_bb()
    bom.draw()
    bom.draw_bb()
    castle.draw()
    castle.draw_bb()
    select.draw()
    select.draw_bb()





    update_canvas()






