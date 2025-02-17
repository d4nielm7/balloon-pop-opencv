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


# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    
    # Apply Logic
    window.fill((255, 255, 255))
    window.blit(imgBG,(0,0)) 
    window.blit(imgBalloonRed,(200,300))

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
