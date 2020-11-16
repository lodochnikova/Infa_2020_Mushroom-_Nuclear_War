# На вход подаётся двумерный массив damage размера как экран
# с вещественными значениями от 0 до 1
# На выход выводится картинка
# Для визуализации добавлены screen.fill(green)
# и задан массив damage[x][y]=(x+y)/(w+h), w, h - размеры экрана
import pygame
import math
import random
from pygame.draw import *

width = 800
height = 600
time = 0
DARK_YELLOW = (128, 128, 0)
BRIGHT_YELLOW = (255, 255, 0)

damage = []
for i in range(width):
    damage.append([])
    for j in range(height):
        damage[i].append((i+j)/(width+height))

def draw():
    global width, height, time
    for i in range(math.floor(width/10)):
        for j in range(math.floor(height/10)):
            rad_dot(10*i, 10*j)

def rad_dot(x, y):
    global damage, time
    time2 = time + round((x + y)/10)
    if (damage[x][y]>0):
        r = 128 + math.floor(127 * math.sin(time2/10))
        g = 255 - math.floor(255 * damage[x][y])
        b = 0
        Radius = 2 + math.sin(time2/30)
        circle (screen, (r, g, b), (x, y), Radius, 0)

pygame.init()
FPS = 30
screen = pygame.display.set_mode((width, height))

draw()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
test = (0, 128, 0)
while not finished:
    clock.tick(FPS)
    time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    draw()
    pygame.display.update()
    screen.fill(test)

pygame.quit()
