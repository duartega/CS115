'''
Program: CS 115 Lab 6a
Author: Gabriel Duarte
Description: This program will ask the user for a value
   and tell the user whether the value is even or odd.
'''


def main():

    N = int(input('Enter a number: '))

    while (N != 1):
        if N % 2 == 1:
            M = (3*N)+1
            N = M
            print('The next term is: ',M,'.',sep="")
        else:
            O = N // 2
            N = O
            print('The next term is: ',O,'.',sep="")


main()