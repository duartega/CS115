"""
    Program: CS 115 Lab 4c
    Author: Gabriel Duarte
    Description: This program draws a few rectangles and fills them with random colors.
                    It also tells you the coordinate, row, and column for each click unless
                    the click is out of bounds. It will then only show the coordinate and
                    will not show a column or row.
"""
from graphics import *
from random import seed, randint
from time import clock


def random_color():
    # Don't worry about the internal details of this function.
    colors = ['blue', 'blue2', 'blue3',
              'green', 'green2', 'green3',
              'orange', 'orange2', 'orange3',
              'red', 'red2', 'red3',
              'purple', 'purple2', 'purple3',
              'yellow', 'yellow2', 'yellow3',
              'gray', 'gray2', 'gray3',
              'pink', 'pink1', 'pink2', 'pink3']

    return colors[randint(0, len(colors)-1)]


def main():
    seed()  # Initialize random number generator

    top_left_x = 100
    top_left_y = 100
    width = 60
    height = 60
    num_rows = int(input('Number of rows: '))
    num_columns = int(input('Number of columns: '))

    window = GraphWin('Lab 4B', 800, 800)



    for i in range(num_columns):
       x = top_left_x + (width*i)
       y = top_left_y

       top_left_point = Point(x, y)
       bottom_right_point = Point(x + width, y + height)
       enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
       enclosing_rectangle.setFill(random_color())
       enclosing_rectangle.draw(window)

    for r in range(num_rows):
        y = top_left_y + (height*r)  # formula based on top_left_y, height, and r

        for c in range(num_columns):
            # Calculate x-coordinate of the top left point of the current square.
            x = top_left_x + (width * c)

            top_left_point = Point(x, y)
            bottom_right_point = Point(x + width, y + height)
            enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
            enclosing_rectangle.setFill(random_color())
            enclosing_rectangle.draw(window)


    for i in range(10):
        c_point = window.getMouse()
        x_c_point = int(c_point.getX())
        y_c_point = int(c_point.getY())
        row = int((y_c_point - top_left_y) // height)+1
        column = int((x_c_point - top_left_x)//width)+1

        if column > num_columns or column < 1 or row > num_rows or row < 1:
            print('The click at (',x_c_point,',',y_c_point,') is outside of the grid.', sep="")
        else:
            print('The click at (',x_c_point,',',y_c_point,') is in row ',row,', column ',column,'.',sep="")



    window.getMouse()
    window.close()

main()