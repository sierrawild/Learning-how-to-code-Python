import pygame

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Animation")

white = (250, 250, 250)
cat = pygame.image.load(r"PyGame\files\cat.png")
catx = 10
caty = 10
direction = "right"

running = True
while running:
    for event in pygame.event.get():
        if event. type == pygame.QUIT:
            running = False
            
    screen.fill(white)
    
    if direction == "right":
        catx += 5
        if catx >= 280:
            direction = "down"
    elif direction == "down":
        caty += 5
        if caty >= 220:
            direction = "left"
    elif direction == "left":
        catx -= 5
        if catx <= 10:
            direction = "up"
    elif direction == "up":
        caty -= 5
        if caty <= 10:
            direction = "right"

    screen.blit(cat, (catx, caty))

    pygame.display.update()
    fpsClock.tick(FPS)
        

pygame.quit()