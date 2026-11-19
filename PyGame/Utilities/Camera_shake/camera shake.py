import pygame, random

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0

cam = Camera()
xoff, yoff = 0,0
shake_timer = 0

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
SHAKE_TIME = 1
SHAKE_MAX = 25
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
    pygame.draw.circle(screen, "red", (640 - cam.x + xoff, 360 - cam.y + yoff), 50)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60
    
pygame.quit()