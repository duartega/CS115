"""
Program: CS 115 Lab 2
Author: Your name
Description: This program will compute the area of a square,
    given the side length.
"""

import math

def main():
    # Get the side length
    length = float(input('Enter a numeric value: '))

    # Compute the area of the square
    square_area = length * length
    circle_area = math.pi * (square_area)
    cube_volume = square_area * length
    sphere_volume =  4/3 * math.pi * cube_volume
    eq_tri_area = square_area * math.sqrt(3) / 4

    print("The area of a square with side length ", length,
          " is ", square_area, ".", sep="")
    print("The area of a circle with radius length ", length, " is ", circle_area, ".", sep="")
    print("The volume of a cube with edge length ", length, " is ", cube_volume, ".", sep="")
    print("The volume of a sphere with radius length ", length, " is ", sphere_volume, ".", sep="")
    print("The area of an equilateral triangle with side length ", length, " is ", eq_tri_area, ".", sep="")


main()