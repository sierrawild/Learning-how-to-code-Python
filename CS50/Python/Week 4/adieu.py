import inflect

p = inflect.engine()


prefix = 'Adieu, adieu, to '
names = []


while True:
    try:
        name = input("Name: ").strip().title()
        names.append(name)
    except EOFError:
        break
print("")
print(f'Adieu, adieu, to {p.join(names)}')
