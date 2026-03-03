"""
random_circles_fun.py

Use a function to draw a specified number of circles in random colors.

Programmer: Surajit A. Bose, Date: 2024.05.17
"""

# import statements
from graphics import Canvas
import random

# Constants
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    """
    Instantiate canvas and call function to draw circles.
    
    Preconditions: Constants for canvas width and height are defined.
    
    Postconditions: Circles are drawn.
    """
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for _ in range(N_CIRCLES):
        draw_random_circle(canvas)
            
            
def draw_random_circle(canvas):
    """
    Draw one circles in a random color.
    
    Parameters:
    - canvas, a Canvas object
    
    Preconditions: Constant for the circle diameter is defined
    
    Postconditions: The circle is drawn and fits on the canvas.
    
    Returns: None
    """
    left_x = random.randint(0, CANVAS_WIDTH - CIRCLE_SIZE)
    top_y = random.randint(0, CANVAS_HEIGHT - CIRCLE_SIZE)
    canvas.create_oval(left_x, top_y, 
        left_x + CIRCLE_SIZE, 
        top_y + CIRCLE_SIZE, random_color())
    
def random_color():
    """
    Return a random color from a list of colors. 
    
    Preconditions: None
    
    Postconditions: One color is randomly chosen from a list of colors.
    
    Returns: Randomly chosen color.
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

if __name__ == '__main__':
    main()