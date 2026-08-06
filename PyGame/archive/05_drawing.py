import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)
pygame. display.set_caption("Drawing")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

screen.fill(WHITE)
pygame.draw.polygon(screen, GREEN, ((115, 0),(295, 160), (235, 277), (0, 106)))
pygame.draw.line(screen, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(screen, BLUE, (120, 60), (60, 120))
pygame.draw.line(screen, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(screen, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(screen, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(screen, RED, (200, 150, 100, 50))
pygame.draw.rect(screen, BLUE, (350, 300, 100, 100), 5, 25)

pixObj = pygame.PixelArray(screen)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()
    
pygame.quit()