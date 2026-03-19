import pygame, math, random
# https://www.youtube.com/watch?v=BHr9jxKithk&t=305s

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

MOVEMENT_SPEED = 10
SIZE = 50

# settings

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()




# objects in game
rect_1 = pygame.Rect(100,100, SIZE, SIZE)
obstacles = []
for _ in range(20):
    obstacle_rect = pygame.Rect(random.randint(0 + SIZE, SCREEN_WIDTH - SIZE), random.randint(0 + SIZE, SCREEN_HEIGHT - SIZE), SIZE, SIZE)
    obstacles.append(obstacle_rect)

player_x = 500
player_y = 500

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    
    # key input
    dx, dy = 0, 0
    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_LEFT]: dx -=1
    if key[pygame.K_d] or key[pygame.K_RIGHT]: dx +=1
    
    if key[pygame.K_w] or key[pygame.K_UP]: dy -=1
    if key[pygame.K_s] or key[pygame.K_DOWN]: dy +=1
    
    # normalize diagonal
    if dx != 0 and dy != 0:
        l = math.sqrt(dx**2 + dy**2)
        dx /= l
        dy /= l
        
    # player.x += dx * MOVEMENT_SPEED
    # player.y += dy * MOVEMENT_SPEED
    player_x += dx * MOVEMENT_SPEED
    player_y += dy * MOVEMENT_SPEED
    
    
    screen.fill("#6DF8D3")
    
    # rectangles 
    color = "#93FF4A"
    # for obstacle in obstacles:
    #     if rect_1.colliderect(obstacle):
    #         color = "#FF60D7"
    
    if rect_1.collidelist(obstacles) >= 0:
            color = "#FF60D7"
            print(rect_1.collidelist(obstacles))
    
    pos = pygame.mouse.get_pos()
    rect_1.center = pos
    # draw rect
    for i in obstacles:
        pygame.draw.rect(screen, "#7890FF", i)
    pygame.draw.rect(screen, color, rect_1)
    
    
    # player made of circles
    
    # Player circle collision — check distance from player centre to each obstacle
    player_color = "#E24A4A"
    for obstacle in obstacles:
        closest_x = max(obstacle.left, min(player_x, obstacle.right))
        closest_y = max(obstacle.top, min(player_y, obstacle.bottom))
        dist = math.sqrt((player_x - closest_x)**2 + (player_y - closest_y)**2)
        if dist < SIZE: # size is the circle radius
            player_color = "#F2B21B"
            break
    
    pygame.draw.circle(screen, player_color, (int(player_x), int(player_y)), SIZE, int(SIZE/2), True, False, True, False)
    pygame.draw.circle(screen, player_color, (int(player_x), int(player_y)), SIZE*.8, int(SIZE/3), False, True, False, True)

    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()