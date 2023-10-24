"""
Implement a program that:

* Prompts the user for a level, n. If the user does not input 1, 2, or 3, 
the program should prompt again.
* Randomly generates ten (10) math problems formatted as X + Y = , wherein 
each of X and Y is a non-negative integer with n digits. No need to support 
operations other than addition (+).
* Prompts the user to solve each of those problems. If an answer is not 
correct (or not even a number), the program should output EEE and prompt 
the user again, allowing the user up to three tries in total for that 
problem. If the user has still not answered correctly after three tries, 
the program should output the correct answer.
* The program should ultimately output the user's score: the number of correct 
answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, 
re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer 
returns a randomly generated non-negative integer with level digits or raises 
a ValueError if level is not 1, 2, or 3:

"""
"""

import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
"""


import random


def main():
    level = get_level()

    for _ in range(10):
        a, b = generate_integer(level)
        tries = 0
        while tries < 3:
            try:
                print(f"{a} + {b} = ", end= "")
                answer = int(input().strip())
                if answer != (a + b):
                    print("EEE")
                    if tries == 2:
                        print(f"{a} + {b} = {a + b}")
                    tries += 1
                else:
                    tries = 4
            except EOFError:
                return False
        
def get_level():
    while True:
        level = (input("Level: ").strip())
        if level in {"1","2","3"}:
            return int(level)
        
        
def generate_integer(level):
    if level == 1:
        n = 9
    elif level == 2:
        n = 99
    else:
        n = 999
    
    return random.randint(0, n), random.randint(0, n)

if __name__ == "__main__":
    main()