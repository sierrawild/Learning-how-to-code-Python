# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

screen.fill("#AEF1AA")

x = 500 
y = -10 * x**2
x1, y1 = 400, 200

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "#FF4917", (x,y), 50)
    pygame.draw.circle(screen, "#F8663E", (x,y), 40)
    pygame.draw.circle(screen, "#F8753E", (x,y), 30)
    x -= 1
    
    
    pygame.draw.circle(screen, "#3EF2F8", (x1,y1), 30)
    pygame.draw.circle(screen, "#688CD5", (x1,y1), 20)
    pygame.draw.circle(screen, "#735CE8", (x1,y1), 10)
    x1 += 1

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60*400)  # limits FPS to 60

pygame.quit()