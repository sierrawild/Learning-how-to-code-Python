# change directory to current path of the file
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


import csv, sys
from tabulate import tabulate

# if len(sys.argv) < 2:
#     sys.exit("To few command line arguments")
# if len(sys.argv) > 2:
#     sys.exit("To many command line arguments")
# if sys.argv[1][-4:] != ".csv":
#     sys.exit("Not CSV file")

file_name = "regular.csv"
try:
    with open(file_name) as f:
        file = csv.reader(f)
            
        print(tabulate(file, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit(f'{file_name} does not exits')
    