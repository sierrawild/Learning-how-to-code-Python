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

# cheese
cheese_pos = random_teleport(WIDTH,HEIGHT, player_size)
score = 0

# walls
walls = walls(WIDTH, HEIGHT)
    
# font
score_font = pygame.font.Font(None, 40)
score_surf = score_font.render(str(score), True, palette['text'])


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
    movement = key_input(dt, player_pos, player_speed)
    player_rect = player_collisions(player_pos, player_size, walls, movement)
    
    # cheese
    cheese = pygame.Rect(cheese_pos.x, cheese_pos.y, int(player_size * 0.7), int(player_size * 0.7))
    if cheese.collidelist(walls) != -1:
        cheese_pos = random_teleport(WIDTH,HEIGHT, player_size)
    # score
    if cheese.colliderect(player_rect):
        score += 1
        score_surf = score_font.render(str(score), True, palette['text'])
        cheese_pos = random_teleport(WIDTH,HEIGHT, player_size)
    cheese = pygame.Rect(cheese_pos.x, cheese_pos.y, int(player_size * 0.7), int(player_size * 0.7))
        
    ### DRAW ###
    # player
    pygame.draw.rect(screen, palette['player'], player_rect)

    # cheese
    pygame.draw.rect(screen, palette['cheese'], cheese)
    
    # walls
    for wall in walls:
        pygame.draw.rect(screen,palette['wall'], wall)

    
    
    # flip() the display to put your work on screen
    screen.blit(score_surf, (50,50))
    pygame.display.flip()


    dt = clock.tick(60) / 1000


pygame.quit()