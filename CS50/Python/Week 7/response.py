import validators

def main():
    print(validate(input("What's your email address? ")))


def validate(spam):
    if validators.email(spam):
        return "Valid"
    else:
        return "Invalid"
    
    
if __name__ == "__main__":
    main()