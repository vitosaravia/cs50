"""
In the United States, dates are typically formatted in month-day-year order 
(MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad 
design. Dates in that format can't be easily sorted because the date's year 
comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, 
and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in 
that format are also ambiguous. Harvard was founded on September 8, 1636, 
but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that 
prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) 
order, no matter the country, formatting years with four digits, months with 
two digits, and days with two digits, “padding” each with leading zeroes as 
needed.

In a file called outdated.py, implement a program that prompts the user for a 
date, anno Domini, in month-day-year order, formatted like 9/8/1636 or 
September 8, 1636, wherein the month in the latter might be any of the values 
in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

Then output that same date in YYYY-MM-DD format. If the user's input is not a 
valid date in either format, prompt the user again. Assume that every month has 
no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 
days.

INPUT: 9/8/1636
OUTPUT: 1636-09-08

INPUT: September 8, 1636
output: 1636-09-08
"""

def main():
    while True:
        month, day, year = take_date()
        if format_date(month, day, year):
            return print(format_date(month, day, year))
        else:
            print("Invalid expression")


def take_date():
    date = input("Date: ").strip().lower()
    if "/" in date:
        date_parts = date.split("/")
        if len(date_parts) > 1:
            return int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
        else: print("Invalid Expression")
    elif "," in date:
        date_parts = date.split(" ")
        return date_parts[0].title(), int(date_parts[1][:-1]), int(date_parts[2])


def format_date(month, day, year):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    if isinstance(month, str):
        if month in months:
            month = months.index(month) + 1
        else: return 0
    
    if 1 <= eval(str(day)) <= 31 and 1 <= eval(str(month)) <= 12:   
        if month <10:
            month = "0" + str(month)
        if day <10:
            day = "0" + str(day)
        return f"{year}-{month}-{day}"
    else:
        return 0

if __name__ == "__main__":
    main()