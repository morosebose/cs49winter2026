"""
fahrenheit_to_celsius.py

Prompt the user for a temperature in Fahrenheit.
Convert the temperature to Celsius and print out the result.

Programmer: Surajit A. Bose, Date: 2025.01.31
"""

def main():
    """Three different solutions, from most readable to most concise. Pick any one!"""

    # Method 1: Most readable
    fahrenheit = input("Enter temperature in Fahrenheit: ")
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Temperature: {fahrenheit}F = {celsius}C")

    # Method 2: Save a step by doing input and casting at once
    # This is the most usual way
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"Temperature: {fahrenheit}F = {celsius}C")

    # Method 3: Shortest. Do the calculation inside the f-string
    # Not recommended in this case, as the code is hard to understand
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"Temperature: {fahrenheit}F = {(fahrenheit - 32) * 5 / 9}C")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()