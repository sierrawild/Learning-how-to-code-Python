months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        ad = input('Date: ').strip().title()
        if '/' in ad:
            m, d, y = ad.split("/")
            if len(y) > 4:
                continue
            d = int(d)
            m = int(m)

            if m > 12:
                continue
            if d > 31:
                continue
            print(f'{y}-{m:02d}-{d:02d}')
            break
        elif ',' in ad:
            m,d,y = ad.split(" ")
            if len(y) > 4:
                continue
            if m not in months:
                continue
            d = d.replace(",","")
            d = int(d)
            if d > 31:
                continue

            print(f'{y}-{1+months.index(m):02d}-{d:02d}')
            break
        else:
            continue
    except EOFError:
        break
    except ValueError:
        continue
