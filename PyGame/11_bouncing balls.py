import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 1080))
clock = pygame.time.Clock()

speed = 10
radius = 30


pos1 = pygame.Vector2(100,100)
ball_1rec = pygame.Rect(0,0, radius * 2, radius * 2)
speed_vector2_1 = [speed,speed]

pos2 = pygame.Vector2(200,200)
ball_2rec = pygame.Rect(0,0, radius * 2, radius * 2)
speed_vector2_2 = [speed,speed]

def ScreenEdgeCollisionDetection(screen, speed_vector2, ball_rec):
    if ball_rec.left < 0 or ball_rec.right > screen.get_width():
        speed_vector2[0] = -speed_vector2[0]
    if ball_rec.top < 0 or ball_rec.bottom > screen.get_height():
        speed_vector2[1] = -speed_vector2[1]


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT \
        or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
            
    
            
    screen.fill("#C9F1FF")
    
    # ball 1
    pos1 += speed_vector2_1 # works because pos1 is a Vector2
    ball_1rec.center = pos1
    ScreenEdgeCollisionDetection(screen, speed_vector2_1, ball_1rec)
    
    ball_1 = pygame.draw.circle(screen, "red", ball_1rec.center, radius) # draw the ball
    # pygame.draw.rect(screen, "blue", ball_1rec, 2) # draw rec for debugging 
    
    # ball 2
    pos2 += speed_vector2_2 # works because pos2 is a Vector2
    ball_2rec.center = pos2
    ScreenEdgeCollisionDetection(screen, speed_vector2_2, ball_2rec)
    
    ball_2 = pygame.draw.circle(screen, "green", ball_2rec.center, radius) # draw the ball
    
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
    
