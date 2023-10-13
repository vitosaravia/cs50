"""
implement a program that prompts the user for the answer to the Great Question of Life, 
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) 
forty-two or forty two. Otherwise output No.
"""


user_answer = (input("What is the answer to the Great Question of Life, the Universe, and Everything? ")).lower()

if user_answer in ["42", "forty-two", "forty two"]:
    print("Yes!")
else:
    print("No")
