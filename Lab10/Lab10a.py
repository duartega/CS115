"""
Program: CS 115 Lab 10 part (a)
Author: Gabriel Duarte
Description: This program will open a file and then search its contents
             using linear and binary search.
"""


def readfile(filename):
    """
    Reads the entire contents of a file into a single string using
    the read() method.

    Parameter: the name of the file to read (as a string)
    Returns: the text in the file as a large, possibly multi-line, string
    """

    infile = open(filename, "r")  # open file for reading

    # Use Python's file read function to read the file contents
    filetext = infile.read().splitlines()

    infile.close()  # close the file

    return filetext  # the text of the file, as a single string

def print_list(list_to_print):
    """
    Print the contents of a list.

    Parameter: the list to print
    Returns: nothing
    """

    for i, item in enumerate(list_to_print):
        print(i, ': ', item, sep="")


def main():
    """ Read and print a file's contents. """
    intext = input("Please enter a file name:")

    contents = readfile(intext)
    print('Number of lines in file:', (len(contents)))
    print_list(contents)

    cities = input('Enter the name of a city:')
    while cities.lower() != 'quit':
        cities = input('Enter the name of a city:')

main()
