import pygame 
import time 
import math
from tools import transform_image

pygame.init()

# [Init Assets] 

# want image to be loaded but also scaled, needs a path and POS 
GROUND = transform_image(pygame.image.load("imgs/ground.png"), 1.5)
PLAYER = transform_image(pygame.image.load("imgs/minotaur.png"), 0.2)

# setup window and display mode 
WIDTH, HEIGHT = GROUND.get_width(), GROUND.get_height()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up game loop and initialize draw to window:  
clock = pygame.time.Clock()
FPS = 60
run = True 

# create array with tuple of <img> and <pos> for win.blit()
# 0,0 starts at top-left corner 
images = [(GROUND, (0,0)),(PLAYER,(0,0))]


# uses array of image tuple info to draw to window
def draw(win, images):
	# img,pos are inside each element of the array as a tuple
	for img, pos in images:
		win.blit(img, pos)

# note constructors are called __init__	
class AbstractCharacter:
	def __init__(self, speed, angle):
		self.speed = 0
		self.angle = angle
		
	
while (run):
	clock.tick(FPS)
	  
#   update is called every frame 
	pygame.display.update()

	draw(WIN, images)

#   component-draws here: 
#	WIN.blit(GROUND, (0,0))
#	WIN.blit(PLAYER, (0,0))
	
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			run = False
			break
#   Get Input Here to reference class movement: 					
	
