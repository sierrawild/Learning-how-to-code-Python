import inflect

p = inflect.engine()


prefix = 'Adieu, adieu, to '
names = []


while True:
    try:
        name = input("Name: ").strip().title()
        if name:
            names.append(name)
    except EOFError:
        break

print(f'Adieu, adieu, to {p.join(names)}')
