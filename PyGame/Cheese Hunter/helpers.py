import pygame, random

palette = {'name': 'default',
            'bg': "#75E7F2",
            'player': "#F2A875",
            'enemy': "#F275A0",
            'cheese': "#FFF835",
            'text': "#0D2B33",
            'wall': "#0D2B33",
           }


def key_input(dt, player_pos, player_speed):
    keys = pygame.key.get_pressed()
    move = pygame.Vector2(0,0)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        move.y -= 1
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        move.y += 1
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        move.x -=1
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        move.x += 1

    # normalizing diagonal movement 
    if move.length() > 0:
        move = move.normalize()
        return (move * player_speed * dt)

def player_collisions(player_pos, player_size, walls, movement):
    # x axis, horizontal movement 
    if movement != None:
        player_pos.x += movement.x
    player_rect = pygame.Rect(player_pos.x, player_pos.y, player_size, player_size)
    hit = player_rect.collidelist(walls)
    if hit != -1 and movement != None:
        if movement.x > 0:
            player_rect.right = walls[hit].left
        elif movement.x < 0:
            player_rect.left = walls[hit].right
    player_pos.x = player_rect.x

    # y axis, vertical movement
    if movement != None:
        player_pos.y += movement.y
    player_rect = pygame.Rect(player_pos.x, player_pos.y, player_size, player_size)
    hit = player_rect.collidelist(walls)
    if hit != -1 and movement != None:
        if movement.y > 0:
            player_rect.bottom = walls[hit].top
        elif movement.y < 0:
            player_rect.top = walls[hit].bottom
    player_pos.y = player_rect.y
    return player_rect    
        
def edge_wrap(WIDTH, HEIGHT, player_pos):
    player_pos.x %= WIDTH
    player_pos.y %= HEIGHT
    
def lerp(a,b,t):
    return a + (b-a) * t

def walls(WIDTH, HEIGHT):
    wall_thickness = 30
    vertical_wall_coordinates = [(0,0,HEIGHT), (WIDTH-wall_thickness,0,HEIGHT), 
                             (200,200, 600), (600,0, 400), (820, 400, 200), (980, 180, 450)]
    horizontal_wall_coordinates = [(0,0,WIDTH), (0,HEIGHT-wall_thickness, WIDTH), 
                               (200, 200, 150), (300, 300, 150), (400, 500, 300), (600, 120, 150), (980, 220, 100), 
                               (1100, 320, 100), (1100, 520, 200)]
    walls = []
    for wall in vertical_wall_coordinates:
        walls.append(pygame.Rect(wall[0], wall[1], wall_thickness, wall[2]))
    for wall in horizontal_wall_coordinates:
        walls.append(pygame.Rect(wall[0], wall[1], wall[2], wall_thickness))
    return walls


def random_teleport(WIDTH,HEIGHT, size):
    return pygame.Vector2(random.randint(0 + size,WIDTH - size), random.randint(0 + size,HEIGHT - size))
