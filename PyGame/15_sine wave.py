import pygame, math

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

screen.fill("#FFF9C9")

time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

time += 1

# make different example of sine wave up and down with different multipliers giving different effects 

pygame.display.flip()
clock.tick(60)            
            
pygame.quit()