import pygame
from gameDocs import *

pygame.init()
pygame.font.init()

gameController = Controller()

clock = pygame.time.Clock()


finished = False

while not finished:
	dt = clock.tick(120)
	finished = gameController.eventHandle()
	gameController.update(dt/1000)
	gameController.draw()
