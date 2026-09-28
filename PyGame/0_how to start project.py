import pygame

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Name of the game')
clock = pygame.time.Clock()
dt = 0

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
    screen.fill("#AEF1AA") # fill the screen with a color to wipe away anything from last frame

    

    ### UPDATE ###
    
    
    
    ### DRAW ###
    pygame.draw.circle(screen, "red", (640, 360), 50)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60
    
pygame.quit()