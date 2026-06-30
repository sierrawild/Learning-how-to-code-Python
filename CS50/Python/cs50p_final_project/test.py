import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

x = 0
# Font 
font = pygame.font.SysFont("arial", 50)
font = pygame.font.Font(None, 50)

# print(pygame.font.get_fonts()) # print sys fonts



# main loop
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

    # RENDER YOUR GAME HERE
    
    x += 1
    text_surface = font.render(f'Hello, World! {int(x)}', antialias=True, color='white')
    w, h = text_surface.get_size()
    padding = 20
    backdrop = pygame.draw.rect(screen, 'black', (1280/2 - padding, 720/2 - padding, w + padding*2, h + padding*2), 0, 10)
    screen.blit(text_surface, (1280/2, 720/2))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()