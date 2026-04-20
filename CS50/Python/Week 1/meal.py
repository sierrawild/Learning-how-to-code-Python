def main():
    time = input('What time is it? ').strip()

    # am/pm = time

    answer = convert(time)

    if answer >= 7 and answer <= 8:
        print("breakfast time")

    elif answer >= 12 and answer <= 13:
        print("lunch time")

    elif answer >= 18 and answer <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(':')
    return int(h) + (int(m)/60)

if __name__ == "__main__":
    main()
