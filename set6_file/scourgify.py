"""implement a program that:

*Expects the user to provide two command-line arguments:
    *the name of an existing CSV file to read as input, whose columns are 
    assumed to be, in order, name and house, and
    *the name of a new CSV to write as output, whose columns should be, in 
    order, first, last, and house.
*Converts that input to that output, splitting each name into a first name 
and last name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first 
cannot be read, the program should exit via sys.exit with an error message."""

import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    output_data = []

    if not input_file.endswith('.csv') or not output_file.endswith('.csv'):
        sys.exit('Invalid file')

    try:
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',', quotechar = '"')

            for i, row in enumerate(reader):
                
                name, house = row
                try:
                    first_name, last_name = name.split(', ')
                except ValueError:
                    if i > 0:
                        sys.exit("Too few information.")
                    else:
                        first_name, last_name = 'first name', 'last name'
                output_data.append([first_name, last_name, house])

        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, ['first name', 'last name', 'house'])
            writer.writerows(output_data)

    except FileNotFoundError:
        sys.exit(f"File not found: {input_file}")



    
if __name__ == "__main__":
    main()
    