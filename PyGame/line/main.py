import pygame
from Player import Player
from settings import WIDTH, HEIGHT, palette


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Line')
clock = pygame.time.Clock()
dt = 0
pygame.mouse.set_visible(False)



player = Player((WIDTH/2, HEIGHT/2))
player_group = pygame.sprite.Group()
player_group.add(player)

running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    # Update
    player_group.update()
    # Draw
    screen.fill(palette['bg'])
    
    player_group.draw(screen)
    
    
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    
pygame.quit()