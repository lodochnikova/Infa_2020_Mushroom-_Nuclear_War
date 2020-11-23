import pygame
from pygame.draw import *
from CONST import *
"""
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
LINES_WIDTH = 2
"""
def draw_field(screen, n = N, SCREEN_X = width, SCREEN_Y = height):
	rect = pygame.draw.rect(screen, GREEN, (0, 0, SCREEN_X, SCREEN_Y))
	"""
	line = pygame.draw.line(screen, WHITE, (SCREEN_X / 2, 0), (SCREEN_X / 2, SCREEN_Y), LINES_WIDTH)
	field_height = SCREEN_Y * 2 // n
	temp = field_height
	for i in range(1, n // 2, 1):
		line = pygame.draw.line(screen, WHITE, (0, temp), (SCREEN_X, temp), LINES_WIDTH)
		temp += field_height
    """
def draw_field_lines(screen, n = N, SCREEN_X = width, SCREEN_Y = height):
	line = pygame.draw.line(screen, WHITE, (SCREEN_X / 2, 0), (SCREEN_X / 2, SCREEN_Y), LINES_WIDTH)
	field_height = SCREEN_Y * 2 // n
	temp = field_height
	for i in range(1, n // 2, 1):
		line = pygame.draw.line(screen, WHITE, (0, temp), (SCREEN_X, temp), LINES_WIDTH)
		temp += field_height

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
