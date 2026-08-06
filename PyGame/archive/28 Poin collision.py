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
            
    
  
    
    screen.fill("#6DF8D3")
    
    # rectangles 
    color = "#93FF4A"
    
    
    pos = pygame.mouse.get_pos()
    # draw rect
    for i in obstacles:
        if i.collidepoint(pos):
            pygame.draw.rect(screen, "#FF7D78", i)
        else:
            pygame.draw.rect(screen, "#7890FF", i)
    
    

    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()