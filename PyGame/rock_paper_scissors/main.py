import pygame, random, player_class, palettes
from pathlib import Path

# TODO Sound
# TODO Reset game
# TODO Announce the winner

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
HANDS = ['rock', 'paper', 'scissors']
SHAKE_MAX = 25
SHAKE_TIME = 1
WINING_HANDS = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
# pygame setup
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
# screen shake
screen = pygame.Surface((WIDTH, HEIGHT))
xoff, yoff = 0,0
shake_timer = 0
# screen name
pygame.display.set_caption('Rock, paper, scissors')
# clock and dt
clock = pygame.time.Clock()
dt = 0
# colors
palette = palettes.default
palette = palettes.bw

# points
player_points = 0
ai_points = 0

# font
file_dir = Path(__file__).parent/"assets"
font_file = file_dir/"Minecraft.ttf"
font_score_p = pygame.font.Font(font_file, 36)
font_score_ai = pygame.font.Font(font_file, 36)
font_question = pygame.font.Font(font_file, 100)
f_question_surf = font_question.render("?", False, palette['text'])
f_question_rect = f_question_surf.get_rect(center=(WIDTH/2, 200))

# functions
def win_check(p1,p2,conditions):
    if p1 == p2:
        return 'draw'
    elif conditions[p1] == p2:
        return 'p1'
    elif conditions[p2] == p1:
        return 'p2'
    else:
        print('error')
        return -1


# classes
class Timer:
    def __init__(self, time):
        self.default_time = time
        self.time = time
        
    def count(self, dt):
        self.time -= dt
        if self.time <= 0:
            self.time = self.default_time
            return True # return True when timer reaches 0 
        else:
            return False
timer_1s = Timer(1)
timer_3s = Timer(3)




# init Player class creating shapes
icon_size = 200
game_ai = player_class.Player(icon_size, palette, None)
rock = player_class.Player(icon_size, palette, 'rock')
paper = player_class.Player(icon_size, palette, 'paper')
scissors = player_class.Player(icon_size, palette, 'scissors')
player_options = [rock, paper, scissors]

# choices variables 
player_choice = None
ai_choice = random.choice(HANDS)
game_ai.hand = ai_choice



# game state ['player_move', 'end_game', 'reveal', 'evaluate_hand']
game_state = 'player_move'
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
        elif game_state == 'player_move' and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for shape in player_options:
                if shape.shape_rect.collidepoint(event.pos):
                    player_choice = shape.hand
                    game_state = 'evaluate_hand'
                    
    ### UPDATE ###
    # screen shake
    if shake_timer > 0:
        shake_timer = max(0, shake_timer - dt)
        magnitude = SHAKE_MAX * (shake_timer / SHAKE_TIME)
        xoff = random.uniform(-magnitude, magnitude)
        yoff = random.uniform(-magnitude, magnitude)
    else:
        xoff = yoff = 0
    
    # evaluate hand
    if game_state == 'evaluate_hand':
        
        result = win_check(player_choice, game_ai.hand, WINING_HANDS)
        if result == 'p2':
            ai_points +=1
            shake_timer += SHAKE_TIME
        elif result == 'p1':
            player_points += 1
        game_state = 'reveal'  
        print(f'Player: {player_choice}   AI: {ai_choice}\nPlayer: {player_points}   AI: {ai_points}\n')
        
    # reveal ai hand
    if game_state == 'reveal':
        counted_1s = timer_1s.count(dt)
        if counted_1s:
            game_state = 'player_move'
            game_ai.hand = random.choice(HANDS)
        
    # game over
    if player_points == 3 or ai_points == 3:
        game_state = 'end_game'
        counted_3s = timer_3s.count(dt)
        if counted_3s:
            print('Counted 3s')
            # TODO Reset game
    # font update
    f_score_surf_p = font_score_p.render(f'Player: {player_points}', False, palette['text'])
    f_score_surf_ai = font_score_ai.render(f'AI: {ai_points}', False, palette['text'])

    ### DRAW ###
    screen.fill(palette['bg']) # fill the screen with a color to wipe away anything from last frame
    shape_starting_point = WIDTH / 4
    for i, shape in enumerate(player_options):
        shape.draw_shape(shape_starting_point * (i +1) , 500, screen, palette)

    if game_state == 'reveal' or game_state == 'end_game':
        game_ai.draw_shape(WIDTH/2, 200, screen, palette)
    
    # draw score
    p_score_rect = f_score_surf_p.get_rect(center=(200,100))
    ai_score_rect = f_score_surf_ai.get_rect(center=(WIDTH-200,100))
    
    # ????
    if game_state == 'player_move':
        card_rect = pygame.Rect(0,0,250,250)
        card_rect.center = f_question_rect.center
        pygame.draw.rect(screen,palette['scissors'], card_rect,width=0,border_radius=25)
        screen.blit(f_question_surf, f_question_rect)
    
    # flip() the display to put your work on screen
    window.blit(screen, (xoff, yoff))
    # blit score after shake so it's not affected
    window.blit(f_score_surf_ai, ai_score_rect)
    window.blit(f_score_surf_p, p_score_rect)
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60
    
pygame.quit()