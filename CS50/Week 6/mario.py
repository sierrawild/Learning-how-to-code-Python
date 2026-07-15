while True:
    try:
        h = int(input('Height: '))
        if h < 1 or h > 8:
            raise ValueError('Pleas give a number between 1 and 8')
        break
    except ValueError:
        print('Pleas give a number between 1 and 8')
        
for row in range(1,1+h):
    print(' ' * (h -row) + ('#' * row), end="")
    print("  ", end="")
    print("#" * row)