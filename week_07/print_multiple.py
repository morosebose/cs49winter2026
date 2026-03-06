"""
print_multiple.py

Print out a given message a given number of times.

Programmer: Surajit A. Bose, Date: 2025.11.23
"""

def main():
    """
    Ask user to input a message and the number of repeats. Call function to print
    message onscreen the specified number of times.
    
    Preconditions: None
    
    Postconditions: Function is called with the appropriate parameters.
    """
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)


# Helper functions, as many as needed to implement the high-level steps
def print_multiple(string, num):
    """
    Print a given message to the screen a specified number of times.
    
    Parameters:
    - string, a str to be printed
    - num, an int specifying the number of times string should be printed
    
    Preconditions: None
    
    Postconditions: string is printed to screen num times
    
    Returns: None
    """
    for _ in range(num):
        print(string)

if __name__ == "__main__":
    main()
