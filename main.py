import pygame
from process import process
from classes import *

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 800, 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)


clock = pygame.time.Clock()
FPS = 24


player = Player(SCREENWIDTH / 2.0 - 25, SCREENHEIGHT - 47, "images/player1.bmp")

total_frames = 0

color = 0
delta = 5

while True:
	process(player)

	player.motion(SCREENWIDTH, SCREENHEIGHT)

	total_frames += 1

	color += delta
	if color == 255:
		delta = -5
	elif color == 0:
		delta = 5
	else:
		pass

	screen.fill((color,color,color))
	BaseClass.all_sprites.draw(screen)


	pygame.display.flip()
	clock.tick(FPS)