import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex1 = r"<iframe.+</iframe>"
    regex2 = r"\"https?\://(www\.)?youtube\.com/embed/[\w]+\""
    if match1 := re.search(regex1,s):
        if match := re.search(regex2,match1.group(0)):
            code =  match.group(0).split("/")
            return r"https://youtu.be/" + code[-1][:-1]
        else:
            return None
    else:
        return None




if __name__ == "__main__":
    main()
