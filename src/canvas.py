import pygame 
import time 
import math
from tools import transform_image

pygame.init()

# [Init Assets] 

# want image to be loaded but also scaled, needs a path and POS 
GROUND = transform_image(pygame.image.load("imgs/ground.png"), 1.5)

# setup window and display mode 
WIDTH, HEIGHT = GROUND.get_width(), GROUND.get_height()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up game loop and initialize draw to window:  

clock = pygame.time.Clock()
FPS = 60
run = True 

while (run):
	clock.tick(FPS)
	
	pygame.display.update()
	
	WIN.blit(GROUND, (0,0))
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			run = False
			break
