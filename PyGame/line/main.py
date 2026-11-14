import pygame
from settings import WIDTH, HEIGHT, palette


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Line')
clock = pygame.time.Clock()
dt = 0

running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    # Update
    
    # Draw
    screen.fill(palette['bg'])
    
    pygame.draw.aacircle(screen,palette['1'], (500,400), 200)
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
pygame.quit()