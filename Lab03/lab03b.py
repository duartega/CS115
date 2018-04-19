"""
Program: CS 115 Lab 3b
Author: Gabriel Duarte
Description: Using the graphics package, this program will draw a circle.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    center = Point(100, 200)         # create a point to serve as the center of the circle
    radius = 40
    circle = Circle(center, radius)  # create a circle centered at "center" with radius "radius"
    circle.setOutline('blue')
    circle.draw(window)              # draw the circle in the window that we created earlier

    center = Point(200,400)
    radius = 60
    circle = Circle(center, radius)
    circle.setOutline("red")
    circle.draw(window)

    center = Point(40,10)
    radius = 20
    circle = Circle(center, radius)
    circle.setOutline("yellow")
    circle.draw(window)

    center = Point(500,340)
    radius = 150
    circle = Circle(center, radius)
    circle.setOutline("green")
    circle.draw(window)

    window.getMouse()                # wait for the mouse to be clicked in the window
    window.close()                   # close the window after the mouse is clicked in the window


main()