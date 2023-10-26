# -*- coding: utf-8 -*-

"""
In Massachusetts, home to Harvard University, it's possible to request a vanity 
license plate for your car, with your choice of letters and numbers instead of 
random ones. Among the requirements, though, are:

- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and 
a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For 
example, AAA222 would be an acceptable … vanity plate; AAA22A would not be 
acceptable. The first number used cannot be a '0'.”
- “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a vanity plate and 
then output Valid if meets all of the requirements or Invalid if it does not. 
Assume that any letters in the user's input will be uppercase. Structure your 
program per the below, wherein is_valid returns True if s meets all requirements 
and False if it does not. Assume that s will be a str. You're welcome to implement 
additional functions for is_valid to call (e.g., one function per requirement).
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid_1(s):
    #Start with 2 letters
    if s[:2].isalpha():

        #max and min of characters
        if 2 <= len(s) <= 6:

            #Return True if all characters in the string are alphanumeric 
            # and there is at least one character, False otherwise
            if s.isalnum():
                
                # Check if the last character is a number and the first number 
                # is not '0'
                if s[-1].isnumeric() and s[2].isdigit() and s[2] != '0':
                    
                    return True
                else:
                    print(1)
                    return False
            else:
                print(2)
                return False
        else:
            print(3)
            return False
    else:
        print(4)
        return False


def is_valid(s):
    if (s[:2].isalpha() 
        and 2 <= len(s) <= 6 
        and s.isalnum() 
        and s[-1].isnumeric() 
        and s[2].isdigit() 
        and s[2] != '0'):
        return True                
    else:
        return False
    

if __name__ == "__main__":
    main()