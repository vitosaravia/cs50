"""implement a program that expects exactly one command-line argument, 
the name (or path) of a CSV file in Pinocchio's format, and outputs a 
table formatted as ASCII art using tabulate, a package on PyPI at 
pypi.org/project/tabulate. Format the table using the library's grid 
format. If the user does not specify exactly one command-line argument, 
or if the specified file's name does not end in .csv, or if the specified 
file does not exist, the program should instead exit via sys.exit."""

import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith('.csv'):
            menu_table = []
            try:
                with open(sys.argv[1], newline = '') as csv_menu:
                    menu = csv.reader(csv_menu, delimiter = ',', quotechar = '|')
                    for row in menu:
                        menu_table.append(row)
            except FileNotFoundError:
                sys.exit("File does not exist")
            print(tabulate(menu_table[1:], menu_table[0], tablefmt="grid"))
    
        else:
            sys.exit("Not a CSV file")

    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()





