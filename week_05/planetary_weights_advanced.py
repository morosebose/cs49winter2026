"""
planetary_weights_advanced.py

Prompt the user for a weight on Earth and a planet. 
Print the equivalent weight on specified planet.

This solution uses Python's match ... case, an advanced version of if ... elif ... else.

Programmer: Surajit A. Bose, Date: 2025.02.12
"""

import random

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    """
    Get Earth weight. Get planet. Calculate and display weight on planet.
    """
    # Prompt user for a weight on Earth
    weight = float(input("Enter a weight on Earth: "))
    
    # Prompt user for a planet. Ensure first letter is uppercase.
    # Remove leading or trailing spaces
    planet = str.title(input('Enter a planet: ').strip())
    
    # Get gravitational constant for specified planet

    match planet:
        case 'Mercury':
            weight *= MERCURY_GRAVITY
        case 'Venus':
            weight *= VENUS_GRAVITY
        case 'Earth':
            pass        # do nothing
        case 'Mars':
            weight *= MARS_GRAVITY
        case 'Jupiter':
            weight *= JUPITER_GRAVITY
        case 'Saturn':
            weight *= SATURN_GRAVITY
        case 'Uranus':
            weight *= URANUS_GRAVITY
        case 'Neptune':
            weight *= NEPTUNE_GRAVITY
        case 'Mystery':
            weight *= random.random()
        case _:
            weight = 0
            
    # For valid planet, display weight on planet
    if weight:
        print(f'The equivalent weight on {planet}: {planetary_weight:.2f}')
    # For invalid planet, print error message
    else:
        print(f'Planet {planet} not recognized.')
    
if __name__ == '__main__':
    main()