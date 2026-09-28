import pygame, random

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
SHAKE_TIME = 1
SHAKE_MAX = 25
# pygame setup
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.Surface((WIDTH, HEIGHT))
xoff, yoff = 0,0
shake_timer = 0

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
            elif event.key == pygame.K_SPACE:
                shake_timer += SHAKE_TIME
    screen.fill("#AEF1AA") # fill the screen with a color to wipe away anything from last frame

    ### UPDATE ###
    if shake_timer > 0:
        shake_timer = max(0, shake_timer-dt)
        magnitude = SHAKE_MAX * (shake_timer / SHAKE_TIME)
        xoff = random.uniform(-magnitude, magnitude)
        yoff = random.uniform(-magnitude, magnitude)
    else:
        xoff, yoff = 0, 0
        
    ### DRAW ###
    for i in range(10):
        for j in range(5):
            pygame.draw.circle(screen, "blue", (150 + 100 * i, 150 + 100 * j), 20)

    # flip() the display to put your work on screen
    window.blit(screen,(xoff, yoff))
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60
    
pygame.quit()