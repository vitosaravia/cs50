"""implement a function called validate that expects an IPv4 address 
as input as a str and then returns True or False, respectively, if 
that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you're welcome to modify main 
and/or implement other functions as you see fit, but you may not import 
any other libraries. You're welcome, but not required, to use re and/or 
sys."""

#import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    ip_numbers = ip.split(".")
    if len(ip_numbers) == 4:
        try:
            for i in ip_numbers:
                if not 0 <= int(i) <= 255:
                    return False
        except ValueError:
            sys.exit("Invalid input.")
    else:
        return False
    return True


if __name__ == "__main__":
    main()