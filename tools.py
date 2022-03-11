import pygame 

def transform_image(img, scalar):
	# get size as a tuple of newly scaled image: 
	size = round(img.get_width() * scalar), round(img.get_height() * scalar)
	return pygame.transform.scale(img, size)
