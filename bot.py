from bomb import create_bomb
from field import what_field_is
from math import ceil
from random import *
#player 1 - игрок, player 2 - бот
bomb_x = []
bomb_y = []
bomb_count = 0
#атака рандомные клики, c freq = hp * k
def bot_attack():
    k = 0
    while (k==0):
        x = randint (800)
        y = randint (600)
        k = what_field_is(x, y)
    #x, y, bot
    create_bomb(x, y, "bot")

#оборона у бота есть массив потенциально обезвреживаемых бомб, он кидает кубик и пытается уничтожить самую старую
def bot_defend():
    k = 0
    for i in range(100)
        i = randint(bomb_count)
        x = bomb_x [i]
        y = bomb_y [i]
        if (what_field_is(x, y) == 2):
            del_bomb(x, y, "player")

#починка рандомные клетки
def bot_repair():
    field_to_help = None
    for field in fields:
        if field.holder_name == 'bot':
            if field_to_help == None or field_to_help.hp > field.hp:
                field_to_help = field
    field_to_help('bot')

#когда что делать t - время в кадрах, hpP - доля от полного здоровья игрока, hpB - бота:
def bot_act(t, hpP, hpB):
    period = 6 / (abs(hp) + 0.1)
    per = ceil (period)
    if (t % per == 0):
        k = random()
        if (k<=1/3):
            bot_defend()
        elif (k <= 1/3 + hp *2/3):
            bot_attack()
        else
            bot_repair()






