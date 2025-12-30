import pygame

pygame.init()

resolution = (800, 800)
screen =  pygame.display.set_mode(resolution)

ball_img = pygame.image.load(r"PyGame\files\ball_image.png")#.convert()
ball_img = pygame.transform.scale(ball_img, (ball_img.get_width() * 2,
                                   ball_img.get_height() * 2))


clock = pygame.time.Clock()
delta_time = 0.1

x = 100
y = 400
moveSpeed = 500

player_pos = pygame.Vector2(x, y)
running = True
while running:
    screen.fill("#FFED94")
    
    hit_box = pygame.Rect(player_pos[0], player_pos[1], ball_img.get_width(), ball_img.get_height())
    mouse_pos = pygame.mouse.get_pos()
    
    target = pygame.Rect(300, 400, 150, 300)
    collision = hit_box.colliderect(target)
    m_collision = target.collidepoint(mouse_pos)
    pygame.draw.rect(screen, (250 * collision ,250 * m_collision , 0), target)
    screen.blit(ball_img, player_pos)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= moveSpeed * delta_time
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += moveSpeed * delta_time
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= moveSpeed * delta_time
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += moveSpeed * delta_time
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))
    
    
         
pygame.quit()