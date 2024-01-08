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
**************************************
'''
user_input = input(order_request)

print("1 order of " + str(user_input) + ' has been added to your meal')
