"""
implement a program that expects exactly one command-line argument, the name (or path) of a 
Python file, and outputs the number of lines of code in that file, excluding comments and 
blank lines. If the user does not specify exactly one command-line argument, or if the 
specified file's name does not end in .py, or if the specified file does not exist, the 
program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. 
(A docstring should not be considered a comment.) Assume that any line that only contains 
whitespace is blank.
"""


import sys

def count_lines_of_code(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist.")
    
    code_lines = 0
    in_multiline_comment = False

    for line in lines:
        line = line.strip()

        if in_multiline_comment:
            if line.endswith("'''") or line.endswith('"""'):
                in_multiline_comment = False
            continue
        elif line.startswith("'''") or line.startswith('"""'):
            in_multiline_comment = True
            if line.endswith("'''") or line.endswith('"""'):
                in_multiline_comment = False
            continue
        elif line.startswith('#'):
            continue
        elif not line:
            continue
        code_lines += 1

    return print(code_lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments.")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments.")

    file_path = sys.argv[1]
    
    if not file_path.endswith(".py"):
        sys.exit("Not a Python file.")

    count_lines_of_code(file_path)
