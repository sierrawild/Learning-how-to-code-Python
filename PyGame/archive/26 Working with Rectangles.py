import pygame, math

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 10

# setting
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working with Rectangles")

clock = pygame.time.Clock()

# variables 
rect_1 = pygame.Rect(400, 200, 100, 200)
cat = pygame.image.load(r"PyGame\files\cat.png").convert_alpha()
cat_facing_left = cat
cat_facing_right = pygame.transform.flip(cat, True, False)
rect_2 = cat.get_rect()
cat_direction = "left"



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # key input
    dx, dy = 0,0
    key = pygame.key.get_pressed()
    if key[pygame.K_a]: 
        dx -=1 
        cat_direction = "left"
    if key[pygame.K_d]: 
        dx +=1
        cat_direction = "right"
    if key[pygame.K_s]: dy +=1
    if key[pygame.K_w]: dy -=1
    
    # normalize if moving diagonally
    if dx != 0 and dy !=0:
        length = math.sqrt(dx**2 + dy**2) # = √2 ≈ 1.414
        dx /= length
        dy /= length
        
    # apply speed
    
    rect_2.x += dx * MOVEMENT_SPEED
    rect_2.y += dy * MOVEMENT_SPEED
    
    
    screen.fill("#FFEF9E")
    
    
    
    # drawing
    
    pygame.draw.rect(screen, "#35EA99", rect_1)
    # pygame.draw.rect(screen, "#543543", rect_2)
    # player direction
    # if cat_direction == "right":
    #     cat = cat_facing_right
    # if cat_direction == "left":
    #     cat = cat_facing_left
    current_sprite = cat_facing_right if cat_direction == "right" else cat_facing_left
    screen.blit(current_sprite, rect_2)
    
    
    ##############
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()