# change directory to current path of the file
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

import csv, sys

# if len(sys.argv) < 3:
#     sys.exit("To few command line arguments")
# if len(sys.argv) > 3:
#     sys.exit("To many command line arguments")

# file_name_1 = sys.argv[1]
# file_name_2 = sys.argv[2]

file_name_1 = "before.csv"
file_name_2 = "after.csv"


if not file_name_1.endswith(".csv"):
    sys.exit("Not CSV file")
if not file_name_2.endswith(".csv"):
    sys.exit("Not CSV file")
try:
    with open(file_name_1) as f:
        file = csv.reader(f)
        headers = next(file)
        data = list(file)
        
        new_file = []
        
        for x in data:
            last, first = x[0]
            house = x[1]
            new_file.append({"first": first.strip(), "last": last.strip(), "house": house.strip()})
        
        with open(file_name_2, "w") as file2:  
            writer = csv.DictWriter(file2, fieldnames=['first','last','house'], restval="", extrasaction="ignore")
            writer.writeheader()
            for entry in new_file:
                writer.writerow(entry)
            
            
except FileNotFoundError:
    sys.exit(f"{file_name_1} not found")
    