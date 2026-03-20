"""
pop-up_shop.py

Loop through a dictionary of fruits, prompting the user to see how many of each fruit
they want to buy, then print out the total combined cost of all of the fruits.

Programmer: Surajit A. Bose, Date: June 22, 2025
"""

def main():
    """
    fruits is a dictionary with fruit names as keys and
    the price of the corresponding fruit as values
    """
    fruits = {'apple': 1.5, 
        'durian': 50, 
        'jackfruit': 80, 
        'kiwi': 1, 
        'rambutan': 1.5, 
        'mango': 5}
    
    total = 0
    
    for fruit in fruits:
        num = int(input(f'How many ({fruit}) do you want?: '))
        total += num * fruits[fruit]
    
    print(f'Your total is ${total: .2f}')

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()