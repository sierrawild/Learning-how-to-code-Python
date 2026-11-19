import pygame
from Player import Player
from Entity import Enemy
# from settings import WIDTH, HEIGHT, palette
import settings

score = 0

pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption('Line')
clock = pygame.time.Clock()
dt = 0
pygame.mouse.set_visible(False)


# player 
player = Player((settings.WIDTH/2, settings.HEIGHT/2))
player_group = pygame.sprite.Group()
player_group.add(player)

# enemies
e = Enemy((settings.WIDTH/2, settings.HEIGHT/2))
enemy_group = pygame.sprite.Group()
enemy_group.add(e)

# all sprite group for drawing 
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(e)
all_sprites_group.add(player)


running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    ### Update ###
    player_group.update()
    enemy_group.update(player.pos, dt)
    
    # font
    score_txt = settings.font_score.render(str(score), True, (settings.palette['bg_comp']))

    ### Draw ###
    screen.fill(settings.palette['bg'])
    
    all_sprites_group.draw(screen)
    # font
    screen.blit(score_txt, (50,50))
    
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
pygame.quit()