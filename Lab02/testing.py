"""
Program: CS 115 Lab 3 Part E
Author: Shawn Fogel
Description: Using the graphics package, this program will draw a blue square of circles with a red
diagonal stripes of circles.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    num_circles = int(input('Enter number of circles: '))
    radius = int(input('Enter the radius of the circles: '))

    # Left vertical circles

    x = radius + 5
    y = radius + 5
    diameter = radius * 2
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        y=y + diameter

    # Top horizontal circles

    x = radius + 5
    y = radius + 5
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        x = x + diameter

    # Bottom horizontal circles

    x = radius + 5
    y = radius + 5 + (num_circles-1) * diameter
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        x = x + diameter

    # Right vertical circles

    x = radius + 5 + (num_circles-1) * diameter
    y = radius + 5
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        y = y + diameter

    # Top-left-to-bottom-right diagonal circles

    x = radius + 5
    y = radius + 5
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)

        y = y + diameter
        x = x + diameter


    #Top-right-to-bottom-left diagonal circles

    x = radius + 5 + (num_circles-1) * radius * 2
    y = radius + 5
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)

        y = y + diameter
        x = x - diameter

    window.getMouse()
    window.close()


main()