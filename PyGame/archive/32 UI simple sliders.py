import pygame, math
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

hue, saturation, value = 100, 70, 80
color = pygame.Color(0, 255, 245)
cube_size = 100

button_size = 50
button_1 = pygame.Rect(50, 100, button_size, button_size)
dragging = False


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        # MOUSE handling
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_1.collidepoint(event.pos):
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                button_1.move_ip(0, event.rel[1])
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("aliceblue")
    
    pygame.draw.rect(screen, color, 
                    (int((screen.get_width()-cube_size)/2),int((screen.get_height()-cube_size)/2), 
                    cube_size, cube_size), 0, 20)
    
    # button
    pygame.draw.rect(screen, "darkorchid", button_1, 0, 5)
    
    color.hsva = (hue, saturation, value)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()