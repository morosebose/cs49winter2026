"""
in_range.py

Check whether a given integer is within a given range and print result to screen.

Programmer: Surajit A. Bose, Date: 2024.05.31
"""

def main():
    """
    Get user input for n, low, and high and display whether n is in range.

    Preconditions: None

    Postconditions: 
        - If n is in the range between low and high, print "n is in range!"
        - If not print "n is not in range..."
    """
    # Get user input
    n = int(input('n: '))

    # Get the other inputs
    lo = int(input('low: '))
    hi = int(input('high: '))

    # Pass all of them as arguments in a call to in_range()
    # Print message based on the return from in_range()
    if in_range(n, lo, hi):
        print('n is in range!')
    else:
        print('n is not in range ...')


def in_range(n, low, high): 
    """
    Check whether given integer n is between low and high, inclusive.

    Parameters: 
        n, number to be checked
        low, low end of range
        high, high end of range

    Preconditions: high is greater than low

    Postconditions: None

    Returns: Boolean whether n is between low and high, inclusive. 
    """
    return low <= n <= high
    
    """
    # Alternate implementation demonstrating early return
    if low > n:
        return False
    if high < n:
        return False
    return True
    """


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()