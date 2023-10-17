"""
One of the most popular places to eat in Harvard Square is Felipe's Taqueria, 
which offers a menu of entrees, per the dict below, wherein the value of each 
key is a price in dollars:

{
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

In a file called taqueria.py, implement a program that enables a user to place 
an order, prompting them for items, one per line, until the user inputs control-d 
(which is a common way of ending one's input to a program). After each inputted 
item, display the total cost of all items inputted thus far, prefixed with a 
dollar sign ($) and formatted to two decimal places. Treat the user's input 
case insensitively. Ignore any input that isn't an item. Assume that every 
item on the menu will be titlecased.
"""

def main():

    total = 0
    items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
        }


    try:
        while True:
            add_order = (input("Item: ")).strip().title()

            if add_order in items.keys():
                total = total + items[add_order]
                print(f"Total: {total}")

    
    except  EOFError:
        pass

    print('')

if __name__ == "__main__":
    main()
