import pygame

pygame.init()

width = 1280
height = 720
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()


tryingToQuit = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if tryingToQuit < 3:
                width += 20
                height += 20
                tryingToQuit += 1
                screen = pygame.display.set_mode((width, height))
            elif tryingToQuit < 5:
                tryingToQuit += 1
                running = False
            else:
                running = False
                

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
    
    screen.fill("#FFDBDB")
    
    
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()