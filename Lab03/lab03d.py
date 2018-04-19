"""
Program: CS 115 Lab 3 Part D
Author: Your name
Description: Using the graphics package, this program will draw a number of
             circles using a for-loop.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    x = 100
    y = 100
    num_circles = int(input("Please enter the amount of circles you would like to draw: "))
    radius = int(input("Please enter the radii for the circles: "))
    diameter = radius * 2
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        # Circle 1
        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)
        y += diameter



    window.getMouse()
    window.close()


main()