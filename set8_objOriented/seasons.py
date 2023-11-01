"""implement a program that prompts the user for their date 
of birth in YYYY-MM-DD format and then sings prints how old 
they are in minutes, rounded to the nearest integer, using 
English words instead of numerals, just like the song from 
Rent, without any and between words. Since a user might not 
know the time at which they were born, assume, for 
simplicity, that the user was born at midnight 
(i.e., 00:00:00) on that date. And assume that the current 
time is also midnight. In other words, even if the user runs 
the program at noon, assume that it's actually midnight, on 
the same date. Use datetime.date.today to get today's date, 
per docs.python.org/3/library/datetime.html#datetime.date.today."""

import sys
import inflect
from datetime import date, datetime

def main():
    print(minutes(input("Date of Birth (YYYY-MM-DD): ").strip()))

def minutes(birth_date):

    try: birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    except: sys.exit("Invalid date")

    age = datetime.today() - birth_date

    age = int(age.total_seconds() // 60)

    return inflect.engine().number_to_words(age)


if __name__ == "__main__":
    main()