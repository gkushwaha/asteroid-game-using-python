import pygame, random
from .objectFunctions import rot_center


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, vel_x, vel_y, img, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.x, self.y = x, y
        self.angle = random.randrange(360)
        self.angle_spd = random.randrange(-360, 360)
        self.forward = 0
        self.speed = 400
        self.vel_x, self.vel_y = vel_x, vel_y
        self.width = width
        self.height = height
    def update(self, dt):

        self.angle += self.angle_spd * dt
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt
        self.rect.x = self.x
        self.rect.y = self.y

        if self.rect.y < 50:
            self.y = self.height-50
        if self.rect.y > self.height-50:
            self.y = 50

        if self.rect.x < 50:
            self.x = self.width-50
        if self.rect.x > self.width-50:
            self.x=50

    def draw(self, display):
        imageRot, rectRot = rot_center(self.image, self.rect, self.angle)
        display.blit(imageRot, rectRot)
