"""
Program: CS 115 Lab 10 part (c)
Author: Gabriel Duarte
Class: CS 115
Description: This program will open a file and then search its contents
             using linear and binary search.
"""

#----------------------------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------

def print_list(list_to_print):
    """
    Print the contents of a list.

    Parameter: the list to print
    Returns: nothing
    """

    for i, item in enumerate(list_to_print):
        print(i, ': ', item, sep="")

#----------------------------------------------------------------------------------------

def linear_search(search_list, value_to_find):
    """
    Uses a hand-coded linear search to find the position of an item in a list

    Parameters: the list; the item to search for
    Returns: the position of the item in the list
        (or None if it is not in the list)
    """
    position = -1
    for i in search_list:
        position += 1
        if i == value_to_find:
            return position

#----------------------------------------------------------------------------------------

def binary_search(search_list, value_to_find):
    """
    Uses a binary search function to find the position of an item in a list
    Parameters: the list; the item to search for
    Returns: the position of the item in the list
             (or None if it is not in the list)
    """

    first = 0
    last = (len(search_list) - 1)
    count = 0

    while (first <= last):

        count += 1
        middle = (first + last) // 2
        mid_item = search_list[middle]

        if (len(search_list)) % 2 == 0:
            middle = ((first + last) // 2)

        if mid_item > value_to_find:
            last = middle -1

        elif (mid_item < value_to_find):
            first = middle + 1

        elif (mid_item == value_to_find):
            print('**Binary search iterations:', count)
            return middle - 1

    if value_to_find not in search_list:
        print('**Binary search iterations:', count)
        print('Binary search: None')
        return None

#----------------------------------------------------------------------------------------

def main():
    """ Read and print a file's contents. """
    intext = input("Please enter a file name:")

    contents = readfile(intext)
    #print('Number of lines in file:', (len(contents)))
    print('The original list of cities is:')
    print_list(contents)
    print('After sorting, the new list is:')
    contents.sort()
    print_list(contents)

    cities = ''
    while cities.lower() != 'quit':
        cities = input('\nEnter the name of a city:')
        if cities.lower() == 'quit':
            exit()
        else:
            linear_position = linear_search(contents, cities)
            print('The position of', cities, 'is:', '\nLinear search:', linear_position)
            binary_position = binary_search(contents, cities)

            if binary_position != None:
                print('Binary search:', binary_position + 1)


main()
