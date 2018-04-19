"""
Program: CS 115 Lab 6c
Author: Gabriel Duarte
Description: This program will read a positive integer and
 express it as the sum of powers of 2.
"""

def main():
    # Read user's input and store it in a variable called i_num.
    i_num = int(input('Enter a number: '))

    # Outer loop:
    while i_num > 0:
        # Initialize n and two_to_n.
        n = 0
        two_to_n = 2**n

        while (two_to_n < i_num):
            n += 1
            two_to_n *= 2

        if (two_to_n > i_num):
            n -= 1
            two_to_n /= 2
            print(2, '**', n, ' + ', sep="", end="")
        i_num = i_num - two_to_n

    print(2, '**', n, sep='')

main()