# На вход подаётся двумерный массив damage размера как экран
# с вещественными значениями от 0 до 1
# На выход выводится картинка
# Для визуализации добавлены screen.fill(green)
# и задан массив damage[x][y]=(x+y)/(w+h), w, h - размеры экрана

# При вызове функции bomb(x, y) следует передать координаты бомбы
# Вызывать взрыв бомбы для отрисовки отдельно не нужно
# Однако массив damage здесь не обновляется
# Для визуализации задан вызов бомб каждые 50 кадров
import pygame
import math
import random
from pygame.draw import *
from field import *
from CONST import *

time = 0

damage = []
for i in range(width):
    damage.append([])
    for j in range(height):
        damage[i].append((i+j)/(width+height))
bomb_time = []
bomb_x = []
bomb_y = []
bomb_count = 0
bomb_del = 0

def draw():
    #global width, height, time, bomb_del, bomb_x, bomb_y, bomb_time, bomb_count
    global time, bomb_del, bomb_x, bomb_y, bomb_time, bomb_count

    print (time)
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

    if (time % 30 == 0):
        bomb(time % 800, time % 600)
        bomb(time % 800 + 50, time % 600)

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

    if (time % 30 == 0):
        bomb(time % 800, time % 600)
        bomb(time % 800 + 50, time % 600)

def rad_dot(x, y):
    global damage, time
    time2 = time + round((x + y)/10)
    if (damage[x][y]>0):
        r = 128 + math.floor(127 * math.sin(time2/10))
        g = 255 - math.floor(255 * damage[x][y])
        b = 0
        Radius =  math.floor(2 + math.sin(time2/30))
        circle (screen, (r, g, b), (x, y), Radius, 0)

def bomb(x, y):
    global bomb_time, bomb_x, bomb_y, bomb_count, time
    bomb_x.append(x)
    bomb_y.append(y)
    bomb_time.append(time)
    bomb_count += 1

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

def boom_check(i):
    global bomb_time, time, boom, bomb_del
    if (time - bomb_time[i] >= boom):
        bomb_del += 1


pygame.init()
FPS = 30
screen = pygame.display.set_mode((width, height))

draw()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
#test = (0, 128, 0)
while not finished:
    clock.tick(FPS)
    time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    draw()
    #draw_field_lines(screen)
    pygame.display.update()
    #screen.fill(test)
    draw_field(screen)

pygame.quit()