import pygame, os, math
from .objectFunctions import rot_center
from .bullet import Bullet

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, img, parent, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.parent = parent
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = x, y
		self.x, self.y = x, y
		self.angle = 0
		self.turning = 0
		self.forward = 0
		self.speed = 400
		self.vel = 0
		self.shootButton = False
		self.can_shoot = .15
		self.width = width
		self.height = height

	def draw(self, display):
		imageRot, rectRot = rot_center(self.image, self.rect, self.angle)
		display.blit(imageRot, rectRot)


	def update(self, dt):
		self.angle += self.turning * 180 * dt
		if(self.angle > 360):
			self.angle -= 360
		elif(self.angle < 0):
			self.angle += 360

		if self.forward:
			self.vel += self.speed * dt
		elif(self.vel > 0):
			self.vel -= self.speed * dt
		if(self.vel > 400):
			self.vel = 400
		if(self.vel < 0):
			self.vel = 0
		self.x += math.sin(math.radians(self.angle + 180)) * self.vel * dt
		self.y += math.cos(math.radians(self.angle + 180)) * self.vel * dt

		self.rect.x, self.rect.y = self.x, self.y

		if self.rect.y < 50:
			self.y = self.height-50
		if self.rect.y > self.height-50:
			self.y = 50

		if self.rect.x < 50:
			self.x = self.width-50
		if self.rect.x > self.width-50:
			self.x=50



		#Player shoot bullet
		if self.shootButton and (self.can_shoot<=0):
			self.can_shoot=.15
			self.parent.bullets.add(Bullet(self.rect.center[0], self.rect.center[1], self.parent.sprites[3], self.vel, self.angle))

		self.can_shoot -= dt
		