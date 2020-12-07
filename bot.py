#from Bomb import create_bomb
from field import what_field_is
from math import ceil
from random import *
from drawing_module import dr_bomb, Health_Points, repair, find_bomb_x, find_bomb_y, del_bomb

#player 1 - игрок, player 2 - бот
bomb_x = []
bomb_y = []
bomb_count = 0
#атака рандомные клики, c freq = hp * k
def bot_attack():
    k = 2
    while (k==2):
        x = randint(0, 800)
        y = randint(0, 600)
        k = what_field_is(x, y)

    #x, y, bot
    #create_bomb(x, y, "bot")
    dr_bomb(x, y)

#оборона у бота есть массив потенциально обезвреживаемых бомб, он кидает кубик и пытается уничтожить самую старую
def bot_defend():
    x = find_bomb_x()
    y = find_bomb_y()
    del_bomb(x, y)

#починка рандомные клетки
def bot_repair():
    k = 1
    while (k == 1):
        x = randint(0, 800)
        y = randint(0, 600)
        k = what_field_is(x, y)

    # x, y, bot
    # create_bomb(x, y, "bot")
    repair(x, y, 2)

#когда что делать t - время в кадрах, hp - доля от полного здоровья бота
def bot_act(t):
    hp = Health_Points()
    print(hp)
    period = 6 / (abs(hp) + 0.1)
    per = ceil (period)
    if (t % per == 0):
        k = random()
        if (k<=1/3):
            bot_defend()
        elif (k <= 1/3 + hp *2/3):
            bot_attack()
        else:
            bot_repair()






