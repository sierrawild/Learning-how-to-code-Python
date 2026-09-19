import pygame

palette = {'name': 'default',
            'bg': "#75E7F2",
            'player': "#F2A875",
            'enemy': "#F275A0",
            'star': "#FFF835",
            'text': "#0D2B33"
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
        player_pos += (move * player_speed * dt)
        
def edge_wrap(WIDTH, HEIGHT, player_pos):
    player_pos.x %= WIDTH
    player_pos.y %= HEIGHT
    
def lerp(a,b,t):
    return a + (b-a) * t