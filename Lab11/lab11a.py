"""
Program: CS 115 Lab 11 part (a)
Author: Gabriel Duarte
Class: CS 115
Description: We are finding the position of the lowest value with the
             find_index_of_main function
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

def find_index_of_min(L, start_index):
    """
       Parameter: a list L
       Returns: the index of the minimum element of the list
           (returns None if the list is empty)
       """

    # Initialize the variable
    count = start_index
    if (len(L)) == 0 or start_index > (len(L) - 1):
        return None

    for item in L[start_index:]:
        if item < L[count]:
            count += 1
    return count


#----------------------------------------------------------------------------------------

def main():

    # Read and print a file's contents.
    file_name = input("Name of input file:")

    # Calls the read file function.
    file_text = readfile(file_name)

    # Prints the contents of the file
    print_list(file_text)

    # Calls the find_index_of_min function to sort by lowest and swap
    #print(find_index_of_min(file_text,0))


main()