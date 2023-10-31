

import re 

def main():
    print(is_valid_email(input("What's your email address? ").strip()))


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the re.match() function to search for a match within the string
    if re.match(pattern, email) and email.count('@') == 1 and email.count('..') == 0:
        return "Valid"
    else:
        return "Invalid"
    
if __name__ == "__main__":
    main()