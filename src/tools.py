import pygame 

# round() just 'rounds' to an int which is needed over dec vals
def transform_image(img, scalar):
	# get size as a tuple of newly scaled image: 
	size = round(img.get_width() * scalar), round(img.get_height() * scalar)
	return pygame.transform.scale(img, size)

# //
# function to take an image and rotate it based on an angle
# needs a surface ref: win, & top_left for? 
# gotta do this bc pygame makes it a rectangle around it
# // 
def rotate_image(win, img, top_left, angle):

	# note this will only rotate around top_left corner
    processedImage=pygame.transform.rotate(img, angle)

    # rotate around center w/o changing x/y onscreen: 
    newRect = processedImage.get_rect(center=processedImage.get_rect(topLeft = top_left).center)
    
    # draw both images: why ? 
    # because it's a surface to another surface - blit(surf1, surf2)
    # the new rects top left is an x,y we need for the processedimage 
    # we use old image to keep the same image but different centers   
    win.blit(processedImage, newRect.topLeft)
	
