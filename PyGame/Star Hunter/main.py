import pygame

WIDTH, HEIGHT = 1280, 720
palette = {'bg': "#75E7F2",
           '1': "#FF8484"}
running = True


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(WIDTH/2,HEIGHT/2)
player_speed = 300
player_size = 25

def key_input(dt, player_pos, player_speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += player_speed * dt

def edge_wrap(WIDTH, HEIGHT, player_pos):
    player_pos.x %= WIDTH
    player_pos.y %= HEIGHT

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(palette['bg'])
    ### Update ###
    key_input(dt, player_pos, player_speed)
    
    edge_wrap(WIDTH, HEIGHT, player_pos)

    
    ### Draw ###
    pygame.draw.rect(screen, palette['1'], (player_pos.x, player_pos.y, player_size, player_size)) # player

    
    pygame.display.flip()

    dt = clock.tick(60) / 1000
    
pygame.quit()

