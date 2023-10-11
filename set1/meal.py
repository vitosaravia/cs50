"""
implement a program that prompts the user for a time and outputs whether it's breakfast time, 
lunch time, or dinner time. If it's not time for a meal, don’t output anything at all. Assume 
that the user's input will be formatted in 24-hour time as #:## or ##:##. And assume that each 
meal's time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime 
in between, it's time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) 
that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For 
instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 
(i.e., 7.5 hours).

"""

def main():
    
    time = input("What time is it? ")

    if convert(time):
        time_float = convert(time)
        if time_float >= 7 and time_float <= 8:
            print("breakfast time")
        elif time_float >= 12 and time_float <= 13:
            print("lunch time")
        elif time_float >= 18 and time_float <= 19:
            print("dinner time")
        else:
            return
    else:
        print("Invalid expression")

def convert(time):

    try:
        hour, minutes = map(float, time.split(":"))
    except ValueError:

        return False
    
    if hour >= 24 or minutes >= 60:

        return False

    else:
        minutes = minutes / 60

        time = float(hour + minutes)

        return time


if __name__ == "__main__":
    main()