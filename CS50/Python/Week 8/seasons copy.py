from datetime import date
import inflect, sys
p = inflect.engine()
today = date.today()
# today = "2003-01-01"

def main():
    dob = input("When wore you born (format: YYYY-MM-DD): ")
    # dob = "2001-01-01"
    
    try:
        print(process(dob, today))
    except ValueError:
        sys.exit("Invalid date")

def process(x, today=None):
    if today is None:
        today = date.today()
    
    if type(today) == str:
        today = today.strip().split("-")
        try:
            today = date(year=int(today[0]),month=int(today[1]),day=int(today[2]))
        except ValueError:
            raise ValueError('Invalid date')

    x = x.strip().split("-")
    try:
        date_of_birth = date(year=int(x[0]),month=int(x[1]),day=int(x[2]))
    except ValueError:
        raise ValueError('Invalid date')
    # today = date.today()
    days = (today - date_of_birth).days
    minutes = days * 24 * 60
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()

