"""
hospital_karel.py

Karel begins at the left end of a row that has beepers at various points.
The beepers indicate spots where a hospital should be built.
Hospitals are two adjacent columns of three beepers each.

Programmer: Surajit A. Bose, Date: 2025.05.02
"""

from karel.stanfordkarel import *

def main():
    """
    Walk the row and build hospitals where indicated.
    
    Preconditions: 
    - Karel is at one end of the row, facing east
    - Beepers on the row indicate future hospital locations
        
    Postconditions: 
    - Hospitals built
    - Karen is at the other end of the row, facing east
    """
    while front_is_clear():
        move_to_location()
        build_hospital()
        

def move_to_location():
    """
    Move to location where hospital should be built.
    
    Preconditions:
    - Karel is facing east
    - The current corner has no beeper on it
    
    Postconditions:
    - Kael is facing east at a corner with a beeper on it
    """
    while no_beepers_present():
        move()


def build_hospital():
    """
    Build hospital at current corner.
    
    Preconditions: 
    - Karel is on a corner with a beeper indicating a hospital site
    - Karel is facing east
    
    Postconditions: 
    - Hospital is built
    - Karel is facing east
    - If there is a wall in front of Karel, Karel is on the west corner of the hospital
    - If there is no wall, the west corner of the hospital is directly behind Karel
    """
    turn_left()
    build_column()
    turn_right()
    move()
    turn_right()
    build_column()
    turn_left()
    if front_is_clear():
        move()


def build_column():
    """
    Build a single column of beepers.
    
    Preconditions: 
    - Karel is correctly oriented to build a column of three consecutive beepers.
    - There may or may not be a beeper on the corner where Karel is
    
    Postconditions: 
    - Column is built
    - Karel is on top of the third beeper put down, facing the same direction 
    """
    if no_beepers_present():
        put_beeper()
    for i in range(2):
        move()
        put_beeper()


def turn_right():
    """Turn Karel to face right from its original direction."""
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()