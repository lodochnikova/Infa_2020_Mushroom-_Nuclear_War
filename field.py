import pygame
from pygame.draw import *
SCREEN_X = 800
SCREEN_Y = 600
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
LINES_WIDTH = 2
N = 10

FPS = 30

def draw_field(screen, n = 2, SCREEN_X = 800, SCREEN_Y = 600):
	surface = pygame.Surface((SCREEN_X, SCREEN_Y), pygame.SRCALPHA)
	rect = pygame.draw.rect(surface, GREEN, (0, 0, SCREEN_X, SCREEN_Y))
	line = pygame.draw.line(surface, WHITE, (SCREEN_X / 2, 0), (SCREEN_X / 2, SCREEN_Y), LINES_WIDTH)
	field_height = SCREEN_Y * 2 // n
	temp = field_height
	for i in range(1, n // 2, 1):
		line = pygame.draw.line(surface, WHITE, (0, temp), (SCREEN_X, temp), LINES_WIDTH)
		temp += field_height
	screen.blit(surface,(0, 0))
	pygame.display.update()

def what_field_is(x, y):
	player_number = 1
	if x > SCREEN_X / 2:
		player_number = N // 2 + 1
	field_height = SCREEN_Y * 2 // N
	temp = 0
	for i in range(0, N // 2, 1):
		if (y >= temp) and (y <= temp + field_height):
			player_number += i
			break
		temp += field_height
	return player_number
#pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
draw_field(screen, N, SCREEN_X, SCREEN_Y)

clock = pygame.time.Clock()
finished = False
#print(what_field_is(700, 300))
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()