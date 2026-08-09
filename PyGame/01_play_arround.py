import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

dt = 0
speed = 300
p_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Close the window by pressing ESCAPE
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#AEF1AA")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p_pos.y -= speed * dt
    if keys[pygame.K_DOWN]:
        p_pos.y += speed * dt
    if keys[pygame.K_LEFT]:
        p_pos.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        p_pos.x += speed * dt
    
    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", p_pos, 50)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()