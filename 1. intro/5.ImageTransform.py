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
imgBG = pygame.image.load("../Resources/bg-sky.png").convert() 
imgBalloonRed = pygame.image.load("../Resources/balloon-red.png").convert_alpha() 
#imgBalloonRed = pygame.transform.rotate(imgBalloonRed, 90)
imgBalloonRed = pygame.transform.rotozoom(imgBalloonRed, 90,0.3)
#imgBalloonRed = pygame.transform.flip(imgBalloonRed,True,False)


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

    imgBalloonRed_small = pygame.transform.smoothscale(imgBalloonRed, (int(imgBalloonRed.get_width() * 0.2), int(imgBalloonRed.get_height() * 0.2)))
    window.blit(imgBG,(0,0)) 
    window.blit(imgBalloonRed_small,(200,300))

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)
