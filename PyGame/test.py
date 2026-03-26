# Example file showing a basic pygame "game loop"
import pygame, random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# check available fonts
# print(pygame.font.get_fonts())

print(random.random())


running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#AEF1AA")

    
    # RENDER YOUR GAME HERE
    color = pygame.Color("red")
    for i in range(10):
        pygame.draw.circle(screen, color, (640, 360), i*20, 10)
        color.r -=20
    
    
    # FONT
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()