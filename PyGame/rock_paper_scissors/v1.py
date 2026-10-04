import pygame, random

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
HANDS = ['rock', 'paper', 'scissors']

palette = {'name': 'default',
           'rock': "#63F5FF",
           'paper': "#FFF9D2",
           'scissors': "#FF6A50",
           'bg': "#D7FFD6",
           }
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Name of the game')
clock = pygame.time.Clock()
dt = 0

# functions
def draw_shape(x,y, size, shape, palette, surface):
    shape_rect = pygame.Rect(x,y,size,size)
    shape_rect.center = (x,y)
    if shape == 'rock':
        pygame.draw.aacircle(surface, palette['rock'], (x,y), size/2)
    elif shape == 'paper':
        pygame.draw.rect(surface, palette['paper'], shape_rect)
    elif shape == 'scissors':
        points = [(x - size/2, y + size/2), (x, y - size/2), (x + size/2, y+size/2)]
        pygame.draw.polygon(surface, palette['scissors'], points)

# classes
class Player:
    def __init__(self):
        self.hand = None
        
    def choose_random_hand(self, hands):
        self.hand = random.choice(hands)

game_ai = Player()





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
    screen.fill(palette['bg']) # fill the screen with a color to wipe away anything from last frame

    

    ### UPDATE ###
    
    
    ### DRAW ###
    pygame.draw.circle(screen, "red", (100, 100), 50)

    game_ai.hand = 'rock'
    draw_shape(500,500, 300, game_ai.hand, palette, screen)
    game_ai.hand = 'paper'
    draw_shape(500,500, 250, game_ai.hand, palette, screen)
    game_ai.hand = 'scissors'
    draw_shape(500,500, 250, game_ai.hand, palette, screen)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60
    
pygame.quit()