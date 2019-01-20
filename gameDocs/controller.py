import pygame, os, random
from .player import Player
from .debri import Debri
from .asteroid import Asteroid
from .bullet import Bullet
from .gui import Gui
from .database import Database

PLAYER_SPRITE = 0
ASTEROID_SPRITE_MEDIUM = 1
DIRT_SPRITE = 2
BULLET_SPRITE = 3
ASTEROID_SPRITE_LARGE = 4
ASTEROID_SPRITE_SMALL = 5


class Controller:
	def __init__(self):
		self.sprites = []
		self.bullet_count_big = 0
		self.bullet_count_medium = 0
		self.bullet_count_small = 0
		self.asteroids_01 = pygame.sprite.Group()
		self.asteroids_02 = pygame.sprite.Group()
		self.asteroids_03 = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		self.debri = pygame.sprite.Group()

		self.loadResources()

		self.screen_width = 800
		self.screen_height = 600

		self.display = pygame.display.set_mode((self.screen_width,self.screen_height))
		pygame.display.set_caption('Asteroids')

		self.theGui = Gui()
		self.thePlayer = Player(50, 50, self.sprites[PLAYER_SPRITE], self, self.screen_width, self.screen_height)
		self.asteroids_02.add(Asteroid(100,200, random.randrange(-25, 25),-50, self.sprites[ASTEROID_SPRITE_MEDIUM], self.screen_width, self.screen_height))
		self.asteroids_03.add(Asteroid(400,500, random.randrange(-25, 25),-50, self.sprites[ASTEROID_SPRITE_LARGE], self.screen_width, self.screen_height))
		self.asteroids_01.add(Asteroid(250,300, random.randrange(-25, 25),-50, self.sprites[ASTEROID_SPRITE_SMALL], self.screen_width, self.screen_height))

	def loadResources(self):
		self.sprites.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'player.png')))
		self.sprites.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'ASTEROID_SPRITE_MEDIUM.png')))
		self.sprites.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'dirt.png')))
		self.sprites.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'bullet1.png')))
		self.sprites.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'ASTEROID_SPRITE_BIG.png')))
		self.sprites.append(pygame.image.load(os.path.join(os.path.dirname(__file__),'ASTEROID_SPRITE_SMALL.png')))

	def eventHandle(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return True
			#if event.type == pygame.KEYDOWN:
		keys = pygame.key.get_pressed()
		self.thePlayer.turning = keys[pygame.K_LEFT] - keys[pygame.K_RIGHT]
		self.thePlayer.forward = keys[pygame.K_UP]
		self.thePlayer.shootButton = keys[pygame.K_SPACE]

		return False
	def update(self, dt):
		self.thePlayer.update(dt)
		bulletstoremove = []
		debritoremove = []
		asteroidtoremove = []

		for a in self.asteroids_01.sprites():
			a.update(dt)
		for a in self.asteroids_02.sprites():
			a.update(dt)
		for a in self.asteroids_03.sprites():
			a.update(dt)

		for a in self.bullets.sprites():
			a.update(dt)
			if(a.timetodie <= 0):
				bulletstoremove.append(a)
		for a in self.debri.sprites():
			a.update(dt)
			if(a.timetodie <= 0):
				debritoremove.append(a)

		
		collide_list_big = pygame.sprite.groupcollide(self.asteroids_03, self.bullets, False, True)

		if len(collide_list_big)>0:
			self.bullet_count_big +=1
		
		if (self.bullet_count_big == 15):
			for i in collide_list_big:
				self.createDebri(i)
				self.theGui.score += 5
				self.asteroids_03.remove(i)
				self.asteroids_02.add(Asteroid(400,500, random.randrange(-25, 25),-50, self.sprites[ASTEROID_SPRITE_MEDIUM], self.screen_width, self.screen_height))
				self.asteroids_01.add(Asteroid(250,300, random.randrange(-25, 25),-50, self.sprites[ASTEROID_SPRITE_SMALL], self.screen_width, self.screen_height))
			collide_list_big = 0

		collide_list_medium = pygame.sprite.groupcollide(self.asteroids_02, self.bullets, False, True)

		if len(collide_list_medium)>0:
			self.bullet_count_medium +=1
		
		if (self.bullet_count_medium == 7):
			for i in collide_list_medium:
				self.theGui.score += 5
				self.createDebri(i)
				self.asteroids_02.remove(i)
				self.asteroids_01.add(Asteroid(250,300, random.randrange(-25, 25),-50, self.sprites[ASTEROID_SPRITE_SMALL], self.screen_width, self.screen_height))
			self.bullet_count_medium = 0


		collide_list_small = pygame.sprite.groupcollide(self.asteroids_01, self.bullets, False, True)

		if len(collide_list_small)>0:
			self.bullet_count_small +=1
		
		if (self.bullet_count_small == 4):
			for i in collide_list_small:
				self.theGui.score += 5
				self.createDebri(i)
				self.asteroids_01.remove(i)
			self.bullet_count_small = 0
				

				
		collide_player_small = pygame.sprite.spritecollide(self.thePlayer, self.asteroids_01, False)
		collide_player_medium = pygame.sprite.spritecollide(self.thePlayer, self.asteroids_02, False)
		collide_player_big = pygame.sprite.spritecollide(self.thePlayer, self.asteroids_03, False)

		if (collide_player_small or collide_player_medium or collide_player_big):
			pygame.quit()
			Database(self.theGui.score)
			quit()
		

		for i in bulletstoremove:
			self.bullets.remove(i)
	
		for i in debritoremove:
			self.debri.remove(i)
			
		#If there is anything in the collide_list, create the debri for it
		# and subtract 5 from score

		#for i in collide_list:
		#	self.createDebri(i)

		'''if(len(collide_list) > 0):
			for i in collide_list:
				self.createDebri(i)
			self.theGui.score -= 5'''


	def draw(self):

		self.display.fill((0,0,0))

		for a in self.debri.sprites():
			a.draw(self.display)
		for a in self.asteroids_01.sprites():
			a.draw(self.display)
		for a in self.asteroids_02.sprites():
			a.draw(self.display)
		for a in self.asteroids_03.sprites():
			a.draw(self.display)
		for a in self.bullets.sprites():
			a.draw(self.display)

		self.thePlayer.draw(self.display)

		self.theGui.draw(self.display)
		pygame.display.flip()
	def createDebri(self, asteroid):
		for i in range(40):
			self.debri.add(Debri(asteroid.rect.center, self.sprites[DIRT_SPRITE]))
