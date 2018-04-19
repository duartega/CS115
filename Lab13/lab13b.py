"""
Program: Lab 13 (b)
Author: Gabriel Duarte
Define and test a basic City class.
"""
import sys

def readfile(filename):
    """
    Reads the entire contents of a file into a single string using
    the read() method.

    Parameter: the name of the file to read (as a string)
    Returns: the text in the file as a large, possibly multi-line, string
    """

    infile = open(filename, "r")  # open file for reading

    # Use Python's file read function to read the file contents
    filetext = (infile.read().splitlines())

    infile.close()  # close the file

    return filetext  # the text of the file, as a single string

class City:
    def __init__(self,city_name,population):
        self.set_name(city_name)
        self.set_population(population)

    def set_name(self,name):
        self.name = name

    def set_population(self,population):
        self.population = population

    def __str__(self):
        string_to_print = self.name + ' (pop. ' + str(self.population) + ')'
        return string_to_print

    def __lt__(self, other):
        # Return True if the population of self is less than
        # the population of other and return False otherwise
        if self.population < other.population:
            return True
        else:
            return False

def print_list(list_to_print):
    '''
    Print the contents of a list.

    Parameter: the list to print
    Returns: nothing
    '''

    for i, item in enumerate(list_to_print):
        print(i, ': ', item, sep="")


# ----------------------------------------------------------------------------------------

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

    for i in range(start_index, (len(L))):
        if L[i] < L[count]:
            count = i
    return count


# ----------------------------------------------------------------------------------------

def selection_sort(L):
    '''
    Use the selection sort algorithm to sort a list.
    Parameter: unsorted list
    Sorts the original list that was passed to it -- doesn't return anything.
    '''

    for i in range(len(L) - 1):
        min = find_index_of_min(L, i)

        temp = L[min]
        L[min] = L[i]
        L[i] = temp


# ----------------------------------------------------------------------------------------


def main():

    cities = []
    population = []
    list = []


    file = input("Please enter a file name:")
    data = readfile(file)


    for i in range(0,len(data),2):
            cities.append(data[i])
    for k in range(1,len(data),2):
            population.append(data[k])


    for m in range(len(cities)):
        list.append(City(cities[m], int(population[m])))


    print('\nThe orginal list of cities is:')
    print_list(list)
    selection_sort(list)
    print('\nThe new list of cities is:')
    print_list(list)

# ----------------------------------------------------------------------------------------

main()