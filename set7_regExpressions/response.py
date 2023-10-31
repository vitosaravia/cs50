

import re 

def main():
    print(is_valid_email(input("What's your email address? ").strip()))


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return "Valid"
    else:
        return "Invalid"
    
if __name__ == "__main__":
    main()