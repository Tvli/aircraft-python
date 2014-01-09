import pygame, sys, random, classes

def process(player, FPS, total_frames, SCREENWIDTH):
	velocity = 10

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

	keys = pygame.key.get_pressed()

	if keys[pygame.K_SPACE]:
		classes.Bullet(player.rect.x, player.rect.y, "images/bullet.png")


	Create_Flight(FPS, total_frames, SCREENWIDTH)


def Create_Flight(FPS, total_frames, SCREENWIDTH):
	three_second = FPS * 3
	if total_frames % three_second == 0:
		x = random.randint(1, SCREENWIDTH - 50)
		classes.Flight(x, -20, "images/craft.jpg")






