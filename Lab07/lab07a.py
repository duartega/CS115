"""
Program: CS 115 Lab 7a
Author: Gabriel Duarte
Description: This program finds $1.00 words.
"""


def main():


    # Ask the user for a word, and save the word to a variable.
    word = input('Enter a word: ')
    total = 0
# Convert the user's word to lowercase
    word = word.lower()
# As long as the user's word is not 'quit'...

    while (word != 'quit'):
        word = word.lower()
        for i in word.split():
            for j in i:
                total += ord(j) - 96
            print('Your word is worth: ',"${:.2f}".format(total/100))
        if (total >= 100):
            print('Congratulations!')
        total = 0
        word = input('Enter a word: ')
# Echo their word back to them
# Get a new word from them, convert it to lowercase,
# and save it to the same variable.


main()