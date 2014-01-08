import pygame, sys

def process(player):
	velocity = 2

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				player.velx = velocity
			if event.key == pygame.K_a:
				player.velx = -velocity
			if event.key == pygame.K_w:
				player.vely = -velocity
			if event.key == pygame.K_s:
				player.vely = velocity


		if event.type == pygame.KEYUP:
			if event.key == pygame.K_d:
				player.velx = 0
			if event.key == pygame.K_a:
				player.velx = 0
			if event.key == pygame.K_w:
				player.vely = 0
			if event.key == pygame.K_s:
				player.vely = 0

	player.rect.x += player.velx
	player.rect.y += player.vely





