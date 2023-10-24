"""
Implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, n, 
that they would like to buy. If that argument cannot be converted to a float, the 
program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at 
https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, 
among whose nested keys is the current price of Bitcoin as a float. Be sure to 
catch any exceptions, as with code like:
import requests

try:
    ...
except requests.RequestException:
    ...

Outputs the current cost of n Bitcoins in USD to four decimal places, using , as a 
thousands separator.
"""

import sys
import requests

def main():
    try:
        amount = sys.argv[1]
    except:
        sys.exit("Missing command-line argument")
    
    try:
        amount = float(amount)
    except:
        sys.exit("Invalid amount")

    print(f"${_get_price(amount):,.4f}")

def _get_price(amount):
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    if data.status_code == 200:
        # Remove the comma and convert to float
        return amount * float((data.json()['bpi']['USD']['rate']).replace(',', ''))
    else:
        sys.exit(f"Error: {data.status_code}")

if __name__ == "__main__":
    main()