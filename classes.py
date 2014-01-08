import pygame


class BaseClass(pygame.sprite.Sprite):
	all_sprites = pygame.sprite.Group()

	def __init__(self, x, y, image_string):
		pygame.sprite.Sprite.__init__(self)
		BaseClass.all_sprites.add(self)

		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.rect.width
		self.rect.height 


class Player(BaseClass):
	List = pygame.sprite.Group()

	def __init__(self, x, y, image_string):
		BaseClass.__init__(self, x, y, image_string)
		Player.List.add(self)
		self.velx, self.vely = 0, 0


	def motion(self, SCREENWIDTH, SCREENHEIGHT):
		predicted_x_location = self.rect.x + self.velx
		predicted_y_location = self.rect.y + self.vely

		if predicted_x_location < 0:
			self.velx = 0
		elif predicted_x_location + self.rect.width > SCREENWIDTH:
			self.velx = 0
		elif predicted_y_location < 0:
			self.vely = 0
		elif predicted_y_location + self.rect.height > SCREENHEIGHT:
			self.vely = 0
		else:
			self.rect.x += self.velx
			self.rect.y += self.vely
















