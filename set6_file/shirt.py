"""implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the 
input after resizing and cropping the input to be the same size, saving the result as 
its output.

Open the input with Image.open, per 
pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop 
the input with ImageOps.fit, per 
pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default 
values for method, bleed, and centering, overlay the shirt with Image.paste, per 
pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the 
result with Image.save, per 
pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

if the user does not specify exactly two command-line arguments,
if the input's and output's names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input's name does not have the same extension as the output's name, or
if the specified input does not exist.
Assume that the input will be a photo of someone posing in just the right way, like these 
demos, so that, when they're resized and cropped, the shirt appears to fit perfectly.

If you'd like to run your program on a photo of yourself, first drag the photo over to VS 
Code's file explorer, into the same folder as shirt.py. No need to submit any photos with 
your code. But, if you would like, you're welcome (but not expected) to share a photo of 
yourself wearing your virtual shirt in any of CS50's communities!


os.path.splitext(input_file)[1][1:] != 'csv'"""

import sys
import os
from PIL import Image, ImageOps


def main():

    if len(sys.argv) == 3:
        read = sys.argv[1]
        write = sys.argv[2]
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")

    if os.path.splitext(read)[1][1:] in {"jpg", "png", "jpeg"}:
        if os.path.splitext(read)[1][1:] == os.path.splitext(write)[1][1:]:
            try_shirt(read, write)
        else:
            sys.exit("Input and output have different extensions.")
    else:
        sys.exit("Invalid input")

def try_shirt(input_path, output_path):
    try:
        with Image.open(input_path) as input_image:
            shirt = Image.open(input_path)

            input_image = ImageOps.fit(input_image, size=(1000,1000))

            input_image.paste(shirt, (0, 0), shirt)

            input_image.save(output_path)

    except FileNotFoundError:
        sys.exit('Input does not exist.')

if __name__ == "__main__":
    main()