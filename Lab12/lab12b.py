"""
    Author: Gabriel Duarte
    Assignment: Lab 12 (a)
    Class: CS 115
    Date: 04/18/2017
    Description: This program will eventually read in a list of students and grades from a text
    file, calculate the students' averages, and print the list of students.
"""

class Student:
    """ A class that holds the data for an individual student """
    def __init__(self, name, scores):
        self.set_name(name)
        self.set_scores(scores)
        self.get_average(scores)

    def get_average(self, scores):
        """ Return the average grade """
        self.average = sum(scores) / len(scores)
        return self.average

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
        string_to_print += '\t' + str(self.get_average(self.scores))

        print(string_to_print)


# A tester program
def main():
    # Try to create and print a student with grades of 8, 9, and 10
    test_student = Student('Gabriel', [78, 88, 100])
    test_student.print()


main()
