def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) > 6 or len(s) < 2:
        return False
    if s[:2].isalpha() == False:
        return False
    if number_check(s) == True:
        return False

    return True

def number_check(s):
    no_start = False
    for i in s:
        if no_start == False and i == "0":
            return True
        if i.isdigit() == True:
            no_start = True
        if i.isalpha() and no_start == True:
            return True

        if i.isdigit() == False and i.isalpha() == False:
            return True
    return False



if __name__ == "__main__":
    main()
