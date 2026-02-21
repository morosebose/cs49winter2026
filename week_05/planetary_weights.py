"""
planetary_weights.py

Prompt the user for a weight on Earth and a planet. 
Print the equivalent weight on specified planet.

Programmer: Surajit A. Bose, Date: 2024.05.10
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
    
    Preconditions: None
    
    Postconditions: 
    - Earth weight received from user
    - Equivalent weight on Mars printed onscreen to two decimal places.
    """
    # Prompt user for a weight on Earth
    weight = float(input("Enter a weight on Earth: "))
    
    # Prompt user for a planet. Ensure first letter is uppercase.
    # Remove leading or trailing spaces
    planet = str.title(input('Enter a planet: ').strip())
    
    # Calculate weight on specified planet
    if planet == "Mercury":
        weight *= MERCURY_GRAVITY
    elif planet == "Venus":
        weight *= VENUS_GRAVITY
    elif planet == "Earth":
        pass        # do nothing
    elif planet == "Mars":
        weight *= MARS_GRAVITY
    elif planet == "Jupiter":
        weight *= JUPITER_GRAVITY
    elif planet == "Saturn":
        weight *= SATURN_GRAVITY
    elif planet == "Uranus":
        weight *= URANUS_GRAVITY
    elif planet == "Neptune":
        weight *= NEPTUNE_GRAVITY
    elif planet == "Mystery":
        weight *= random.random()
    else:       # unknown planet
        weight = 0
        
    # For valid planet, display weight on planet, rounded to 2 decimal places
    if weight != 0:
        weight = round(weight, 2)
        print(f'The equivalent weight on {planet}: {weight}')
    # For invalid planet, print error message
    else:
        print(f'Planet {planet} not recognized.')
    
if __name__ == '__main__':
    main()