import pygame
from drawing_module import dr_bomb, draw
from CONST import *
from field import *



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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if what_field_is(x, y) == 1:
                player_name = 'player'
                player_name = player()
                dr_bomb(x,y)
            else:
                player_name = 'bot'
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:  # '''нажата ЛКМ - событие связано с бомбой'''
                if player_name != 'bot':
                    #player_name.catch(x, y)
                    continue
                else:
                    dr_bomb(x,y)
                    #player_name.bomb(x, y)
            if pressed[2]:  # '''нажата ПКМ - событие связано с полем'''
                if player_name == 'player':
                    #player_name.repair(x, y)
                    continue

    draw(time )
    #draw_field_lines(screen)
    pygame.display.update()
    #screen.fill(test)
    draw_field(screen)

pygame.quit()



            
