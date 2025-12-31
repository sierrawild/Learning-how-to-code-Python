import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 1080))
clock = pygame.time.Clock()

speed = [2,2]

pos1 = pygame.Vector2(100,100)
radius = 50

ball_1rec = pygame.Rect(0,0, radius * 2, radius * 2)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT \
        or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
            
    
            
    screen.fill("#7AA0AD")
    
    ball_1rec.center = pos1
    ball_1 = pygame.draw.circle(screen, "red", ball_1rec.center, radius)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
    
