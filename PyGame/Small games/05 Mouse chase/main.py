import pygame, random
from path import character_sprites



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

# player
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, sprite):
        super().__init__()
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        
    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.rect.center = self.pos

        
player_sprite = random.choice(character_sprites)
player = Player((W//2,H//2), player_sprite)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

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
    player.update()          
    
    ### Draw ###
    #background
    screen.fill(bg)
    for col in range(W//x + 1):
        for row in range(H//x + 1):
            if col % 2 == 0 and row % 2 == 0 \
                or col % 2 != 0 and row % 2 != 0:
                    pygame.draw.circle(screen,bg2,(col*x, row*x), x*0.6)
    
    all_sprites.draw(screen)
    
    window.blit(screen, (xoff, yoff))
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
                