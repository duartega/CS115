"""
Program: Lab 13 (a)
Author: Gabriel Duarte
Define and test a basic City class.
"""
import sys


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


def main():
    tokyo = City('Tokyo', 13189000)
    mexico_city = City('Mexico City', 8857188)


    print(tokyo)
    print(mexico_city)


    # Print whichever city is larger
    print('The larger city is:')
    if mexico_city < tokyo:
        print(tokyo)
    else:
        print(mexico_city)


main()