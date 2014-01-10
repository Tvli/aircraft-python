import pygame, math


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

	def destroy(self, ClassName):
		ClassName.List.remove(self)
		BaseClass.all_sprites.remove(self)
		del self


class Player(BaseClass):
	List = pygame.sprite.Group()
	spare_list = []

	def __init__(self, x, y, image_string):
		BaseClass.__init__(self, x, y, image_string)
		Player.List.add(self)
		Player.spare_list.append(self)
		self.velx, self.vely = 0, 0
		self.score = 0

	def get_score(self):
		self.score += 100


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


class Flight(BaseClass):
	List = pygame.sprite.Group()
	def __init__(self, x, y, image_string):
		BaseClass.__init__(self, x, y, image_string)
		Flight.List.add(self)
		self.health = 100
		self.velx, self.vely = 0, 2

	def fly(self, SCREENHEIGHT):
		self.rect.y += self.vely


	@staticmethod
	def update(SCREENHEIGHT):
		for flight in Flight.List:
			flight.fly(SCREENHEIGHT)

			if flight.rect.y > SCREENHEIGHT:
				flight.destroy(Flight)



class Bullet(pygame.sprite.Sprite):
	List = pygame.sprite.Group()
	spare_list = []

	def __init__(self, x, y, image_string):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_string)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.velx, self.vely = 0, -15

		try:
			last_element = Bullet.spare_list[-1]
			difference = abs(self.rect.y - last_element.rect.y)

			if difference < self.rect.height + 50:
				return
		except Exception:
			pass

		Bullet.spare_list.append(self)
		Bullet.List.add(self)


	@staticmethod
	def movement():
		for bullet in Bullet.List:
			bullet.rect.y += bullet.vely


	def destroy(self):
		Bullet.List.remove(self)
		Bullet.spare_list.remove(self)
		del self




















