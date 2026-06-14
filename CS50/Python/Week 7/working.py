import re
import sys


def main():
    # print(convert(input("Hours: ")))
    print(convert("13 AM to 5 PM"))


def convert(s):
    regex = r"^([01]?[0-9]\:?[0-5]?\d? [AP]M) to ([01]?[0-9]\:?[0-5]?\d? [AP]M)"
    regex1 = r"^[01]?\d [AP]M"
    if match := re.search(regex,s):
        one, two = match.group(0).strip().split(" to ")
        one, two = one.strip(), two.strip()
        
        
        if re.search(regex1, one):
            one = am_pm_to24h_2(one)
        else:
            one = am_pm_to24h(one) 
            
        if re.search(regex1, two):
            two = am_pm_to24h_2(two)
        else:
            two = am_pm_to24h(two)
        return f"{one} to {two}"
    
        
    else:
        raise ValueError()

def am_pm_to24h(time):
    am_pm = time[-2:]
    ham = time[:-2]
    if am_pm == "AM":
        h,m = ham.strip().split(":")
        if len(h.strip()) == 1:
            h = "0" + h
            ham = h + ":" + m
        elif h == "12":
            h = "00"
            ham = h + ":" + m
        return ham.strip()
    else:
        hours, minutes = ham.strip().split(":")
        hours = int(hours) + 12
        if hours == 24:
            hours = 12
        return f"{hours}:{minutes}"

        
def am_pm_to24h_2(time):
    am_pm = time[-2:]
    ham = time[:-2]
    ham = ham.strip()
    if len(ham) == 1:
        ham = "0" + ham
    if am_pm == "AM":
        if ham == "12":
            ham = "00"
        return f"{ham.strip()}:00"
    else:
        hours = ham.strip()
        hours = int(hours) + 12
        if hours == 24:
            hours = 12
        return f"{hours}:00"
    


if __name__ == "__main__":
    main()