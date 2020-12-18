import pygame
from CONST import *

def Bot_Win(screen):
	#Вывести надпись на случай поражения игрока
	screen.fill((0,255,0))
	f1 = pygame.font.Font(None, 70)
	text1 = f1.render('You lose!', True,
	                  (255, 0, 0))
	screen.blit(text1, (width//2.5, height//2.5))
	pygame.display.update()
	pygame.time.wait(3000)
	pygame.quit()

def Player_Win(screen):
	#Вывести надпись на случай победы игрока
	screen.fill((0,255,0))
	f1 = pygame.font.Font(None, 70)
	text1 = f1.render('You win!', True,
	                  (0, 0, 0))
	screen.blit(text1, (width//2.5, height//2.5))
	pygame.display.update()
	pygame.time.wait(3000)
	pygame.quit()