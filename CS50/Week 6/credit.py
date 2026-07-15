import sys
card_length = {13, 15, 16}
cards = [{'AMEX': {34, 37}}, 
         {'MASTERCARD': {51, 52, 53, 54, 55}}, 
         {'VISA': {4}},
         'INVALID',]

# ask for input
number = input('Card number: ')
# number = "378282246310005" # debug

def main():
    # check length
    if len(number) not in card_length or number.isnumeric() == False:
        print(cards[3])
        sys.exit()

    valid = validate(number)

    # print output
    if not valid:
        print(cards[3])
    elif int(number[0]) in cards[2]['VISA']:
        print(*cards[2])
    elif int(number[0:2]) in cards[0]['AMEX']:
        print(*cards[0])
    elif int(number[0:2]) in cards[1]['MASTERCARD']:
        print(*cards[1])
        
        


def validate(number): 
    # turn the number into a list and reverse it
    number_list = []
    for i in number:
        number_list.append(i)
    number_list.reverse()

    # Separate to 2 list of even and odd based on position, not the number itself
    even = []
    odd = []
    for index, n in enumerate(number_list):
        if index % 2 != 0:
            even.append(int(n)*2) # number * 2
        else:
            odd.append(int(n))

    # add products of the even numbers together
    spam = 0
    for i in even:
        for j in str(i):
            spam += int(j)

    # add sum of product to odd numbers
    for i in odd:
        spam += i
    
    # check if valid
    if spam % 10 == 0:
        return True
    else:
        return False  

if __name__ == "__main__":
    main()