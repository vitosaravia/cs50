"""
Suppose that you're in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per 
line, until the user inputs control-d (which is a common way of ending one's input to a 
program). Then output the user's grocery list in all uppercase, sorted alphabetically by 
item, prefixing each line with the number of times the user inputted that item. No need to 
pluralize the items. Treat the user's input case-insensitively.
"""

from collections import Counter

def main():
    items = Counter(get_list())
    if items:
        for item, count in sorted(items.items()):
            print(f"{count} {item.upper()}")

def get_list():
    grocery_list = []
    while True:
        try:
            item_input = input("").strip().lower()
            grocery_list.append(item_input)
        except EOFError:
            print("")
            return grocery_list
        

if __name__ == "__main__":
    main()