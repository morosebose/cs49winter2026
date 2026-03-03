"""
this_big.py

Draw a square of dimensions THIS_BIG, centered at CENTER_X, CENTER_Y

Programmer: Surajit A. Bose, Date: May 30, 2025
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
THIS_BIG = 144
CENTER_X = 160
CENTER_Y = 160

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    left_x = CENTER_X - THIS_BIG / 2
    top_y = CENTER_Y - THIS_BIG / 2

    canvas.create_rectangle(left_x, top_y, left_x + THIS_BIG, top_y + THIS_BIG)

    # Comment out line 23 and try these alternative approaches!

    # Alternative approach 1: calculate right_x and bottom_y using THIS_BIG
    # right_x = left_x + THIS_BIG
    # bottom_y = top_y + THIS_BIG
    # canvas.create_rectangle(left_x, top_y, right_x, bottom_y)

    # Alternative approach 2: calculate right_x and bottom_y using CENTER_X and CENTER_Y
    # right_x = CENTER_X + THIS_BIG / 2
    # bottom_y = CENTER_Y + THIS_BIG / 2
    # canvas.create_rectangle(left_x, top_y, right_x, bottom_y)
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()