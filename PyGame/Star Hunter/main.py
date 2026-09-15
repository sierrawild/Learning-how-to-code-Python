import pygame, random

WIDTH, HEIGHT = 1280, 720
palette = {'bg': "#75E7F2",
           'player': "#FF8484",
           'star': "#FFF835",
           'text': "#F5A237"
           }
running = True


pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
dt = 0

speed = 1
speed_up = {5: 1.1, 15: 1.2, 30: 1.3, 50:1.4, 100:1.5}
# player data
player_pos = pygame.Vector2(WIDTH/2,HEIGHT/2)
player_speed = 300
player_size = 25

points = 0

# font
font = pygame.font.Font(None, 36)
text_surf = font.render(str(points), True, palette['text'])

def random_teleport(WIDTH,HEIGHT, size):
    return pygame.Vector2(random.randint(0 + size,WIDTH - size), random.randint(0 + size,HEIGHT - size))
# enemies and pickups
star_pos = random_teleport(WIDTH,HEIGHT, player_size)


def key_input(dt, player_pos, player_speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= player_speed * dt * speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += player_speed * dt * speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= player_speed * dt * speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += player_speed * dt * speed


def edge_wrap(WIDTH, HEIGHT, player_pos):
    player_pos.x %= WIDTH
    player_pos.y %= HEIGHT
    
    # add peaking from the other side here 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            
    screen.fill(palette['bg'])
    ### Update ###
    # player related update
    player_rec = pygame.Rect(player_pos.x, player_pos.y, player_size, player_size)
    key_input(dt, player_pos, player_speed)
    edge_wrap(WIDTH, HEIGHT, player_pos)
    

    # star related update
    star_rec = pygame.Rect(star_pos.x, star_pos.y, int(player_size * 0.7), int(player_size * 0.7))
    
    # speed up logic
    for i in speed_up:
        if points == i:
            speed = speed_up[i]
            
    # collision
    if player_rec.colliderect(star_rec):
        points += 1
        star_pos = random_teleport(WIDTH,HEIGHT, player_size)
        text_surf = font.render(str(points), True, palette['text'])
    
    ### Draw ###
    pygame.draw.rect(screen, palette['star'], star_rec) # star
    pygame.draw.rect(screen, palette['player'], player_rec ) # player
    screen.blit(text_surf, (10, 10))
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000
    
pygame.quit()

