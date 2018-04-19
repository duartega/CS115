"""
Program: CS 115 Lab 5d
Author: Gabriel Duarte
Description: This program draws a graph and identifies turning points.
"""
from graphics import *


def main():
    window_height = 600
    window = GraphWin('Graph', 800, window_height)

    # Open the input file and read the number of points
    pointsfile = open("points.txt", "r")
    num_points = int(pointsfile.readline())

    x = 20
    first_y = int(pointsfile.readline())  # get the first y-coordinate
    first_point = Point(x, window_height - first_y)

    x += 10
    second_y = int(pointsfile.readline())
    second_point = Point(x, window_height - second_y)

    # Draw a line between the first two points
    line = Line(first_point, second_point)
    line.setOutline('orange')
    line.draw(window)

    peak = second_y > first_y

    if peak == False:
        circle = Circle(first_point, 3)
        circle.setFill('red')
        circle.draw(window)
        print(second_point, ' is a peak.')
    if peak == True:
        circle = Circle(first_point, 3)
        circle.setFill('blue')
        circle.draw(window)
        print(second_point, ' is a valley.')

# Update first_y and first_point
    first_y = second_y
    first_point = second_point

    for i in range(2, num_points):  # already did first 2
        # Read the next point and update x
        x += 10
        second_y = int(pointsfile.readline())
        second_point = Point(x, window_height - second_y)

        ##### Copy this code from Part B
     # Draw a line between the first two points
        line = Line(first_point, second_point)
        line.setOutline('orange')
        line.draw(window)

        # Draw a circle centered at the first point
        circle = Circle(first_point, 1)
        circle.draw(window)

        if peak == True:
            if second_y < first_y:
                # Draw the second point
                circle = Circle(first_point, 3)
                circle.setFill('red')
                circle.draw(window)
                print(second_y,' is a peak.')
        elif peak == False:
            if second_y>first_y:
                circle = Circle(first_point, 3)
                circle.setFill('blue')
                circle.draw(window)
                print(second_y, ' is a valley.')
        else:
            # Draw the second point
            circle = Circle(first_point, 1)
            circle.setFill('black')
            circle.draw(window)

        ############
        # Think about why this works!
        peak = second_y > first_y
        ############

        # second_point becomes the first point of the next line
        first_y = second_y
        first_point = second_point



        ###### Complete this code
        # Decide and print whether first_point is a peak or a valley
        # Draw the appropriate circle
    if peak == True:
        # Draw the second point
        circle = Circle(first_point, 3)
        circle.setFill('red')
        circle.draw(window)
    if peak == False:
        # Draw the second point
        circle = Circle(first_point, 3)
        circle.setFill('blue')
        circle.draw(window)




    window.getMouse()
    window.close()

main()