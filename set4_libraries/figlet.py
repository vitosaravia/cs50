"""
FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 
1990s for making large letters out of ordinary text, a form of ASCII art:

 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the 
first of the two should be -f or --font, and the second of the two should be the 
name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font 
or the second is not the name of a font, the program should exit via sys.exit with 
an error message.
"""
import sys
from pyfiglet import Figlet, FigletFont
import random

def main():
    avaliable_fonts = FigletFont.getFonts()

    if 2 < len(sys.argv):
        if "-f" == sys.argv[1] or "--font" == sys.argv[1]:
            font = sys.argv[2]
        else:
            return sys.exit("Invalid usage")
    elif len(sys.argv) == 1:
        font = random.choice(avaliable_fonts)
    else:
        return sys.exit("Invalid usage")

    if font not in avaliable_fonts:
        return sys.exit("Invalid usage")
    else:
        user_input = input("Input: ").strip().lower()
        convert(font, user_input)

def convert(f, text):

    custom_figlet = Figlet(font=f)

    ascii_art = custom_figlet.renderText(text)

    return print(ascii_art)

if __name__ == "__main__":
    main()