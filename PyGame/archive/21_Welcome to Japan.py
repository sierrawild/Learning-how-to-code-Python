import pygame

pygame.init()

WIDTH = 900
HEIGHT = 700
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# font
fontObj = pygame.font.Font(None, 70)
textSurfObj = fontObj.render("We are going to Japan!!!", True, "red")
textRect = textSurfObj.get_rect()
textRect.center = (WIDTH/2, 600)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("#BFFBFF")
    
    # Flag
    pygame.draw.rect(screen, "black", (145,45, 610, 410), 10)
    pygame.draw.rect(screen, "white", (150,50, 600, 400))
    pygame.draw.aacircle(screen, "red", (450, 250), 120)
    
    screen.blit(textSurfObj, textRect)
    
    pygame.display.flip()
    clock.tick(FPS)
    
pygame.quit()