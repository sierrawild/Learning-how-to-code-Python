import pygame, random, math
from pathlib import Path

WIDTH, HEIGHT = 1280, 720
palette = {'bg': "#75E7F2",
           'player': "#F2A875",
           'enemy': "#F275A0",
           'star': "#FFF835",
           'text': "#0D2B33"
           }

running = True
game_over = False

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Star Hunter')
clock = pygame.time.Clock()
dt = 0

global_speed = 0.5
speed_up = {5:0.6, 15:0.8, 30:1,}
points = 0

# player data
player_pos = pygame.Vector2(WIDTH/2,HEIGHT/2)
player_speed = 320
player_size = 70

# enemies
active_enemies = []
enemies_size = 50
enemies_speed = 100

enemy_oscillate = pygame.Rect(0, HEIGHT*0.9, enemies_size *1.5,enemies_size)
enemy_chaser = pygame.Rect(WIDTH//2, HEIGHT +200, enemies_size, enemies_size * 1.3)
enemy_glider = pygame.Rect(WIDTH//2, -100, enemies_size, enemies_size)
target = pygame.Vector2(500, 500)
frames_passed = 0

# font
font = pygame.font.Font(None, 36)
game_over_font = pygame.font.Font(None, 76)
points_text_surf = font.render(str(points), True, palette['text'])
game_over_font_surf = game_over_font.render('GAME OVER', True, palette['text'])
game_over_rect = game_over_font_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
game_over_font_surf2 = font.render('press SPACE to play again', True, palette['text'])
game_over_rect2 = game_over_font_surf2.get_rect(center=(WIDTH//2, HEIGHT * 0.6))

# sound
BASE = Path(__file__).parent
sfx_pickup = pygame.mixer.Sound(BASE / 'pickup.mp3')
sfx_end = pygame.mixer.Sound(BASE / 'end.mp3')
sfx_end_played = False
sfx_start = pygame.mixer.Sound(BASE / 'start.mp3')
sfx_start.play()

# music
pygame.mixer.music.load(BASE/ 'music.mp3')
pygame.mixer.music.play(-1)

def lerp(a,b,t):
    return a + (b-a) * t

def oscillate(start, finish, time, speed = 1):
    t = 0.5 + 0.5 * math.sin(time * speed)
    return lerp(start, finish, t) 
    

def random_teleport(WIDTH,HEIGHT, size):
    return pygame.Vector2(random.randint(0 + size,WIDTH - size), random.randint(0 + size,HEIGHT - size))
# enemies and pickups
star_pos = random_teleport(WIDTH,HEIGHT, player_size)


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

    if move.length() > 0:
        move = move.normalize()
        player_pos += move * player_speed * dt * global_speed

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
    if not game_over:
        key_input(dt, player_pos, player_speed)
    edge_wrap(WIDTH, HEIGHT, player_pos)
    player_rec = pygame.Rect(player_pos.x, player_pos.y, player_size, player_size)
    

    # star related update
    star_rec = pygame.Rect(star_pos.x, star_pos.y, int(player_size * 0.7), int(player_size * 0.7))
    
    # speed up logic
    for i in speed_up:
        if points == i:
            global_speed = speed_up[i]
    
    # enemies update
    if points == 2 and len(active_enemies) == 0:
        active_enemies.append(enemy_oscillate)
    if points == 4 and len(active_enemies) == 1:
        active_enemies.append(enemy_chaser)
    if points == 10 and len(active_enemies) == 2:
        active_enemies.append(enemy_glider)
    
    if enemy_oscillate in active_enemies:
        enemy_oscillate.x = oscillate(0,WIDTH - enemies_size, pygame.time.get_ticks() / 1000, global_speed)
        
    if enemy_chaser in active_enemies:
        direction = player_pos - pygame.Vector2(enemy_chaser.center)
        if direction.length() > 0:
            direction = direction.normalize()
            step = enemies_speed * dt * global_speed
            enemy_chaser.x += direction.x * step
            enemy_chaser.y += direction.y * step
            
    if enemy_glider in active_enemies:
        overshoot = 1.4
        frames_passed += 1
        
        if frames_passed % 150 == 0:
            target.y = lerp(enemy_glider.y, player_pos.y, overshoot)
            target.x = lerp(enemy_glider.x, player_pos.x, overshoot)
        
        enemy_glider.x = lerp(enemy_glider.x, target.x, 0.2 * 0.2)
        enemy_glider.y = lerp(enemy_glider.y, target.y, 0.2 * 0.2)
            
    
    # collision
    if player_rec.colliderect(star_rec):
        points += 1
        star_pos = random_teleport(WIDTH,HEIGHT, player_size)
        points_text_surf = font.render(str(points), True, palette['text'])
        sfx_pickup.play()
    for enemy in active_enemies:
        if player_rec.colliderect(enemy):
            game_over = True
            break
            
    
    ### Draw ###
    pygame.draw.rect(screen, palette['star'], star_rec) # star
    pygame.draw.rect(screen, palette['player'], player_rec ) # player
    screen.blit(points_text_surf, (10, 10))
    
    # enemies
    for enemy in active_enemies:
        pygame.draw.rect(screen, palette['enemy'], enemy)

    
    # game over screen
    if game_over:
        screen.blit(game_over_font_surf, game_over_rect)
        screen.blit(game_over_font_surf2, game_over_rect2)
        # sounds
        if sfx_end_played == False:
            sfx_end.play()
            sfx_end_played = True
            pygame.mixer.music.pause()
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_over = False
            sfx_start.play()
            sfx_end_played = False
            pygame.mixer.music.unpause()
            active_enemies = []
            points = 0
            global_speed = 1
            points_text_surf = font.render(str(points), True, palette['text'])
            screen.blit(points_text_surf, (10, 10))
            
            # reset enemies
            enemy_oscillate = pygame.Rect(0, HEIGHT*0.9, enemies_size *1.5,enemies_size)
            enemy_chaser = pygame.Rect(WIDTH//2, HEIGHT +200, enemies_size, enemies_size * 1.3)
            enemy_glider = pygame.Rect(WIDTH//2, -100, enemies_size, enemies_size)
            
            
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
pygame.quit()

