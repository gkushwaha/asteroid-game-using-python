import pygame, math
from .objectFunctions import rot_center

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, img, vel, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.x, self.y = x, y
        self.timetodie = 2
        self.thrust = 100  + vel
        self.angle = angle
        self.velx = math.sin(math.radians(self.angle + 180)) * self.thrust
        self.vely = math.cos(math.radians(self.angle + 180)) * self.thrust
    def update(self, dt):
        self.timetodie -= dt
        self.x += self.velx *dt
        self.y += self.vely *dt
        self.rect.x, self.rect.y = self.x, self.y
       

    def draw(self, screen):
        imageRot, rectRot = rot_center(self.image, self.rect, self.angle)
        screen.blit(imageRot, rectRot)

