"""
Program: CS 115 Lab 3a
Author: Gabriel Duarte
Description: This program adds up the numbers from 1 to 5.
"""


def main():
    total = 0

    for i in range(1, 6):
        number = int(input("Please enter an integer: "))
        total = total + number
        mean = total / 5

    print('The total is:', total)
    print('The mean is; ', mean)

main()