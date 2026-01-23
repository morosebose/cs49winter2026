"""
archway_with_fun.py

Get Karel over an archway. Streamline code using functions.

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
    turn_left()             # face north
    move_three_spaces()
    turn_right()            # face east
    move_three_spaces()
    turn_right()            # face south
    move_three_spaces()
    turn_left()             # face east

    
def turn_right():
    """Turn Karel to face right"""
    turn_left()
    turn_left()
    turn_left()
    

def move_three_spaces():
    """Move Karel forward three corners at once"""
    move()
    move()
    move()
    
    
if __name__ == "__main__":
    main()