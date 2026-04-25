basket = {}
while True:
    try:
        user_input = (input().strip().upper())
        x = basket.get(user_input)
        if x == None:
            basket[user_input] = 1
        else:
            basket[user_input] = x + 1
    except EOFError:
        break
    # except KeyError:
    #     basket

sorted_basket = sorted(basket.items())


for k, v in sorted_basket:
    print(f"{v} {k}")