import csv
import sys

def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print('Provide 2 command line arguments')
        sys.exit(1)
        
    # Read database file into a variable
    try:
        file1 = open(f"{sys.argv[1]}", "r")
        # db = file1.read()
        db = csv.DictReader(file1)
        reader = csv.reader(file1)
        
        # get dna subsequences names
        db_keys = []
        for i in reader:
            db_keys = i
            break
        db_keys.remove("name")
        
    except OSError:
        print("Can't read the database")
        sys.exit(2)
    except FileNotFoundError:
        print("Can't find the database")
        sys.exit(3)
    
    # Read DNA sequence file into a variable
    try:
        file2 = open(f'{sys.argv[2]}')
        dna = file2.read()
    except OSError:
        print("Can't read the file")
        sys.exit(2)
    except FileNotFoundError:
        print("Can't find the file")
        sys.exit(3)
        
        
    # Find longest match of each STR in DNA sequence
    sequence_matches = []
    
    for i in db_keys:
        sequence_matches.append(str(longest_match(dna, i)))

    # Check database for matching profiles
    
    for i in reader:
        if i[1:] == sequence_matches:
            print(i[0])
            sys.exit(0)
    else:
        print('No match')
    
    # close files
    file1.close()
    file2.close()
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run

if __name__ == "__main__":
    main()
