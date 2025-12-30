import pygame
import clouds

# pygame setup
pygame.init()


screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption("Max's Plane")
clock = pygame.time.Clock()
delta_time = 0
moveSpeed = 500

# player setup

plane = pygame.image.load("Maxis_Plane/files/Max plain.png").convert() # load image
plane.set_colorkey((255, 255, 255)) # ignore white color of the background
scale_by = 2.2
plane = pygame.transform.scale(plane, (plane.get_width() / scale_by,
                                       plane.get_height() / scale_by)) # scale down
plane = pygame.transform.flip(plane, True, False)
plane_original = plane

plane_rec = plane.get_rect(center=screen.get_rect().center)
player_pos = pygame.Vector2(plane_rec.center)

tilt_angle = 0
target_tilt = 0
tilt_speed = 4

# cloud
cloud = clouds.Cloud(2000, 500, 50)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("#94EAFF")
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player_pos.y -= moveSpeed * delta_time
        target_tilt = 15
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player_pos.y += moveSpeed * delta_time
        target_tilt = -15
    else:
        target_tilt = 0
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_pos.x += moveSpeed * delta_time
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_pos.x -= moveSpeed * delta_time 
    
    # Tilting and drawing the plane
    tilt_angle += (target_tilt - tilt_angle) * tilt_speed * delta_time
    rotated_plane = pygame.transform.rotate(plane_original, tilt_angle) # rotation up and down
    
    # Clamping to the screen
    plane_width = rotated_plane.get_width()
    plane_heigh = rotated_plane.get_height()
    
    player_pos.x = max(plane_width/2, min(screen.get_width() - plane_width/2, player_pos.x))
    player_pos.y = max(plane_heigh/3, min(screen.get_height() - plane_heigh/3, player_pos.y))
    
    # build plane rectangle 
    plane_rec = rotated_plane.get_rect(center=player_pos)
    
    
    # clouds
    cloud.draw(screen)

    screen.blit(rotated_plane, plane_rec)
    
    # tilt_angle = 0 # centers plane and by taking it out of key if statements, plane can be tilted while using other keys
    
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000
    delta_time = min(delta_time, 0.05)
    
    
    
pygame.quit()