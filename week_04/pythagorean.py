"""
pythagorean.py

Get lengths of two sides of right triangle from user. Display length of hypotenuse.

Programmer: Surajit A. Bose, Date: 2025.02.05
"""

import math

def main():
    """Get length of two sides from user. Display length of hypotenuse."""
    len_AB = float(input("Enter the length of AB: "))
    len_AC = float(input("Enter the length of AC: "))

    sum_of_squares = (len_AB ** 2) + (len_AC ** 2)
    hypotenuse = math.sqrt(sum_of_squares)

    print(f"The length of BC (the hypotenuse) is: {hypotenuse}")
    

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()