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


# classes
class Player:
    def __init__(self, size, palette):
        self.hand = None
        self.size = size
        self.palette = palette
        self.shape_rect = None
        
    def choose_random_hand(self, hands):
        self.hand = random.choice(hands)
        
    def draw_shape(self,x,y, surface):
        self.shape_rect = pygame.Rect(x,y,self.size,self.size)
        self.shape_rect.center = (x,y)
        if self.hand == 'rock':
            pygame.draw.aacircle(surface, palette['rock'], (x,y), self.size/2)
        elif self.hand == 'paper':
            pygame.draw.rect(surface, palette['paper'], self.shape_rect)
        elif self.hand == 'scissors':
            points = [(x - self.size/2, y + self.size/2), (x, y - self.size/2), (x + self.size/2, y+self.size/2)]
            pygame.draw.polygon(surface, palette['scissors'], points)

game_ai = Player(250, palette)





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
        # mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if game_ai.shape_rect.collidepoint(event.pos):
                print('hi')
        
                
                
    screen.fill(palette['bg']) # fill the screen with a color to wipe away anything from last frame

    

    ### UPDATE ###
    
    
    ### DRAW ###

    game_ai.hand = 'rock'
    game_ai.draw_shape(200,500, screen)
    game_ai.hand = 'paper'
    game_ai.draw_shape(600,500, screen)
    game_ai.hand = 'scissors'
    game_ai.draw_shape(900,500, screen)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60
    
pygame.quit()