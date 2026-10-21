import pygame, random, player_class, palettes
from pathlib import Path


# CONSTANTS
WIDTH, HEIGHT = 1280, 720
HANDS = ['rock', 'paper', 'scissors']
SHAKE_MAX = 25
SHAKE_TIME = 1
WINING_HANDS = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
# colors
COLOR = palettes.default
hands_bg_color = pygame.Color(COLOR['bg'])
h, s, v, a = hands_bg_color.hsva
hands_bg_color.hsva = (h, s,v * 0.9 ,a)
# pygame setup
pygame.mixer.init()
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
# screen shake
screen = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
xoff, yoff = 0,0
shake_timer = 0
# screen name
pygame.display.set_caption('Rock, paper, scissors')
# clock and dt
clock = pygame.time.Clock()
dt = 0

# points
player_points = 0
ai_points = 0

# font
file_dir = Path(__file__).parent/"assets"
font_file = file_dir/"Minecraft.ttf"
font_score_p = pygame.font.Font(font_file, 36)
font_score_ai = pygame.font.Font(font_file, 36)
font_question = pygame.font.Font(font_file, 200)
f_question_surf = font_question.render("?", False, COLOR['text'])
f_question_rect = f_question_surf.get_rect(center=(WIDTH/2, 200))

# sound
sound_draw = pygame.mixer.Sound(file_dir/'draw.wav')
sound_hover = pygame.mixer.Sound(file_dir/'hover.wav')
sound_select = pygame.mixer.Sound(file_dir/'select.wav')
sound_right = pygame.mixer.Sound(file_dir/'right.wav')
sound_wrong = pygame.mixer.Sound(file_dir/'wrong.wav')
sound_lose = pygame.mixer.Sound(file_dir/'lose.wav')
sound_win = pygame.mixer.Sound(file_dir/'win.wav')
sound_end_game_played = False

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
    
def reset_game():
    global player_points, ai_points, sound_end_game_played
    player_points = 0
    ai_points = 0
    sound_end_game_played = False
    return 'player_move'
    


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
game_ai = player_class.Player(icon_size, COLOR, None)
rock = player_class.Player(icon_size, COLOR, 'rock')
paper = player_class.Player(icon_size, COLOR, 'paper')
scissors = player_class.Player(icon_size, COLOR, 'scissors')
player_options = [rock, paper, scissors]

# choices variables 
player_choice = None
ai_choice = random.choice(HANDS)
game_ai.hand = ai_choice



# game state ['player_move', 'end_game', 'reveal', 'evaluate_hand'ga]
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
                    sound_select.play()
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
            sound_wrong.play()
        elif result == 'p1':
            player_points += 1
            sound_right.play()
        elif result == 'draw':
            sound_draw.play()

        game_state = 'reveal'  
        # print(f'Player: {player_choice}   AI: {ai_choice}\nPlayer: {player_points}   AI: {ai_points}\n') # debug
        
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
        counted_1s = timer_1s.count(dt)
        if counted_1s and sound_end_game_played == False:
            if player_points == 3:
                sound_win.play()
                sound_end_game_played = True
            elif ai_points == 3:
                sound_lose.play()
                sound_end_game_played = True
        if counted_3s:
            # print('Counted 3s') #debug
            game_state = reset_game()
    # font update
    f_score_surf_p = font_score_p.render(f'Player: {player_points}', False, COLOR['text'])
    f_score_surf_ai = font_score_ai.render(f'AI: {ai_points}', False, COLOR['text'])

    
    
    ### DRAW ###
    screen.fill(COLOR['bg']) # fill the screen with a color to wipe away anything from last frame
    
    # player choice background
    hands_bg_rect = pygame.Rect(0, 0, WIDTH - 300, 300)
    hands_bg_rect.center = paper.shape_rect.center
    hands_bg_color.hsva = (h, s,v * 0.9 ,a)
    pygame.draw.rect(screen, hands_bg_color, hands_bg_rect,0,50)
    hands_bg_color.hsva = (h, s*0.9,v * 0.8 ,a)
    pygame.draw.rect(screen, hands_bg_color, hands_bg_rect, 10, 50)
    
    # hover
    if game_state == 'player_move':
        mouse_pos = pygame.mouse.get_pos()
        for shape in player_options:
            if shape.shape_rect.collidepoint(mouse_pos):
                shape.hover(screen, COLOR['highlight'], sound_hover)
            else:
                shape.hover_sound_played = False
                
    # draw choices 
    shape_starting_point = WIDTH / 4
    for i, shape in enumerate(player_options):
        shape.draw_shape(shape_starting_point * (i +1) , 500, screen, COLOR)

    if game_state == 'reveal' or game_state == 'end_game':
        game_ai.draw_shape(WIDTH/2, 200, screen, COLOR)
        
    
    # draw score
    p_score_rect = f_score_surf_p.get_rect(center=(200,100))
    ai_score_rect = f_score_surf_ai.get_rect(center=(WIDTH-200,100))
    
    # ????
    if game_state == 'player_move':
        card_rect = pygame.Rect(0,0,250,250)
        card_rect.center = f_question_rect.center
        card_rect.x -= 10 # manual adjustment to align with ?
        card_rect.y -= 30 # manual adjustment to align with ?
        pygame.draw.rect(screen,COLOR['q_card'], card_rect,width=0,border_radius=25)
        screen.blit(f_question_surf, f_question_rect)
    
    # flip() the display to put your work on screen
    window.blit(screen, (xoff, yoff))
    # blit score after shake so it's not affected
    window.blit(f_score_surf_ai, ai_score_rect)
    window.blit(f_score_surf_p, p_score_rect)
    pygame.display.flip()

    # reset player hand
    player_choice = None
    
    dt = clock.tick(60) / 1000 # limits FPS to 60
    
pygame.quit()