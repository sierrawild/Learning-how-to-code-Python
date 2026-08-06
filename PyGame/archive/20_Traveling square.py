import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


# variables
x = 0
y = 0

sqr_size = 50
travel_distance = 30

running = True
def square(WIDTH, HEIGHT, screen, x, y, sqr_size, travel_distance):
    
    
    pygame.draw.rect(screen, "#23F0FF", (x, y, sqr_size, sqr_size))
    
    x += travel_distance
    if x >= WIDTH:
        y += travel_distance
        x = 0
    if y >= HEIGHT:
        y = 0
        y = 0
    
    return x,y

while running:
    # quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    screen.fill("#FFDBDB")
    
    x,y = square(WIDTH, HEIGHT, screen, x, y, sqr_size, travel_distance)
    
    
    pygame.display.flip()
    
        
    clock.tick(60)

pygame.quit()