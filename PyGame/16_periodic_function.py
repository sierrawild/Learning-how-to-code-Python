# https://bleuje.com/tutorial2/

import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screenMultiplication = 60
WIDTH = 9 * screenMultiplication
HEIGHT = 16 * screenMultiplication
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
    return 0.01 * distance

# Main game loop
running = True
while running:
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    time = (frame_count - 1) / NUM_FRAMES
    screen.fill(WHITE)
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            x = map_value(i, 0, GRID_SIZE - 1, 0, WIDTH)
            y = map_value(j, 0, GRID_SIZE - 1, 0, HEIGHT)
            
            size = periodic_function(time - offset(x, y))
            
            pygame.draw.aacircle(screen, BLACK, (int(x), int(y)), int(size*0.6))
            
            
    frame_count += 1
    
    if frame_count > NUM_FRAMES:
        frame_count = 1            
    
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
