import pygame, math
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

hue, saturation, value = 100, 70, 80
color = pygame.Color(0, 255, 245)
cube_size = 100



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("aliceblue")
    
    pygame.draw.rect(screen, color, (int((screen.get_width()-cube_size)/2),int((screen.get_height()-cube_size)/2), cube_size, cube_size))
    
    color.hsva = (hue, saturation, value)
    
    # Using mouse to influence colors
    pos = pygame.mouse.get_pos()
    hue = pos[0] %360
    value = (pos[1]* 0.1) % 100
    print(pos)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()