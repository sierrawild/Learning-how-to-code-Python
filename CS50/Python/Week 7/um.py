import re
import sys


def main():
    # print(count(input("Text: ")))
    print(count(", jumm"))


def count(s):
    pattern = r"\bum\b"
    pattern_count = re.findall(pattern,s, re.IGNORECASE)
    return len(pattern_count)



if __name__ == "__main__":
    main()