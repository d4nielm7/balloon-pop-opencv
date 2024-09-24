"""
Rect

    Can detect Collisions
    Can access x and y points

    Two way of creating a rect
    1. pygame.Rect(,x,y,width,height)
    2. surface.get_rect() #creates rect around a surface/image


"""




#import
import pygame

#Initialize

pygame.init()

#Create Window
width, height = 1280,720
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("My Awesome Game")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

#Load Images
imgBG = pygame.image.load("../Resources/bg-sky.png").convert_alpha() 
imgBalloonRed = pygame.image.load("../Resources/balloon-red.png").convert_alpha() 
imgBalloonRed_small = pygame.transform.smoothscale(imgBalloonRed, (int(imgBalloonRed.get_width() * 0.2), int(imgBalloonRed.get_height() * 0.2)))
rectBalloon = imgBalloonRed_small.get_rect()

#Rect

rectNew = pygame.Rect(500,0,200,200)


# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    
    # Apply Logic
    print(rectBalloon.colliderect(rectNew))
    rectBalloon.x +=2

    window.blit(imgBG,(0,0)) 
    
    #pygame.draw.rect(window,(0,255,0), rectBalloon)
    #pygame.draw.rect(window,(0,255,0), rectNew)
    window.blit(imgBalloonRed_small, rectBalloon)

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
