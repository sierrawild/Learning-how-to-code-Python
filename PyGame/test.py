import pygame

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Name of the game')
clock = pygame.time.Clock()
dt = 0

class Enemy(pygame.Rect):
    def __init__(self, x, y, w, h, speed):
        super().__init__(x, y, w, h)
        self.speed = speed
    
    def move(self):
        self.x += self.speed
        self.y += self.speed
    
    def draw(self, surf, color):
        pygame.draw.rect(surf, color, (self.x, self.y, self.w, self.h))

size = 50
speed = 10
enemies = [Enemy(100,100,size,size,speed), Enemy(100,200,size,size,speed)]

running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Close the window by pressing ESCAPE
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#AEF1AA")

    ### UPDATE ###
    
    for enemy in enemies:
        enemy.move()
    
    ### DRAW ###
    for enemy in enemies:
        enemy.draw(screen, 'red')

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60) / 1000
    
pygame.quit()