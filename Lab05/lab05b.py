"""
Program: CS 115 Lab 5b
Author: Gabriel Duarte
Description: This program draws a line graph.
"""
from graphics import *


def main():
    window_height = 600
    window = GraphWin('Graph', 800, window_height)

    # Open the input file and read the number of points
    pointsfile = open("points-test.txt", "r")
    num_points = int(pointsfile.readline())

    # ---- Draw a line between the first and second points
    x = 20  # see note above
    first_y = int(pointsfile.readline())   # get the first y-coordinate
    first_point = Point(x, window_height - first_y)  # see note above

    # We already have the first point, so start with 1.
    # --------------------------------------------------------------------------------
    for i in range(1, num_points):
        # Read the next point and update
        second_y = int(pointsfile.readline())  # get the second y-coordinate
        x += 10
        second_point = Point(x, window_height - second_y)
        # Draw a line between the first two points
        line = Line(first_point, second_point)
        line.setOutline('orange')
        line.draw(window)

        # Draw a circle centered at the first point
        circle = Circle(first_point, 1)
        circle.draw(window)

        # ---- Draw a line between the second and third points
        first_point = second_point  # the first point of the second line

        # Draw the second point
        circle = Circle(first_point, 1)
        circle.draw(window)
    # --------------------------------------------------------------------------------
    window.getMouse()
    window.close()

main()