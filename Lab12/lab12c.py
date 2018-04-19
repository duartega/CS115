"""
    Author: Gabriel Duarte
    Assignment: Lab 12 (c)
    Class: CS 115
    Date: 04/18/2017
    Description: This program will read in a list of students and grades from a text
    file, calculate the students' averages, and print the list of students.
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

class Student:
    """ A class that holds the data for an individual student """
    def __init__(self, name, scores):
        self.set_name(name)
        self.set_scores(scores)



    def get_average(self):
        """ Return the average grade """
        average = sum(self.scores) / len(self.scores)
        average = round(average, 5)

        return average

    def set_name(self, name):
        self.name = name

    def set_scores(self, scores):
        self.scores = scores

    def print(self):
        """ Print the student info in the following format:
           Name (12 characters), grades(separated by tabs), average (formatted
           to 5 decimals """

        # Right now, just prints the student name padded out to 12 characters
        string_to_print = self.name.ljust(12)

        # Convert list of integers to strings for printing purposes
        # There are shorter ways to do this, but this is the clearest.
        for score in self.scores:
            string_to_print += '\t' + str(score)

            # Prints the average of the scores
        string_to_print += '\t' + str(self.get_average())


        print(string_to_print)



# A tester program
def main():

    studentlines = readfile("students.txt")
    total = []

    for line in studentlines:
        words = line.split()
        if words == '':
            break
        name = words[0]
        scores = words[1:]
        score = [int(i) for i in scores]

        test_student = Student(name, score)
        test_student.print()

        total.append(test_student.get_average())

    total_avg = sum(total) / len(total)
    print('Overall average:', round(total_avg, 5))


main()
