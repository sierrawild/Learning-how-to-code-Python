import pygame
from helpers import *

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Cheese Hunter')
dt = 0

# player
player_pos = pygame.Vector2(WIDTH/2,HEIGHT/2)
player_speed = 620
player_size = 25


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
    screen.fill(palette['bg'])

    ### UPDATE ###
    # player update
    key_input(dt, player_pos, player_speed)
    ### DRAW ###
    pygame.draw.circle(screen, palette['player'], (player_pos.x, player_pos.y), 50)

    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000

    clock.tick(60)  # limits FPS to 60

pygame.quit()