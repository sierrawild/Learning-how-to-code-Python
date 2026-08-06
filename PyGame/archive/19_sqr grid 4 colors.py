import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

running = True
while running:
    # quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    
    
    screen.fill("#FFDBDB")
    spacing = 22
    for i in range(0,WIDTH , spacing):
        for j in range(0,HEIGHT, spacing):
            color = "#6ED5CC"
            if i > WIDTH / 2 and j > HEIGHT / 2:
                color = "#7281C2"
            elif i > WIDTH / 2:
                color = "#72C29E"
            elif j > HEIGHT / 2:
                color = "#C2BF72"
                
            pygame.draw.rect(screen, color, (i, j, 20, 20))
    
    
    pygame.display.flip()
    
        
    clock.tick(60)

pygame.quit()