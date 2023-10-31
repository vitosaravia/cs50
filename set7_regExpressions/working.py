"""implement a function called convert that expects a str in either 
of the 12-hour formats below and returns the corresponding str in 
24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be 
capitalized (with no periods therein) and that there will be a space 
before each. Assume that these times are representative of actual 
times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of 
those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, 
etc.). But do not assume that someone's hours will start ante meridiem 
and end post meridiem; someone might work late and even long hours 
(e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you're welcome to modify main 
and/or implement other functions as you see fit, but you may not import 
any other libraries. You're welcome, but not required, to use re and/or 
sys."""

import re
import sys


def main():
    print(convert(input("Hours: ").strip().upper()))


def convert(time_input):
    try:
        time_one, time_two = time_input.split("TO")
    except ValueError:
        sys.exit("Invalid input")
    if "AM" in time_one:
        time_format_one = "AM"
    elif "PM" in time_one:
        time_format_one = "PM"
    else:
        time_format_one = ""
    if "AM" in time_two:
        time_format_two = "AM"
    elif "PM" in time_two:
        time_format_two = "PM"
    else:
        time_format_two = ""
    if ":" in time_one and ":" in time_two:
        time_one = time_one.split(":")
        time_one = [int(re.search(r'\d+', time_one[0]).group()), int(re.search(r'\d+', time_one[1]).group()), time_format_one]
        time_two = time_two.split(":")
        time_two = [int(re.search(r'\d+', time_two[0]).group()), int(re.search(r'\d+ ', time_two[1]).group()), time_format_two]

    elif ":" in time_one or ":" in time_two:
        sys.exit("Invalid format")

    else:
        time_one = [int(re.search(r'\d+', time_one).group()), 0, time_format_one]
        time_two = [int(re.search(r'\d+', time_two).group()), 0, time_format_two]

    if time_format_one == "PM":
        time_one[0] = time_one[0] + 12
    if time_format_two == "PM":
        time_two[0] = time_two[0] + 12

    if not 0 <= time_one[0] < 24 or not 0 <= time_one[1] < 60:
        sys.exit("Invalid format")
    if not 0 <= time_two[0] < 24 or not 0 <= time_two[1] < 60:
        sys.exit("Invalid format")

    for i in range(2):
        if len(str(time_one[i])) == 1:
            time_one[i] = "0" + str(time_one[i])

    for j in range(2):
        if len(str(time_two[j])) == 1:
            time_two[j] = "0" + str(time_two[j])

    return str(time_one[0]) + ":" + str(time_one[1]) + " to " + str(time_two[0]) + ":" + str(time_two[1])

if __name__ == "__main__":
    main()