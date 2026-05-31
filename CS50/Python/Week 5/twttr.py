vowels = ['A','E','I','O','U','a','e','i','o','u']
def main():


    say = input('Input:').strip()

    hey = shorten(say)

    print(hey)


def shorten(word):
    hey = []
    for letter in word:
        if letter not in vowels:
            hey.append(letter)
    return ''.join(hey)


if __name__ == '__main__':
    main()
