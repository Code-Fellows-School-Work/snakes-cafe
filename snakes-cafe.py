from collections import Counter

# Used ChatGPT to explain how to store a multiline string instead of individually using print function for each line
# Own notes: Contents within the triple quotations define a multiline string
# Own notes: Call the multiline string using the print function and the variable name as a parameter

instructions = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
'''

print(instructions)

menu = '''
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
'''

print(menu)

order_request = '''
**************************************
**  What would you like to order?   **
**     Or type "quit" to exit       **
**************************************
'''

orders = []

# Used a Python Crash Course book by Eric Matthes to learn how to use 'while True loop'
# While True beings the program in an active state and loop will continue running as long as true
while True:
    user_input = input('> What would you like to order? ')
    if user_input == 'quit':
        break
    else:
        orders.append(user_input)
        order_number = Counter(orders)
        # Used ChatGPT to help troubleshoot this loop setup
        for item, count in order_number.items():
            print(f"{count} order of {item} has been added to your meal")