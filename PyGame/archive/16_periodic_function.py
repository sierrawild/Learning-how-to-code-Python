# https://bleuje.com/tutorial2/

import pygame
import math
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
screenMultiplication = 70
WIDTH = 16 * screenMultiplication
HEIGHT = 9 * screenMultiplication
FPS = 60
NUM_FRAMES = 60
GRID_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Loop from periodic function and offset")

# Clock for FPS and frame count
clock = pygame.time.Clock()
frame_count = 1

# File handling
SAVE = True
if SAVE:
    pathDir = r"D:\Python\Periodic_function"
    os.makedirs(pathDir, exist_ok=True)
    fileList = os.listdir(pathDir)
    fileDir = os.path.join(pathDir, str(len(fileList)))
    os.makedirs(fileDir, exist_ok=False)
    
    saved = False

# functions

def map_value(value, old_min, old_max, new_min, new_max):
    old_range = old_max - old_min
    new_range = new_max - new_min
    return ((value - old_min) / old_range) * new_range + new_min

def periodic_function(p):
    return map_value(math.sin(2 * math.pi * p), -1, 1, 2, 8)

def offset(x,y):
    center_x, center_y = WIDTH/2, HEIGHT/2
    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
    # TODO Play with the offset to get different effects 
    return 0.05 * distance

# Main game loop
running = True
while running:
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    time = (frame_count - 1) / NUM_FRAMES
    screen.fill(BLACK)
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x = map_value(i, 0, GRID_SIZE - 1, 0, WIDTH)
            y = map_value(j, 0, GRID_SIZE - 1, 0, HEIGHT)
            
            size = periodic_function(time - offset(x, y))
            
            pygame.draw.aacircle(screen, WHITE, (int(x), int(y)), int(size*0.7))
            pygame.draw.rect(screen, WHITE, (int(x), int(y), int(size), int(size)))
    
            
    
    
    
    pygame.display.flip()
    
    if SAVE:
        if frame_count <= NUM_FRAMES and saved == False:
            filename = str(frame_count) + ".png"
            savePath = os.path.join(fileDir, filename)
            pygame.image.save(screen, savePath, )
        if frame_count >= NUM_FRAMES:
            saved = True
            
    frame_count += 1
    if frame_count > NUM_FRAMES:
        frame_count = 1            
    clock.tick(FPS)

pygame.quit()
