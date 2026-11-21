import pygame

# constants
WIDTH, HEIGHT = 0, 0
SHAKE_TIME = 1
SHAKE_MAX = 25

xoff, yoff = 0,0
shake_timer = 0

x = 35

pygame.init()
window = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
W, H = pygame.display.get_window_size()
screen = pygame.Surface((W, H))
pygame.display.set_caption('Mouse chase')
clock = pygame.time.Clock()
dt = 0
pygame.mouse.set_visible(False)

# palette
bg = '#B2FFFE'
bg2 = '#B2FFCF'
bg_comp = '#FFB2B3'

running = True
while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
    ### Update ###
                
    
    ### Draw ###
    #background
    screen.fill(bg)
    for col in range(W//x + 1):
        for row in range(H//x + 1):
            if col % 2 == 0 and row % 2 == 0 \
                or col % 2 != 0 and row % 2 != 0:
                    pygame.draw.circle(screen,bg2,(col*x, row*x), x*0.6)
    
    window.blit(screen, (xoff, yoff))
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
                