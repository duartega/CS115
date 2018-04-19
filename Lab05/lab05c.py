"""
Program: CS 115 Lab 5c
Author: Gabriel Duarte
Description: This program draws a graph and determines whether
   consecutive points are increasing or decreasing.
"""
from graphics import *


def main():
    window_height = 600
    window = GraphWin('Graph', 800, window_height)

    # Open the input file and read the number of points
    pointsfile = open("points-test.txt", "r")
    num_points = int(pointsfile.readline())

    x = 20
    first_y = int(pointsfile.readline())  # get the first y-coordinate
    first_point = Point(x, window_height - first_y)

    for i in range(1, num_points):  # we already have the first point, so, start with 1.
        # Read the next point and update x
        second_y = int(pointsfile.readline())
        x += 10
        second_point = Point(x, window_height - second_y)


        if second_y > first_y:  # The graph is increasing
            print('y of the first point = ',first_y,', y of second point = ',second_y,'\nincreasing')
        else:
            print('y of the first point = ', first_y, ', y of second point = ', second_y, '\ndecreasing')

        # Draw a line between the first two points
        line = Line(first_point, second_point)
        line.setOutline('orange')
        line.draw(window)

        # Draw a circle centered at the first point
        circle = Circle(first_point, 1)
        circle.draw(window)

        # second_point becomes the first point of the next line
        first_y = second_y
        first_point = second_point

    # Draw the second point
    circle = Circle(first_point, 1)
    circle.draw(window)

    window.getMouse()
    window.close()


main()