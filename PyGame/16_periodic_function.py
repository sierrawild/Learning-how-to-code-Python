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

# circle settings 
size = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Loop from periodic function and offset")

# Clock for FPS
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)
    
    for j in range(int(HEIGHT / size)):
        for i in range(int(WIDTH/size)):
            pygame.draw.aacircle(screen, BLACK, (i * size*2.3,j * size*2.3), size)
    
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
