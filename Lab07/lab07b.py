"""
Program: CS 115 Lab 7b
Author: Gabriel Duarte
Description: Computes the average word length of the user's text.
"""


def main():
    line_of_text = input('Enter some text: ')
    line_length = line_of_text.split()

    print('This line has:', len(line_length), 'words.')

    print(len(line_of_text),sep='')

main()