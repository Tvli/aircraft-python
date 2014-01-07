import pygame

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 1024, 768
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

clock = pygame.time.Clock()
FPS = 24

total_frames = 0

while True:
	total_frames += 1

	pygame.display.flip()
	clock.tick.(FPS)