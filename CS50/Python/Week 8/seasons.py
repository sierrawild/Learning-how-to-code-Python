from datetime import date
import inflect
p = inflect.engine()
today = date.today()
today = "2003-01-01"

def main():
    # dob = input("When wore you born (format: YYYY-MM-DD): ")
    dob = "2001-01-01"
    print(process(dob, today))

def process(x, today):
    if type(today) == str:
        today = today.strip().split("-")
        today = date(year=int(today[0]),month=int(today[1]),day=int(today[2]))
    
    
    x = x.strip().split("-")
    try:
        date_of_birth = date(year=int(x[0]),month=int(x[1]),day=int(x[2]))
    except ValueError:
        return "Invalid date"
    # today = date.today()
    days = (today - date_of_birth).days
    minutes = days * 24 * 60
    return p.number_to_words(minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()

