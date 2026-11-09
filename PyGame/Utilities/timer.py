import pygame

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('timer')
clock = pygame.time.Clock()
dt = 0

color_og = "#FF9669"
color_nw = "#0096FF"
color = color_og

timer_start = 0
timer_time_passed = 0
timer_on = False

running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Close the window by pressing ESCAPE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                color = color_nw
                timer_on = True
                timer_start = pygame.time.get_ticks()
    ### UPDATE ###
    if timer_on:
        timer_time_passed = pygame.time.get_ticks()
    if timer_time_passed - timer_start > 2000:
        color = color_og
    
    ### DRAW ###
    screen.fill("#AEF1AA") # fill the screen with a color to wipe away anything from last frame

    pygame.draw.circle(screen, color, (640, 360), 50)

    pygame.display.flip()     # put your work on screen
    dt = clock.tick(60) / 1000 # limits FPS to 60
    
pygame.quit()