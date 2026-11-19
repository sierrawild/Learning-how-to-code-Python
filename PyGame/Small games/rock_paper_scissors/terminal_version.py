import random

hands = ['paper', 'rock', 'scissors']
pc_choice = ''
player_choice = ''

pointsPC = 0
pointsPlayer = 0

points_to_win = 3

def evaluate_game(p1,p2, hands):
    if p1 not in hands or p2 not in hands:
        # wrong input
        return -1
    if p1 == p2:
        #draw
        return 0
    if p1 == hands[0]:
        if p2 == hands[1]:
            return 1
        if p2 == hands[2]:
            return 2
    if p1 == hands[1]:
        if p2 == hands[2]:
            return 1
        if p2 == hands[0]:
            return 2
    if p1 == hands[2]:
        if p2 == hands[0]:
            return 1
        if p2 == hands[1]:
            return 2
    
    
def print_choices(pc_choice, player_choice):
    print(f'PC: {pc_choice}')
    print(f'Player: {player_choice}')

running = True
while running:
    pc_choice = random.choice(hands)
    player_choice = input('rock, paper or scissors:\n').lower().strip()
    
    who_won = evaluate_game(player_choice, pc_choice, hands)
    
    if who_won == 0:
        print_choices(pc_choice, player_choice)
        print('Draw!!!')
    elif who_won == 1:
        print_choices(pc_choice, player_choice)
        print(f'You won!!!')
        pointsPlayer += 1
    elif who_won == 2:
        print_choices(pc_choice, player_choice)
        print(f'You Lose!')
        pointsPC += 1
    elif who_won == -1:
        print('Invalid input \nTry again')
        
    print(f'Player {pointsPlayer} | PC {pointsPC}\n')
    if pointsPC >= points_to_win or pointsPlayer >= points_to_win:
        running = False
        
        
if pointsPC >= points_to_win:
    print('Better luck next time.\nYou lost!!!')
else:
    print('Great, You win!!!')
    
            