import random

lvl = 0

while lvl < 1:
    try:
        lvl = int(input("Level: "))
        if lvl < 1:
            continue
    except ValueError:
        continue

generated_no = random.randint(1,lvl)

guess = -1

while guess != generated_no:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if guess > generated_no:
        print('Too large!')
    elif guess < 1:
        continue
    elif guess < generated_no:
        print('Too small!')
    elif guess == generated_no:
        print('Just right!')
        break
