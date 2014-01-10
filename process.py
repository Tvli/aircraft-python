import pygame, sys, random, classes

pygame.mixer.init()


def process(player, FPS, total_frames, SCREENWIDTH):
	velocity = 10
	
	bullet_sound = pygame.mixer.Sound("audio/bullet.wav")
	bullet_sound.set_volume(0.3)
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
		bullet_sound.play()
		classes.Bullet(player.rect.x, player.rect.y, "images/bullet.png")


	Create_Flight(FPS, total_frames, SCREENWIDTH)
	Collisions()



def Create_Flight(FPS, total_frames, SCREENWIDTH):
	three_second = FPS * 3
	if total_frames % three_second == 0:
		x = random.randint(1, SCREENWIDTH - 50)
		classes.Flight(x, -20, "images/craft.jpg")


def Collisions():
	collision_sound = pygame.mixer.Sound("audio/explosion.wav")
	collision_sound.set_volume(0.5)
	for flight in classes.Flight.List:
		if pygame.sprite.spritecollide(flight, classes.Bullet.List, True):
			collision_sound.play()
			flight.health -= 50
			if flight.health == 0:
				classes.Player.spare_list[0].get_score()
				flight.destroy(classes.Flight)
			else:
				flight.image = pygame.image.load("images/explosion.png")
				flight.vely -= 1


	for bullet in classes.Bullet.List:
		if pygame.sprite.spritecollide(bullet, classes.Flight.List, False):
			bullet.rect.y += 600
			bullet.destroy()


def gameover():
	for player in classes.Player.List:
		if pygame.sprite.spritecollide(player, classes.Flight.List, False):
			return True















