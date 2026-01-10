# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

screen.fill("#AEF1AA")

x = -20 
y = 0
x1 = 200

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE
    x += 1
    y = int(+0.001*x**2 - 1*x + 400)
    
    pygame.draw.circle(screen, "#FF4917", (x,y), 50)
    pygame.draw.circle(screen, "#F8663E", (x,y), 40)
    pygame.draw.circle(screen, "#F8753E", (x,y), 30)
    
    
    x1 += 1
    y1 = int(-0.001*x**2 + x + 100)
    pygame.draw.circle(screen, "#3EF2F8", (x1,y1), 30)
    pygame.draw.circle(screen, "#688CD5", (x1,y1), 20)
    pygame.draw.circle(screen, "#735CE8", (x1,y1), 10)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60*3)  # limits FPS to 60

pygame.quit()