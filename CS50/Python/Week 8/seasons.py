from datetime import date

def main():
    # dob = input("When wore you born (format: YYYY-MM-DD): ").strip().split("-")
    dob = "1988-01-15".strip().split("-")
    date_of_birth = date(int(dob[0]),int(dob[1]),int(dob[2]))
    today = date.today()
    days = (today - date_of_birth).days
    minutes = days * 24 * 60
    
    print(minutes / 24 / 60 / 365)
    
if __name__ == "__main__":
    main()
    
