# На вход подаётся двумерный массив damage размера как экран
# с вещественными значениями от 0 до 1
# На выход выводится картинка
# Для визуализации добавлены screen.fill(green)
# и задан массив damage[x][y]=(x+y)/(w+h), w, h - размеры экрана

# При вызове функции bomb(x, y) следует передать координаты бомбы
# Вызывать взрыв бомбы для отрисовки отдельно не нужно
# Однако массив damage здесь не обновляется
# Для визуализации задан вызов бомб каждые 50 кадров

# Для удаления бомбы с координатами x, y вызвать функцию del_bomb(x, y)
# Если таких несколько, удаляется только самая старая
import pygame
import math
import random
from pygame.draw import *
from field import *
from CONST import *

time = 0
screen = pygame.display.set_mode((width, height))
damage = []
for i in range(width+1):
    damage.append([])
    for j in range(height+1):
        damage[i].append(0)
bomb_time = []
bomb_x = []
bomb_y = []
bomb_count = 0
bomb_del = 0

def draw(t):
    #global width, height, time, bomb_del, bomb_x, bomb_y, bomb_time, bomb_count
    global time, bomb_del, bomb_x, bomb_y, bomb_time, bomb_count
    time = t

    for i in range(math.floor(width/10)):
        for j in range(math.floor(height/10)):
            rad_dot(10*i, 10*j)
    for i in range(bomb_count):
        draw_bomb(i)

    bomb_del = 0
    for i in range(bomb_count):
        boom_check(i)
    for i in range(bomb_del):
        del bomb_x[0]
        del bomb_y[0]
        del bomb_time[0]
        bomb_count -= 1

    


    #Чтобы разметка полей была над радиацией, но под бомбочками
    draw_field_lines(screen)
    
    for i in range(bomb_count):
        draw_bomb(i)

    bomb_del = 0
    for i in range(bomb_count):
        boom_check(i)
    for i in range(bomb_del):
        del bomb_x[0]
        del bomb_y[0]
        del bomb_time[0]
        bomb_count -= 1

def rad_dot(x, y):
    global damage, time
    time2 = time + round((x + y)/10)
    if (damage[x][y]>0):
        r = 128 + math.floor(127 * math.sin(time2/10))
        g = 255 - math.floor(255 * damage[x][y])
        b = 0
        Radius =  math.floor(2 + math.sin(time2/30))
        circle (screen, (r, g, b), (x, y), Radius, 0)

def dr_bomb(x, y):
    global bomb_time, bomb_x, bomb_y, bomb_count, time
    bomb_x.append(x)
    bomb_y.append(y)
    bomb_time.append(time)
    bomb_count += 1

def del_bomb(x, y):
    global bomb_time, bomb_x, bomb_y, bomb_count, time
    k = 0.5
    for i in range(bomb_count):
        if (bomb_x[i]==x):
            if (bomb_y[i]==y):
                k = i
                break
    if (k==0.5):
        k = 0.5
    else:
        del bomb_x[k]
        del bomb_y[k]
        del bomb_time[k]
        bomb_count -= 1

def bomb_color(t):
    r = int(t/boom * 255)
    c = (r, 0, 0)
    return c

def draw_bomb(i):
    global bomb_time, bomb_x, bomb_y, bomb_count, boom
    dt = time - bomb_time[i]
    x = bomb_x[i]
    y = bomb_y[i]
    color = bomb_color(dt)
    radius = 8
    blast_radius = 20
    circle (screen, color, (x, y), radius, 0)
    if (dt >= boom):
        circle (screen, (255, 255, 0), (x, y), blast_radius, 0)
        upd_dam(x, y)

def find_bomb_x():
    global bomb_count
    for i in range(bomb_count):
        x = bomb_x[i]
        y = bomb_y[i]
        if (what_field_is(x, y) == 2):
            return (x)

def find_bomb_y():
    global bomb_count
    for i in range(bomb_count):
        x = bomb_x[i]
        y = bomb_y[i]
        if (what_field_is(x, y) == 2):
            return (y)

def upd_dam(x, y):
    R = 20
    x0 = x - x%10
    y0 = y - y%10
    for i in range(13):
        for j in range(13):
            k = i - 6
            n = j - 6
            if (k*k + n*n <= 36):
                x1 = x0 + k * 10
                y1 = y0 + n * 10
                r = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
                if ((x1 >= 0) and (x1 <= 800)):
                    if ((y1 >= 0) and (y1 <= 600)):
                        damage[x1][y1] += (1 - damage[x1][y1]) * (R / (r + R))

def repair(x, y, p): #p = 1 - игрок, p = 2 - бот
    x0 = x - x%10
    y0 = y - y%10
    for i in range(7):
        for j in range(7):
            k = i - 3
            n = j - 3
            if (k*k + n*n <= 9):
                x1 = x0 + k * 10
                y1 = y0 + n * 10
                if ((x1 >= 0) and (x1 <= 800)):
                    if ((y1 >= 0) and (y1 <= 600)):
                        if (what_field_is(x1, y1) == p):
                            damage[x1][y1] = 0

def Health_Points():
    s = 0
    for i in range (width//10 + 1):
        for j in range (height//10 + 1):
            if (what_field_is(i*10, j*10) == 1):
                s += damage[i*10][j*10]
    return 1-200*s/width/height

def Health_Points_Bot():
    s = 0
    for i in range (width//10 + 1):
        for j in range (height//10 + 1):
            if (what_field_is(i*10, j*10) == 2):
                s += damage[i*10][j*10]
    return 1-200*s/width/height

def boom_check(i):
    global bomb_time, time, boom, bomb_del
    if (time - bomb_time[i] >= boom):
        bomb_del += 1


