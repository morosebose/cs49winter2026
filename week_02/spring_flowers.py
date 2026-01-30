"""
spring_flowers.py

Karel is at the beginning of a row that has two flower stems. 
Karel walks the entire row and puts petals on the stems.

Programmer: Surajit A. Bose, Date: January 24, 2026.
"""

from karel.stanfordkarel import *


def main():
    """Walk the row and makes the flower stems bloom.
    
    Preconditions:
    - Karel starts facing east in the bottom left corner of the world
    - The world has an arbitrary number of columns
    - There are exactly two flower stem walls somewhere in the row
    - Flower stems are of arbitrary height
    - There are at least two rows above the top of each stem

    
    Postconditions:
    - Petals consisting of a 2 x 2 square of beepers are on both stems
    - Karel is at the bottom right corner of the world, facing east
    """
    for i in range(2):
        move_to_wall()
        bloom_flower()
    move_to_wall()      # fencepost condition


def move_to_wall():
    """Move forward until directly before a wall"""
    while front_is_clear():
        move()


def bloom_flower():
    """Put petals on flower stems
    
    Preconditions:
    - Karel is in the bottom row facing east
    - Directly in front of Karel is a flower stem that has no petals
    
    Postconditions:
    - Flower stem has bloomed with petals consisting of 2 x 2 squares of beepers
    """
    go_up_stem()
    put_all_petals()
    come_down_stem()


def turn_right():
    """Turn Karel to the right"""
    for _ in range(3):
        turn_left()


def go_up_stem():
    """Climb the stem"""
    turn_left()
    while right_is_blocked():
        move()


def put_all_petals():
    """Put all petals on a flower stem"""
    put_two_petals()
    turn_right()
    move()
    turn_right()
    put_two_petals()


def come_down_stem():
    """Come down the stem and face east again"""
    move_to_wall()
    turn_left()


def put_two_petals():
    """Place two consecutive beepers"""
    put_beeper()
    move()
    put_beeper()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()