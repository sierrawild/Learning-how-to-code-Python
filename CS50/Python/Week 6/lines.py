import sys, os

if len(sys.argv) < 2:
    sys.exit('To few command-line arguments')
if len(sys.argv) > 2:
    sys.exit('To many command-line arguments')

if sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

if os.path.isfile(sys.argv[1]) != True:
    sys.exit('File do not exist')

lines_of_code = 0
with open(sys.argv[1]) as file:
    for line in file:
        if line.lstrip() == "":
            continue
        elif line.lstrip().startswith('#'):
            continue
        else:
            lines_of_code += 1

print(lines_of_code)
