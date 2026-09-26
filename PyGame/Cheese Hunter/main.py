import pygame, random
from helpers import *

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Cheese Hunter')
dt = 0
frame_count = 0
game_over = False
# player
player_pos = pygame.Vector2(WIDTH/2,HEIGHT/2)
player_speed = 350
player_size = 25

# cheese
cheese_pos = random_teleport(WIDTH,HEIGHT, player_size)
score = 0

# walls
walls = walls(WIDTH, HEIGHT)
    
# font
score_font = pygame.font.Font(None, 40)
score_surf = score_font.render(str(score), True, palette['text'])

game_over_font = pygame.font.Font(None, 76)
game_over_font_surf = game_over_font.render('GAME OVER', True, palette['game_over'])
game_over_rect = game_over_font_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
game_over_font_surf2 = score_font.render('press SPACE to play again', True, palette['game_over'])
game_over_rect2 = game_over_font_surf2.get_rect(center=(WIDTH//2, HEIGHT * 0.6))

# enemies
enemy_size = 20
enemy_speed = 100
#ghost
ghost_visible = False
ghost = pygame.Rect(0,0, enemy_size * 2, enemy_size * 2)


class Enemy(pygame.Rect):
    def __init__(self, x, y, width, height, speed, color):
        super().__init__(x, y, width, height)
        self.speed = speed
        self.directions = ['N', 'E', 'W', 'S']
        self.direction = random.choice(self.directions)
        self.color = color
        self.velocity = pygame.Vector2(0,0)
        self.move_by = pygame.Vector2(0,0)
    
    def move(self, dt):
        if self.direction == 'N':
            self.velocity.y -= 1
        elif self.direction == 'S':
            self.velocity.y += 1
        elif self.direction == 'W':
            self.velocity.x -= 1
        elif self.direction == 'E':
            self.velocity.x += 1
        
        if self.velocity.length() > 0:
            self.velocity.normalize()
        self.move_by = self.velocity * self.speed * dt
        self.x += self.move_by.x
        self.y += self.move_by.y
        
    def change_direction(self):
        right_to = {'N':'E', 'E':'S', 'S':'W','W':'N'}
        left_to = {'N':'W','W':'S','S':'E','E':'N'}
        chose = random.choice([right_to,left_to])
        
    
    def draw(self, surf):
        pygame.draw.rect(surf,self.color, (self.x, self.y, self.height, self.height))
    
enemies = []
for i in range(3):
    random_pos = random_teleport(WIDTH,HEIGHT, enemy_size*2)
    enemies.append(Enemy(random_pos[0], random_pos[1], enemy_size, enemy_size, enemy_speed * random.uniform(0.2, 0.5), palette['enemy']))

    
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
    frame_count +=1
    # player update
    if not game_over:
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
    
    # enemies 
    # ghost
    if ghost_visible:
        hunt = player_pos - pygame.Vector2(ghost.center)
        if hunt.length() > 0:
            hunt = hunt.normalize()
        step = enemy_speed * dt
        ghost.x += hunt.x * step
        ghost.y += hunt.y * step
    if frame_count % 300 == 0:
        ghost_visible = not ghost_visible
        new_ghost_pos = random_teleport(WIDTH, HEIGHT, enemy_size)
        ghost.x, ghost.y = new_ghost_pos
    if ghost_visible == False:
        ghost.x, ghost.y = -100, -100
    
    for enemy in enemies:
        enemy.move(dt)
    
    # enemies collisions with player
    if ghost.colliderect(player_rect):
        game_over = True
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            game_over = True

    ### DRAW ###
    # player
    pygame.draw.rect(screen, palette['player'], player_rect)

    # cheese
    pygame.draw.rect(screen, palette['cheese'], cheese)
    
    # ghost
    if ghost_visible:
        pygame.draw.rect(screen, palette['ghost'], ghost)
    
    # walls
    for wall in walls:
        pygame.draw.rect(screen,palette['wall'], wall)

    # enemies
    for enemy in enemies:
        enemy.draw(screen)
    
    # game over screen
    if game_over:
        movement = pygame.Vector2(0,0) # stops player from gliding after death
        screen.blit(game_over_font_surf, game_over_rect)
        screen.blit(game_over_font_surf2, game_over_rect2)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_over = False
            score = 0
            score_surf = score_font.render(str(score), True, palette['text'])
            # reset enemies
            new_ghost_pos = random_teleport(WIDTH, HEIGHT, enemy_size)
            ghost.x, ghost.y = new_ghost_pos
    # flip() the display to put your work on screen
    screen.blit(score_surf, (50,50))
    pygame.display.flip()


    dt = clock.tick(60) / 1000


pygame.quit()