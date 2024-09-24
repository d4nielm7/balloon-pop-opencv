import random
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize Pygame
pygame.init()

# Create Window
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Pop")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# Load Images
imgBalloonRed = pygame.image.load('../Resources/balloon-red.png').convert_alpha()
imgBalloonRed_small = pygame.transform.smoothscale(
    imgBalloonRed, (int(imgBalloonRed.get_width() * 0.2), int(imgBalloonRed.get_height() * 0.2))
)
rectBalloon = imgBalloonRed_small.get_rect()
rectBalloon.x, rectBalloon.y = 500, 500

# Variables
speed = 10
score = 0
startTime = time.time()
totalTime = 30

# Tracking variables
hand_detected_count = 0  # For hand detection accuracy
total_frames = 0         # Total frames processed
balloon_popped_count = 0  # Number of balloons popped
balloon_missed_count = 0  # Number of balloons missed

# Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Function to reset balloon position
def resetBalloon():
    rectBalloon.x = random.randint(100, img.shape[1] - 100)
    rectBalloon.y = img.shape[0] + 50

# Main loop
start = True
while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()
    
    # Calculate remaining time
    timeRemain = int(totalTime - (time.time() - startTime))
    
    if timeRemain < 0:
        window.fill((255, 255, 255))
        
        # Calculate and display metrics
        if total_frames > 0:
            detection_accuracy = (hand_detected_count / total_frames) * 100
        else:
            detection_accuracy = 0

        total_attempts = balloon_popped_count + balloon_missed_count
        if total_attempts > 0:
            popping_success_rate = (balloon_popped_count / total_attempts) * 100
        else:
            popping_success_rate = 0

        font = pygame.font.Font(None, 50)  # Use default system font
        textScore = font.render(f'Your Score is: {score}', True, (50, 50, 50))
        textTime = font.render(f'Time\'s Up', True, (50, 50, 50))
        textAccuracy = font.render(f'Hand Detection Accuracy: {detection_accuracy:.2f}%', True, (50, 50, 50))
        textPoppingRate = font.render(f'Balloon Popping Success Rate: {popping_success_rate:.2f}%', True, (50, 50, 50))

        window.blit(textScore, (450, 350))
        window.blit(textTime, (530, 275))
        window.blit(textAccuracy, (450, 400))
        window.blit(textPoppingRate, (450, 450))
    else:
        # OpenCV operations
        success, img = cap.read()
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)

        # Increment frame count
        total_frames += 1

        # Move balloon up
        rectBalloon.y -= speed

        # Reset balloon if it reaches the top
        if rectBalloon.y < 0:
            balloon_missed_count += 1  # Track missed balloons
            resetBalloon()
            speed += 1

        # Check hand and balloon collision
        if hands:
            hand_detected_count += 1  # Track successful hand detections
            hand = hands[0]
            x, y = hand['lmList'][8][:2]  # Extract (x, y) of index finger tip
            if rectBalloon.collidepoint(x, y):
                balloon_popped_count += 1  # Track successful balloon pops
                resetBalloon()
                score += 10
                speed += 1

        # Display the frame from OpenCV in Pygame window
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = np.rot90(imgRGB)
        frame = pygame.surfarray.make_surface(imgRGB).convert()
        frame = pygame.transform.flip(frame, True, False)
        window.blit(frame, (0, 0))

        # Draw the balloon
        window.blit(imgBalloonRed_small, rectBalloon)

        # Render the score and time
        font = pygame.font.Font(None, 50)  # Use default system font
        textScore = font.render(f'Score: {score}', True, (50, 50, 50))  # Black text
        textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 50))  # Black text
        window.blit(textScore, (35, 35))
        window.blit(textTime, (1000, 35))

    # Update Display
    pygame.display.update()

    # Set FPS
    clock.tick(fps)

