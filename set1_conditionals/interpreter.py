"""
implement a program that prompts the user for an arithmetic expression 
and then calculates and outputs the result as a floating-point value 
formatted to one decimal place. Assume that the user’s input will be 
ormatted as x y z, with one space between x and y and one space between 
y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer
For instance, if the user inputs 1 + 1, your program should output 2.0. 
Assume that, if y is /, then z will not be 0.

"""

def main():
    expression = input("Expression: ")

    try:
        x, y, z = expression.split(" ")
        interpreter(float(x), y, float(z))
    except ValueError:
        print("Invalid expression")

def interpreter(x,y,z):
    print(f"{x}{y}{z}")
    """
    match y:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "*":
            print(x * z)
        case "/":
            try:
                print(x / z)
            except ZeroDivisionError:
                print("Expression x/z: z can not be 0")
"""

if __name__ == "__main__":
    main()