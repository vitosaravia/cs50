# -*- coding: utf-8 -*-

"""
implement a program that prompts the user for a greeting. If the greeting starts with “hello”, 
output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. 
Ignore any leading whitespace in the user's greeting, and treat the user's greeting case-insensitively.
"""

import re

def main():

    print(value(input("Greeting: ").lower().strip()))

def value(greeting):
    if re.match("hello", greeting):
        return "$0"
    elif re.match("h", greeting):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()