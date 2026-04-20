vowels = ['A','E','I','O','U','a','e','i','o','u']

say = input('Input:').strip()

hey = []

for letter in say:
    if letter not in vowels:
        hey.append(letter)
        
print(''.join(hey))