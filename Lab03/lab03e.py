"""
Program: CS 115 Lab 3 Part E
Author: Gabriel Duarte
Description: Using the graphics package, this program will draw a square of the amount of circles
                the user entered along witht the radii the user entered.
"""
from graphics import *


def main():
    window = GraphWin("Circles", 800, 800)

    # 1. Get the number of circles and the radius from the user.
    num_circles = int(input("Please enter the amount of circles you'd like to draw: "))
    radius = int(input("Please enter the radii for the circles: "))

    # 2. Draw the left vertical circles.
    # Copy and paste what you need from your lab03d.py here.

    x = radius + 5
    y = radius + 5
    diameter = radius * 2
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        y += diameter

    # 3. Draw the top horizontal circles.
    # Copy and paste the previous code-segment that draws vertical circles (step 2 above)
    # and make the necessary changes to it so that it draws the top row of circles.
    # It is okay to draw a circle on the existing top circle.
    # Hint: To draw horizontal circles, think which coordinate (x or y) needs to be changed inside the for-loop

    x = radius + 5
    y = radius + 5
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        x += diameter

    # 4. Draw the bottom horizontal circles.
    # Copy and paste the previous code-segment that draws the top circles (step 3 above)
    # and make the necessary changes to it so that it draws the bottom row of circles.
    # it is okay to draw a circle on the existing bottom circle.

    x = radius + 5
    y = radius + 5 + (num_circles-1) * diameter
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        x += diameter

    # 5. Draw the right vertical circles.
    # Copy and paste the code-segment that draws the (left) vertically stacked circles (step 2 above)
    # and make the necessary changes to it so that it draws the right vertical circles.
    # it is okay to redraw the right-most two horizontal circles.

    x = radius + 5 + (num_circles-1) * diameter
    y = radius + 5
    diameter = radius * 2
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('red')
        circle.draw(window)

        y += diameter

    # 6. Draw the top-left-to-bottom-right diagonal circles.
    # Copy and paste the code-segment that draws the (left) vertical, stacked circles (step 2 above)
    # and make the necessary changes to it so that it draws the circles that are
    # the left-to-right diagonal of the square. The change in successive x and y of these circles
    # is exactly the same as those in the successive horizontal and vertical circles, respectively.
    # Hint: To draw diagonal circles, you would need to change both the x and y-coordinate inside the for-loop

    x = radius + 5
    y = radius + 5
    diameter = radius * 2
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)

        x += diameter
        y += diameter

    # 7. Draw the top-right-to-bottom-left diagonal circles.
    # Copy and paste the code-segment that draws the left-to-right diagonal circles (step 6 above)
    # and make the necessary changes to it so that it draws the circle
    # on the right-to-left diagonal of the square.
    # Hint: To draw these circles, think if the successive x and y-coordinates inside the for-loop need to increase or decrease

    x = radius + 5 + (num_circles-1) * radius * 2
    y = radius + 5
    diameter = radius * 2
    for i in range(num_circles):
        print('x =', x, 'and y =', y)

        center = Point(x, y)
        circle = Circle(center, radius)
        circle.setOutline('blue')
        circle.draw(window)

        x -= diameter
        y += diameter

    window.getMouse()
    window.close()


main()