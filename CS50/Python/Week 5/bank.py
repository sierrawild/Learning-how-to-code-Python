def main():
    x = input("Greeting: ")
    spam = value(x)
    print(spam)

def value(greeting):
    if greeting[:5] == "hello":
        return '$0'
    elif greeting[:1] == "h":
        return '$20'
    else:
        return '$100'

if __name__ == "__main__":
    main()
