import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r"\"https?\://www.youtube.com/embed/[\w]+\""
    if match := re.search(regex,s):
        code =  match.group(0).split("/")
        return r"https://youtu.be/" + code[-1][:-1]
    else:
        return None




if __name__ == "__main__":
    main()