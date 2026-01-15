import pygame
import random

pygame.init()

WIDTH = 1280
HEIGHT = 720
fps = 1
fps_direction = "up"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    # quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    
    
    screen.fill("#FFDBDB")
    spacing = 22
    for i in range(0,WIDTH , spacing):
        for j in range(0,HEIGHT, spacing):
            color = (random.randrange(20,220), random.randrange(20,220), random.randrange(20,220))
            if i > WIDTH / 2 and j > HEIGHT / 2:
                color = (random.randrange(0,255), 255, 255)
            elif i > WIDTH / 2:
                color = (255, random.randrange(0,180), 255)
            elif j > HEIGHT / 2:
                color = (255, 255, random.randrange(0, 255))
                
            pygame.draw.rect(screen, color, (i, j, 20, 20))
    
    
    pygame.display.flip()
    
    
    
    if fps_direction == "up":
        fps +=1    
    else:
        fps -=1
        
    if fps == 60:
        fps_direction = "down"
    elif fps == 1:
        fps_direction = "up"
        
        
    clock.tick(fps)

pygame.quit()