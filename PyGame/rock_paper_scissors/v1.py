import pygame, random

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
HANDS = ['rock', 'paper', 'scissors']

# colors
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

# wining hands
wining_hands = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

# functions
def win_check(p1,p2,conditions):
    if p1 == p2:
        print('draw')
        return 'draw'
    elif conditions[p1] == p2:
        print('Player1 wins')
        return 'p1'
    elif conditions[p2] == p1:
        print('Player2 wins')
        return 'p2'
    else:
        print('error')
        return -1


# classes
class Player:
    def __init__(self, size, palette, hand):
        self.hand = hand
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

class Timer:
    def __init__(self, time):
        self.default_time = time
        self.time = time
        
    def count(self, dt):
        self.time -= dt
        if self.time <= 0:
            self.time = self.default_time
            return True
        else:
            return False
timer_1s = Timer(1)
icon_size = 200

# init Player class creating shapes
game_ai = Player(icon_size, palette, None)

rock = Player(icon_size, palette, 'rock')
paper = Player(icon_size, palette, 'paper')
scissors = Player(icon_size, palette, 'scissors')

player_options = [rock, paper, scissors]

# choices variables 
player_choice = None
ai_choice = random.choice(HANDS)

game_ai.hand = ai_choice

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
            for shape in player_options:
                if shape.shape_rect.collidepoint(event.pos):
                    print(shape.hand)
                    player_choice = shape.hand
                    win_check(player_choice, game_ai.hand, wining_hands)
        
    ### UPDATE ###
    if timer_1s.count(dt):
        print('1s')
    
    ### DRAW ###
    screen.fill(palette['bg']) # fill the screen with a color to wipe away anything from last frame
    shape_starting_point = WIDTH / 4
    for i, shape in enumerate(player_options):
        shape.draw_shape(shape_starting_point * (i +1) , 500, screen)

    game_ai.draw_shape(WIDTH/2, 200, screen)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60
    
pygame.quit()