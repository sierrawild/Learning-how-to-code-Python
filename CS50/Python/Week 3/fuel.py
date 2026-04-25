def user_input():
    x, y = input("Fraction ").strip().split("/")
    x, y = int(x), int(y)
    return round((x/y)*100)

valid_input = False
while valid_input == False:
    try:
        result = user_input()
        if result < 0:
            continue
        if result > 100:
            continue
        break
    except ZeroDivisionError:    
        # result = user_input()
        continue
    except ValueError:    
        # result = user_input()
        continue

if result <= 1:
    print("E")
elif result >= 99:
    print('F')
else:
    print(f'{result}%')