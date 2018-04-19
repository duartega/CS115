"""

Project 1: This program prompts asks for a place, wind velocity, and air temperature.
        It then takes that data and gets averages for each and tells you the place.
        It also gets the highest and lowest for specific variables.

Author: Gabriel Duarte

Class: cs115

Extra Credit : I have modified the swap loops to work if there was only 1 entry
                and so that it can be used with positive temps or even 0 temp on single entry.
                I also added to check if wind velocity was negative and if it was faster than
                the speed of sound. I added a check to see if there was extreme temperatures
                entered.
"""
import math

#Left off fixing the swap loops because it will record wrong when greater than
def main():

    print('==> Windchill Temperature (WCT) Weather Report Calculator <==') #Print the startup message

    # Initialize the variables for totals
    totalWCT = 0
    totalAirTemp = 0
    totalWindVelocity = 0

    # Initialize the variables for lowest and highest counts
    lowestWCT = float('inf')
    lowestAirTemp = float('inf')
    highestWindVelocity = float('-inf')

    # Initialize the variables fpr lowest and highest places
    lowestWCTplace = ''
    lowestAirTempPlace = ''
    highestWindVelocityPlace = ''

    # Initialize the variables for the temporary swap variables
    tempWCT = float('inf')
    tempAirTemp = float('inf')
    tempWindVelocity = float('-inf')

    # The first statement that asks the user to enter a number of locations
    num_locations = int(input('Select the number of locations for the report: '))

    # Show a message if the input is not valid, then exit the program
    if num_locations == 0:
        print('Error: 0 is not a valid input.')
        exit(255)
    elif num_locations < 0:
        print('Error: ',num_locations, ' is not a valid input.')
        exit(255)
    # Asks the user to enter the amount of decimal places wanted after the decimal up to 4
    decimals = int(input('Select decimal precision for the report [1--4]: '))
    # Show a message if the input is not valid, then exit the program
    if decimals > 4 or decimals < 1:
        print('Error: ',decimals, ' is not in the range 1--4.')
        exit(255)
    elif decimals > 0 and decimals < 5:

        # Start the loop of asking the Location, Wind Speed, and Air Temperature
        for i in range(num_locations):
            # Prints the question and the number of interation it is
            print('Enter name of ** Location',i+1,'**: ',end="")
            # Reads the input from the user into the variable "Place"
            place = input()
            # Gets the input from the user about temperature
            air_temperature =  int(input('\tEnter air temperature [in deg F]: '))

            # Checks to see if the temperature entered is extreme
            # Also checks to see if you are God
            # http://coolcosmos.ipac.caltech.edu/ask/63-What-are-the-highest-and-lowest-temperatures-on-Earth-
            # https://www.theweathernetwork.com/news/articles/last-week-was-nothing-compared-to-these-seven-record-cold-temperatures-recorded-on-earth/19302
            if air_temperature > 136 or air_temperature < -202:
                print('Well, you must be God if you are able to survive such a temperature. Nice try!')
                exit(255)
            if air_temperature > 40 or air_temperature < -45:
                print('\tYou are going out of then WindChill Temperature chart.')
            # Gets the input from the user about wind velocity
            wind_velocity = int(input('\tEnter wind velocity [in mph]: '))

            # Checks to see if the wind velocity entered is negative
            if wind_velocity < 0:
                print('Nice try! Even during time travel wind velocity is positive, just going the other way!')
                exit(255)
            if wind_velocity > 767:
                print('You must be superman if you are able to survive such winds! Nice try stud..')
                exit(255)
            elif wind_velocity >= 0:

                # Calculates the WindChill Temperature
                WCT = (35.74 + 0.6215*(int(air_temperature))) - (35.75*((math.pow(wind_velocity,0.16)))) + (0.4275*(air_temperature*((pow(wind_velocity,0.16)))))
            # Shows the WCT for the area and variables specified
            print('\tWCT is ', round(WCT,decimals),'deg F.')

            # Adds to the totals for averages later on in the code
            totalWCT += WCT
            totalAirTemp += air_temperature
            totalWindVelocity += wind_velocity

            # Swap loop for the lowest WCT
            if WCT > tempWCT:
                tempWCT = WCT
            if WCT < tempWCT:
                tempWCT = WCT
            if tempWCT < lowestWCT:
                lowestWCT = tempWCT
                lowestWCTplace = place
            elif num_locations == 1 and WCT > lowestWCT:
                lowestWCT = WCT
                lowestWCTplace = place
            elif lowestWCT == 0:
                lowestWCT = WCT
                lowestWCTplace = place

            # Swap loop for the lowest air temperature
            if air_temperature > tempAirTemp:
                tempAirTemp = air_temperature
            if air_temperature < tempAirTemp: # or air_temperature > tempAirTemp:
                tempAirTemp = air_temperature
            if tempAirTemp < lowestAirTemp:
                lowestAirTemp = tempAirTemp
                lowestAirTempPlace = place
            elif num_locations == 1:
                lowestAirTemp = air_temperature
                lowestAirTempPlace = place


            # Swap loop for the highest wind velocity
            if wind_velocity > tempWindVelocity:
                tempWindVelocity = wind_velocity
                highestWindVelocityPlace = place
            if tempWindVelocity > highestWindVelocity:
                highestWindVelocity = tempWindVelocity
            elif num_locations == 1 and wind_velocity >= highestWindVelocity:
                highestWindVelocity = wind_velocity
                highestWindVelocityPlace = place

        # Gets the averages of the WCT, AirTemp, and WindVelocity
        averageWCT = totalWCT / num_locations
        averageAirTemp = totalAirTemp / num_locations
        averageWindVelocity = totalWindVelocity / num_locations

        # Prints out all the totals, averages, and places
        print('\n*** Summary ***\nWCT\n\tAvg recorded WCT: ', round(averageWCT,decimals),'deg F')
        print('\tLocation with lowest WCT: ', lowestWCTplace,' (',round(lowestWCT,decimals),' F)',sep="")
        print('Air Temperature\n\tAvg recorded air temperature: ',round(averageAirTemp,decimals),'deg F')
        print('\tLocation with lowest air temperature: ',lowestAirTempPlace,' (',float(round(lowestAirTemp,decimals)),' F)',sep="")
        print('Wind Velocities\n\tAvg recorded wind velocity: ',round(averageWindVelocity,decimals),'mph')
        print('\tLocation with highest wind velocity: ', highestWindVelocityPlace,' (',float(round(highestWindVelocity,decimals)),' mph)',sep='')

main()