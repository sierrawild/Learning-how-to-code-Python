import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 1080))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT \
        or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
            
    screen.fill("#7AA0AD")
    pygame.display.flip()
    
    
    clock.tick(60)
    
pygame.quit()
    
