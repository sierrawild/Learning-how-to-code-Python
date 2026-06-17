from datetime import date

def main():
    dob = input("When wore you born (format: YYY-MM-DD): ")
    today = date.today()
    
    print(f'{dob=} and {today=}')
    
if __name__ == "__main__":
    main()