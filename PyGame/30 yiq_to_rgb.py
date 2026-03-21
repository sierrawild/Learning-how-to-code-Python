import pygame, colorsys

pygame.init()

SCREEN_W, SCREEN_H = 1000, 1000
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.RESIZABLE)
clock = pygame.time.Clock()

# cube settings
cube_size = 80

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            
        # key input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    screen.fill("#62F5FF") 
    
    
    
    
    for x in range(int(8)):
        for xx in range(int(8)):
            y = x / 8
            i = (x+xx)/16
            q = xx / 8
            
            # y = 0
            # i = 0.5
            # q = 0.5
            
            rgb = colorsys.yiq_to_rgb(y,i,q)
            color = tuple(int(c * 255) for c in rgb)
            pygame.draw.rect(screen, color, (x*100 + 100, xx*100 + 100, cube_size, cube_size), border_radius= 15)





    pygame.display.flip()
    clock.tick(60)
pygame.quit()