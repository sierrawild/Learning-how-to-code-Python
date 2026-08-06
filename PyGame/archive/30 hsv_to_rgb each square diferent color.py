import pygame, colorsys

pygame.init()

SCREEN_W, SCREEN_H = 1000, 1000
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.RESIZABLE)
clock = pygame.time.Clock()

# cube settings
cube_size = 80
cols, rows = 8, 8

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
    
    
    
    
    for j in range(int(rows)):
        for i in range(int(cols)):
            index = i + j * cols
            h = index / (cols * rows)
            s = 0.6
            v = 0.8
            rgb = colorsys.hsv_to_rgb(h,s,v)
            color = tuple(int(c * 255) for c in rgb)
            pygame.draw.rect(screen, color, (i*100 + 100, j*100 + 100, cube_size, cube_size), border_radius= 15)





    pygame.display.flip()
    clock.tick(60)
pygame.quit()