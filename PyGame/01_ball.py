import pygame

pygame.init()
screen = pygame.display.set_mode((1800, 1000))
clock = pygame.time.Clock()
running = True
dt = 0
moveSpeed = 500



player_pos = pygame.Vector2(screen.get_width() / 2,
                            screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#aef1aa")

    pygame.draw.circle(screen, "red", player_pos, 35)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= moveSpeed * dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += moveSpeed * dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= moveSpeed * dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += moveSpeed * dt
    
    pygame.display.flip()

    dt = clock.tick(60) / 1000
    
pygame.quit()
    