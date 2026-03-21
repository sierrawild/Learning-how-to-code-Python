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
    
    
    
    
    for i in range(int(8)):
        for j in range(int(8)):
            h = i / 8
            l = (i+j)/16
            s = j / 8
            
            h = i / 8
            l = (i+j)/16
            s = j / 8
            rgb = colorsys.hls_to_rgb(h,l,s)
            color = tuple(int(c * 255) for c in rgb)
            pygame.draw.rect(screen, color, (i*100 + 100, j*100 + 100, cube_size, cube_size), border_radius= 15)





    pygame.display.flip()
    clock.tick(60)
pygame.quit()