"""
implement a program that prompts the user for the name of a 
file and then outputs that file's media type if the file's 
name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

If the file’s name ends with some other suffix or has no 
suffix at all, output application/octet-stream instead, 
which is a common default.

"""

import os

def main():
    extensions = {
        "gif": "image", 
        "jpg": "image", 
        "jpeg": "image",
        "png": "image",
        "pdf": "application", 
        "txt": "application",
        "zip": "unknown",
    }

    file_name = input("File name: ").strip().lower()

    file_extension = file_name.split(".")[-1]

    if file_extension in extensions.keys():
        print(f"{extensions[file_extension]}/{file_extension}")
    else:
        print("application/octet-stream")


def another_way():

    extensions = {
        "gif": "image", 
        "jpg": "image", 
        "jpeg": "image",
        "png": "image",
        "pdf": "application", 
        "txt": "application",
        "zip": "unknown",
    }

    file_name = input("File name: ").strip().lower()

    extension = os.path.splitext(file_name)[1][1:]

    if extension in extensions.keys():
        print(f"{extensions[extension]}/{extension}")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    another_way()
    #main()