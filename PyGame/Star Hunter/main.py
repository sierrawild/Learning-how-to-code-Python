import pygame

width, height = 1280, 720
palette = {'bg': "#75E7F2",
           '1': "#FF8484"}


pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
dt = 0

player_pos = pygame.Vector2(width/2,height/2)
player_speed = 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(palette['bg'])
    
    # player
    pygame.draw.circle(screen, palette['1'], player_pos, 40)

    # key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_s]:
        player_pos.y += player_speed * dt
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_d]:
        player_pos.x += player_speed * dt
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000
    
pygame.quit()

