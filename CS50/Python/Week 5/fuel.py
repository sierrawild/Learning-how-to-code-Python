def main():
    spam = input("Fraction ").strip()
    fuel_lvl = convert(spam)
    print(gauge(fuel_lvl))

def convert(fraction):
    x, y = fraction.strip().split("/")
    # check if inputs are numbers
    if x.isdecimal() == False:
        raise ValueError('x is not a number')
    if y.isdecimal() == False:
        raise ValueError('y is not a number')
    
    # change to ints
    x, y = int(x), int(y)
    
    if y == 0:
        
        raise ZeroDivisionError("Can't divide by 0")
    if x > y:
        raise ValueError('x is greater than y')
    
    
    return round((x/y)*100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return 'F'
    else:
        return(f'{percentage}%')

def user_input():
    x, y = input("Fraction ").strip().split("/")
    x, y = int(x), int(y)
    return round((x/y)*100)

if __name__ == "__main__":
    main()
