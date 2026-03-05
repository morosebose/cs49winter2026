"""
is_odd_shorter.py

Print whether a given number is odd or even. Ignoring the documentation,
this solution is much shorter (i.e., has far fewer lines of code) than the 
one on the Code in Place website. 

Programmer: Surajit A. Bose, Date: 2025.11.23
"""

def main():
    """
    For each integer between 0 and 9 inclusive, print whether the number is odd or even.
    
    Preconditions: None
    
    Postconditions: Number and parity are printed to screen.
    """
    for i in range(10):
        print(f'{i} odd') if is_odd(i) else print(f'{i} even')


# Helper functions, as many as needed to implement the high-level steps
def is_odd (num):
    """
    Checks whether a given number is odd or even.
    
    Parameters: num, an int
    
    Preconditions: None
    
    Postconditions: Parity of num is checked and returned to caller
    
    Returns: Boolean. True if num is odd, False if num is even
    """
    return num % 2 == 1
    
    
if __name__ == "__main__":
    main()
