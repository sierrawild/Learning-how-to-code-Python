import random


def main():
    lvl = get_level()
    
    problems = generate_integer(lvl)

    
    score = 0
    wrong_answer = "EEE"
    
    for i in problems:
        lives = 3
        answer = -1
        correct_answer = i[0] + i[1]
        
        # getting the answer
        while True:
            if lives <= 0:
                print(f'{i[0]} + {i[1]} = {correct_answer}')
                break
            try:
                answer = int(input(f'{i[0]} + {i[1]} = '))
            except ValueError:
                lives -= 1
                print(wrong_answer)
                continue
            
            # checking the answer
            if answer == correct_answer:
                score += 1
                break
            elif answer != correct_answer:
                lives -= 1
                continue
    print(f'Score: {score}')
        
        
    
    

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl > 3 or lvl < 1:
                raise ValueError
            return lvl
        except ValueError:
            continue
    

def generate_integer(level):
    if level == 1:
        x_lvl, y_lvl = 0, 9
    if level == 2:
        x_lvl, y_lvl = 10, 99
    if level == 3:
        x_lvl, y_lvl = 100, 999
        
    problems = []
    for _ in range(10):
        problems.append((random.randrange(x_lvl,y_lvl), random.randrange(x_lvl,y_lvl)))

    return problems

if __name__ == "__main__":
    main()
