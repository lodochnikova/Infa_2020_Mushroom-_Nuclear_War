"""
f(x, y) = k
бомба
R = const, r - расстояние до эпицентра
f(x, y) = k + (1-k) * (R/(r+R))

Если k = 0, то станет 0.5
Если k = 1 то не изменится
"""



import pygame
from drawing_module import dr_bomb, draw, del_bomb, repair
from field import *
from bot import bot_act



pygame.init()
FPS = 30
screen = pygame.display.set_mode((width, height))

time = 0
draw(time)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
#test = (0, 128, 0)
while not finished:
    clock.tick(FPS)
    time += 1
    bot_act(time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if what_field_is(x, y) == 2:
                #player_name = 'player'
                #player_name = player()
                dr_bomb(x,y)
            else:
                for i in range(17):
                    for j in range(17):
                        k = i - 8
                        n = j - 8
                        if (k*k + n*n <= 64):
                            del_bomb(x+k, y+n)
                repair(x, y, 1)

            pressed = pygame.mouse.get_pressed()

    draw(time)
    #draw_field_lines(screen)
    pygame.display.update()
    #screen.fill(test)
    draw_field(screen)

pygame.quit()




