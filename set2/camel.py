"""
implement a program that prompts the user for the name of a variable in 
camel case and outputs the corresponding name in snake case. Assume that 
the user's input will indeed be in camel case.
"""

def main():
    camelCase = input("camelCase: ")

    print(f"snake_case: {convert(camelCase)}")


def convert(phrase):

    snake_case = phrase.lower()

    for i, char in enumerate(phrase):
        if char.isupper():
            snake_case = snake_case[0:i] + "_" + snake_case[i:]

    return snake_case


if __name__ == "__main__":
    main()