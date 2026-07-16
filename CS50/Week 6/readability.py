import re
text = input('Text: ')

word_no = len(text.split(' '))
sentence_no = len(re.split(r'[.!?]',text)) -1
char_no = 0
for i in text:
    if i.isalpha() or i.isdigit():
        char_no += 1

L = (char_no / word_no) * 100
S = (sentence_no / word_no) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)


if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f'Grade {index}')
