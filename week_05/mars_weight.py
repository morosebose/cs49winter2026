"""
mars_weight.py

Prompt the user for a weight on Earth and print the equivalent weight on Mars.

Programmer: Surajit A. Bose, Date: 2025.10.31
"""

# Gravity on Mars is lower, so a person would weigh 37.8% less than on Earth
MARS_CONVERSION_RATE = 0.378

def main():
    """
    Get Earth weight. Calculate and display Mars weight to two decimal places.
    """
    
    # Get earth weight
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # First solution: calculate and round mars_weight in two separate steps
    """
    mars_weight = earth_weight * MARS_CONVERSION_RATE
    mars_weight = round(mars_weight, 2)
    """
    
    # Recommended solution: Combine calculation and rounding in one step
    mars_weight = round(earth_weight * MARS_CONVERSION_RATE, 2)
    
    # print using f-strings
    print(f"The equivalent weight on Mars: {mars_weight}")

    # Two other ways to print, not recommended: commas and plus signs
    # print("The equivalent weight on Mars:", mars_weight)
    # print("The equivalent weight on Mars: " + str(mars_weight))
    
    # Instead of using round(), can use f-strings to round while displaying
    # Get earth weight, calculate mars_weight as in line 22 above, then print:
    # print(f"The equivalent weight on Mars: {mars_weight:.2f}")
    # :.2f  inside the braces after mars_weight means:
    # display mars_weight as a float with two decimal places
    
if __name__ == '__main__':
    main()