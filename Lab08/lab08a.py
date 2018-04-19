"""
Program: CS 115 Lab 8a
Author: Gabriel Duarte
Description: This program displays national flags.
"""

from graphics import *

def draw_stripe(window, top_left, bottom_right, color):
    '''
    Draws a rectangle in the window
    Parameters:
    - window: the window to draw in
    - top_left: the coordinates of the top left corner (as a Point)
    - bottom_right: the coordinates of the bottom right corner (as a Point)
    - color: the color to make the rectangle (as a string)

    Returns: nothing
    '''
    stripe = Rectangle(top_left, bottom_right)
    stripe.setFill(color)
    stripe.setOutline(color)
    stripe.draw(window)

def draw_triangle(window,P1,P2,P3,color):
    triangle = Polygon(P1,P2,P3)
    triangle.setFill(color)
    triangle.setOutline(color)
    triangle.draw(window)


def draw_france_flag(flag_width):
    '''
    Draws a French flag in the graphics window.
    Parameter: the width of the window
    Returns: nothing
    '''

    flag_height = 2 / 3 * flag_width
    stripe_colors = ['DarkBlue', 'white', 'red']
    stripe_width = flag_width / len(stripe_colors)

    # Open a new graphics window with the title 'French flag', the
    # width provided by the user, and the calculated height
    window = GraphWin('French flag', flag_width, flag_height)

    flag_width_Stripes = 0
    for i in range(3):
        flag_width_Stripes += 200
        stripe_top_left = Point(i*stripe_width,0)
        stripe_bottom_right = Point(flag_width_Stripes, flag_height)
        draw_stripe(window,stripe_top_left,stripe_bottom_right,stripe_colors[i])
        #print('stripe_top_left:',stripe_top_left,'\nstripe_bottom_right:',stripe_bottom_right)

    # Close?
    input('Press ENTER to close the flag window.')
    window.close()

def draw_russia_flag(flag_width):
    '''
    Draws a French flag in the graphics window.
    Parameter: the width of the window
    Returns: nothing
    '''

    flag_height = 2 / 3 * flag_width
    stripe_colors = ['white','blue','red']
    stripe_width = flag_height / len(stripe_colors)

    # Open a new graphics window with the title 'Rusian flag', the
    # width provided by the user, and the calculated height
    window = GraphWin('Russian flag', flag_width, flag_height)

    flag_height_stripes = 0
    for i in range(3):
        flag_height_stripes += flag_height / 3
        stripe_top_left = Point(0, i*stripe_width)
        stripe_bottom_right = Point(flag_width, flag_height_stripes)
        draw_stripe(window, stripe_top_left, stripe_bottom_right, stripe_colors[i])

        print('stripe_top_left:',stripe_top_left,'\nstripe_bottom_right:',stripe_bottom_right)

    # Close?
    input('Press ENTER to close the flag window.')
    window.close()

def draw_sudan_flag(flag_width):
    '''
    Draws a French flag in the graphics window.
    Parameter: the width of the window
    Returns: nothing
    '''

    flag_height = 1/2 * flag_width
    stripe_colors = ['red','white','black']
    stripe_width = flag_height / len(stripe_colors)

    # Open a new graphics window with the title 'French flag', the
    # width provided by the user, and the calculated height
    window = GraphWin('Sudan flag', flag_width, flag_height)

    flag_height_stripes = 0
    for i in range(3):
        flag_height_stripes += flag_height / 3
        stripe_top_left = Point(0, i*stripe_width)
        stripe_bottom_right = Point(flag_width, flag_height_stripes)
        draw_stripe(window, stripe_top_left, stripe_bottom_right, stripe_colors[i])
        draw_triangle(window, Point(0,0), Point(200,150), Point(0,300), "darkgreen")


        print('stripe_top_left:',stripe_top_left,'\nstripe_bottom_right:',stripe_bottom_right)

    # Close?
    input('Press ENTER to close the flag window.')
    window.close()

def draw_bangladesh_flag(flag_width):
    ''' Draws the national flag of Japan in a graphics window.

    Parameter: the width of the window
    Returns: nothing
    '''
    flag_height = 3 / 5 * flag_width
    circle_diameter = (2 / 5 * flag_height) + 96

    # Open a new graphics window with the title 'Bangladesh flag',
    # the width passed by the caller, and the calculated height
    win = GraphWin('Bangladesh flag', flag_width, flag_height)

    # Set the window background to white
    win.setBackground('darkgreen')

    # Set up the red circle.
    flag_center = Point(flag_width * (9/20), flag_height / 2)
    circle_radius = circle_diameter / 2

    # Create a circle that is centered in the middle of the flag
    # and has the specified radius
    circ = Circle(flag_center, circle_radius)

    # Turn that circle red
    circ.setFill('red')     # the inside of the circle
    circ.setOutline('red')  # the line around the circle

    # Actually draw the circle
    circ.draw(win)

    # Close?
    input('Press ENTER to close the flag window.')
    win.close()




def draw_japan_flag(flag_width):
    ''' Draws the national flag of Japan in a graphics window.

    Parameter: the width of the window
    Returns: nothing
    '''
    flag_height = 2 / 3 * flag_width
    circle_diameter = 3 / 5 * flag_height

    # Open a new graphics window with the title 'Japanese flag',
    # the width passed by the caller, and the calculated height
    win = GraphWin('Japanese flag', flag_width, flag_height)

    # Set the window background to white
    win.setBackground('white')

    # Set up the red circle.
    flag_center = Point(flag_width / 2, flag_height / 2)
    circle_radius = circle_diameter / 2

    # Create a circle that is centered in the middle of the flag
    # and has the specified radius
    circ = Circle(flag_center, circle_radius)

    # Turn that circle red
    circ.setFill('red')     # the inside of the circle
    circ.setOutline('red')  # the line around the circle

    # Actually draw the circle
    circ.draw(win)

    # Close?
    input('Press ENTER to close the flag window.')
    win.close()


# --- Our main function ---
def main():

    x = input("Please enter a country: ")
    flags = x.lower().split()
    for flag in flags:
        if flag == 'japan':
            draw_japan_flag(600)  # Draw a Japanese flag with a width of 600 pixels
        elif flag == 'bangladesh':
            draw_bangladesh_flag(600)
        elif flag == 'france':
            draw_france_flag(600)
        elif flag == 'russia':
            draw_russia_flag(600)
        elif flag =='sudan':
            draw_sudan_flag(600)
main()