"""
Program: CS 115 Lab 8c
Author: Gabriel Duarte
Description: This program computes geometric quantities.
"""
import sys
import math


def get_numeric_val():
    """
    Ask the user for a number
    Exit if the user does not supply a positive value.
    Otherwise, return the value they entered
    """

    num = float(input('Enter a positive numeric value: '))
    if num <= 0:
        sys.exit('Error: that number was not positive.')
    return num


def get_menu_choice():
    """ Print the menu and return the user's selection """
    action = input('Would you like to \na. Calculate the area of a square?\nb. Calculate the area of a circle?'
                   '\nc. Calculate the volume of a cube?\nd. Calculate the volume of a sphere?'
                   '\ne. Calculate the area of an equilateral triangle?\nq. Quit?\n')
    todo = action.lower()
    return todo


def compute_square_area(side):
    """
    Compute and return the area of a square.
    Parameter: side length of the square
    """
    return side * side

def compute_circle_area(radius):
    """
    Compute and return the area of a circle.
    Parameter: radius of the circle
    """
    return math.pi * (radius**2)


def compute_cube_volume(edge):
    """
    Compute and return the volume of a cube.
    Parameter: edge length of the cube
    """
    return edge**3

def compute_sphere_volume(radius):
    """
    Compute and return the volume of a sphere
     Parameter: radius length of the sphere
    """
    return (4/3) * math.pi * (radius**3)

def computer_tri_area(side):
    """
    Compute and return the area of an equalateral triangle
    Parameter: side length of the triangle
    """
    return (math.sqrt(3)/4) * (side**2)
def main():

    menu_choice = get_menu_choice()  # Get the user's first choice

    while menu_choice != 'q':
        user_num = get_numeric_val()  # Get the side length (etc.)

        if menu_choice == 'a':
            print('The area of a square with side length ',
                  user_num, ' is ', round(compute_square_area(user_num), 5),
                  '.', sep="")

        elif menu_choice == 'b':
            print('The area of a circle with radius length ',
                  user_num, ' is ', round(compute_circle_area(user_num), 5),
                  '.', sep="")

        elif menu_choice == 'c':
            print('The volume of a cube with edge length ',
                  user_num, ' is ', round(compute_cube_volume(user_num), 5),
                  '.', sep="")
        elif menu_choice == 'd':
            print('The volume of a sphere with radius length ',
                  user_num, ' is ', round(compute_sphere_volume(user_num), 5),
                  '.', sep="")
        elif menu_choice == 'e':
            print('The area of a equalateral triangle with side length ',
                  user_num, ' is ', round(computer_tri_area(user_num), 5),
                  '.', sep="")

        menu_choice = get_menu_choice()  # Get user's next choice


main()