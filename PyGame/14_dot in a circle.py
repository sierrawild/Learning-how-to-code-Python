import pygame, math

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

t = 0
r = 200
screen.fill("#A8FFD8")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    t += 1
    speed = t * 0.05
    
    # red dot doing circle clockwise
    x = WIDTH/2 + r*math.cos(speed)
    y = HEIGHT/2 + r*math.sin(speed)
    pygame.draw.circle(screen, "#FF8787", (x, y), 20)
    pygame.draw.circle(screen, "#FC6262", (x, y), 10)
    
    # yellow dot doing circle counter clockwise
    x = WIDTH/2 + r*1.5*math.cos(-speed)
    y = HEIGHT/2 + r*0.7*math.sin(-speed)
    pygame.draw.circle(screen, "#FCFF63", (x, y), 20)
    pygame.draw.circle(screen, "#DCDF42", (x, y), 10)
    
    # blue dot sign 
    x = WIDTH/2
    y = HEIGHT/2 + r*1.2*math.sin(speed)
    pygame.draw.circle(screen, "#7BE7FF", (x, y), 20)
    pygame.draw.circle(screen, "#52DBF9", (x, y), 10)
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()