"""
five_corridors.py

Traverse 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.

Programmer: Surajit A. Bose, Date: February 6, 2026.
"""

from karel.stanfordkarel import *

def main():
    """
    Ensure that there is a beeper at the end of each corridor.

    Preconditions:
    - Karel is at the bottom left corner of a world with five rows.
    - Each row is a corridor ending at a wall
    - Some rows may have a beeper directly before the wall.

    Postconditions:
    - Karel is at the top left corner of the world
    - All rows have a beeper before the wall.
    """
    for _ in range(4):
        complete_one_row()
        move_to_next_row()
    complete_one_row()      # fencepost condition


def complete_one_row():
    """Ensure there is a beeper at the end of the corridor.

    Preconditions: 
    - Karel is facing east at the beginning of a corridor
    - There may or may not be a beeper at the end of the corridor.

    Postconditions:
    - There is a beeper at the end of the corridor
    - Karel is back to the starting point, facing east.
    """
    move_to_wall()
    if no_beepers_present():
        put_beeper()
    turn_around()
    move_to_wall()
    turn_around()


def move_to_next_row():
    """Move Karel to next row"""
    turn_left()
    move()
    turn_right()


def turn_right():
    """Turn Karel to face the right"""
    for i in range(3):
        turn_left()


def turn_around():
    """Turn Karel around 180 degrees"""
    turn_left()
    turn_left()


def move_to_wall():
    """Move Karel forward up to the wall"""
    while front_is_clear():
        move()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
