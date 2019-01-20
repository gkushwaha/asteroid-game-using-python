import pygame, random
from .objectFunctions import rot_center

class Debri(pygame.sprite.Sprite):
    def __init__(self, placement_center, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = placement_center

        self.x, self.y = (self.rect.x + random.randrange(-10,10)), (self.rect.y + random.randrange(-10,10))
        self.angle = 0
        self.timetodie = random.randrange(100,300)/100
        self.xVel, self.yVel = random.randrange(-50,50), random.randrange(-50,50)
        #print("Created Debri")
    def update(self, dt):
        self.x += self.xVel * dt
        self.y += self.yVel * dt
        self.rect.x = self.x
        self.rect.y = self.y
        self.timetodie -= dt
    def draw(self, display):
        imageRot, rectRot = rot_center(self.image, self.rect, self.angle)
        display.blit(imageRot, rectRot)
