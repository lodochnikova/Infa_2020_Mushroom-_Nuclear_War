"""
f(x, y) = k
бомба
R = const, r - расстояние до эпицентра
f(x, y) = k + (1-k) * (R/(r+R))

Если k = 0, то станет 0.5
Если k = 1 то не изменится
"""



import pygame
from drawing_module import dr_bomb, draw, del_bomb, repair, Health_Points, Health_Points_Bot
from field import *
from bot import bot_act
from Ending import Bot_Win, Player_Win




pygame.init()
FPS = 30
screen = pygame.display.set_mode((width, height))

time = 0
draw(time)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
started = False
#test = (0, 128, 0)
while not finished:
    if not started:
        screen.fill(WHITE)
        circle(screen, (128, 10, 10), (250, 250), 200, 0)
        circle(screen, (0, 0, 0), (250, 250), 200, 5)

        f1 = pygame.font.Font(None, 50)
        text1 = f1.render('DO NOT TOUCH', True,
                          (0, 0, 0))
        screen.blit(text1, (width // 7, height // 1.3))

        f2 = pygame.font.Font(None, 30)
        text1 = f2.render('Click on enemy’s territory', True,
                          (0, 0, 0))
        screen.blit(text1, (width // 1.55, height // 5))

        f3 = pygame.font.Font(None, 30)
        text1 = f3.render('to drop the bomb', True,
                          (0, 0, 0))
        screen.blit(text1, (width // 1.55, (height + 100) // 5))

        f4 = pygame.font.Font(None, 30)
        text1 = f4.render('Click on enemy’s bombs', True,
                          (0, 0, 0))
        screen.blit(text1, (width // 1.55, (height + 300) // 5))

        f5 = pygame.font.Font(None, 30)
        text1 = f5.render('to intercept them', True,
                          (0, 0, 0))
        screen.blit(text1, (width // 1.55, (height + 400) // 5))

        f6 = pygame.font.Font(None, 30)
        text1 = f6.render('Click on your own territory', True,
                          (0, 0, 0))
        screen.blit(text1, (width // 1.55, (height + 600) // 5))

        f7 = pygame.font.Font(None, 30)
        text1 = f7.render('to restore HP', True,
                          (0, 0, 0))
        screen.blit(text1, (width // 1.55, (height + 700) // 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ((x-250)**2 + (y-250)**2 <= 200**2):
                    screen.fill(WHITE)
                    circle(screen, (255, 10, 10), (250, 250), 200, 0)
                    circle(screen, (0, 0, 0), (250, 250), 200, 15)

                    f1 = pygame.font.Font(None, 50)
                    text1 = f1.render('DO NOT TOUCH', True,
                                      (0, 0, 0))
                    screen.blit(text1, (width // 7, height // 1.3))

                    f2 = pygame.font.Font(None, 30)
                    text1 = f2.render('Click on enemy’s territory', True,
                                      (0, 0, 0))
                    screen.blit(text1, (width // 1.55, height // 5))

                    f3 = pygame.font.Font(None, 30)
                    text1 = f3.render('to drop the bomb', True,
                                      (0, 0, 0))
                    screen.blit(text1, (width // 1.55, (height + 100) // 5))

                    f4 = pygame.font.Font(None, 30)
                    text1 = f4.render('Click on enemy’s bombs', True,
                                      (0, 0, 0))
                    screen.blit(text1, (width // 1.55, (height + 300) // 5))

                    f5 = pygame.font.Font(None, 30)
                    text1 = f5.render('to intercept them', True,
                                      (0, 0, 0))
                    screen.blit(text1, (width // 1.55, (height + 400) // 5))

                    f6 = pygame.font.Font(None, 30)
                    text1 = f6.render('Click on your own territory', True,
                                      (0, 0, 0))
                    screen.blit(text1, (width // 1.55, (height + 600) // 5))

                    f7 = pygame.font.Font(None, 30)
                    text1 = f7.render('to restore HP', True,
                                      (0, 0, 0))
                    screen.blit(text1, (width // 1.55, (height + 700) // 5))

                    pygame.display.update()
                    pygame.time.wait(500)
                    started = True

        pygame.display.update()
    else:
        clock.tick(FPS)
        time += 1

        hp = Health_Points()
        hpb = Health_Points_Bot()
        print(hp, hpb)
        if (hp < 0.4):
            Bot_Win(screen)
            finished = True

        if (hpb < 0.4):
            Player_Win(screen)
            finished = True

        bot_act(time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if what_field_is(x, y) == 2:
                    # player_name = 'player'
                    # player_name = player()
                    dr_bomb(x, y)
                else:
                    for i in range(17):
                        for j in range(17):
                            k = i - 8
                            n = j - 8
                            if (k * k + n * n <= 64):
                                del_bomb(x + k, y + n)
                    repair(x, y, 1)

                pressed = pygame.mouse.get_pressed()


        # screen.fill(test)
        draw_field(screen)
        draw(time)
        # draw_field_lines(screen)
        pygame.display.update()



pygame.quit()




