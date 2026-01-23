"""
archway_no_fun.py

Get Karel over an archway

Programmer: Surajit A. Bose, Date: January 23, 2025
"""

from karel.stanfordkarel import *

def main():
    """
    Move Karel from one corner of the world to the other over an archway
    
    Preconditions: 
    - Karel is on the bottom row leftmost corner facing east
    - There is an archway three squares high blocking Karel's way forward
    
    Postconditions:
    - Karel is on the bottom row rightmost corner facing east 
    - Archway is behind Karel
    """
    # Face north
    turn_left()
    
    # Move forward three spaces
    move()
    move()
    move()
    
    # Turn right to face east
    turn_left()
    turn_left()
    turn_left()
    
    # Move forward three spaces
    move()
    move()
    move()
    
    # Turn right to face south
    turn_left()
    turn_left()
    turn_left()
    
    # Move forward three spaces
    move()
    move()
    move()
    
    # Face east
    turn_left()
    
    
if __name__ == "__main__":
    main()