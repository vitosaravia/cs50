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

"""

extensions = {
    "gif": "image", 
    "jpg": "image", 
    "jpeg": "image",
    "png": "image",
    "pdf": "application", 
    "txt": "application",
    "zip": "unknown",
}

file_name = (input("File name: ")).lower()

file_extension = (file_name.split("."))[-1]

if file_extension in extensions.keys():
    print(f"{extensions[file_extension]}/{file_extension}")
else:
    print("application/octet-stream")