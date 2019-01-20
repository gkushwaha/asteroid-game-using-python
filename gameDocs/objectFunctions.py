#Object Fucntions
import pygame


# Takes a clean image, rectangle and angle and returns the rotated image with
# same center point
def rot_center(image, rect, angle):
	rot_image = pygame.transform.rotate(image, angle)
	rot_rect = rot_image.get_rect(center=rect.center)
	return rot_image, rot_rect
