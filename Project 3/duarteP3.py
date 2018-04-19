'''
Author: Gabriel Duarte
Assignment: Project 3
Class: CS 115
Description: The game will be the same as the game hangman but will be
backwards. The skeleton will slowly disappear every time the guess is wrong.
It will actively keep a counter of how many words match that sequence
as well as tell you the incorrect guesses. It will also tell you
how many guesses you have remaining.
'''


from ghost_support import *
import itertools


def create_win():  # Create the window by size and add the title
    window = GraphWin('Ghost Word Game', WINSIZE, WINSIZE)
    draw_and_undraw_stick(window, 0)
    return window

# -----------------------------------------------------------------------------


def readfile(filename):
    """
    Reads the entire contents of a file into a single string using
    the read() method.

    Parameter: the name of the file to read (as a string)
    Returns: the text in the file as a large, possibly multi-line, string
    """
    infile = open(filename, "r")  # open file for reading
    new_list = []
    # Use Python's file read function to read the file contents
    filetext = infile.read().splitlines()
    # Convert the letters to lower to make sure HuH and huh are one word
    for i in filetext:
        if i.isalpha():
            new_list.append(i.lower())
    infile.close()  # close the file
    return new_list  # the text of the file, as a single string

# -----------------------------------------------------------------------------


def draw_and_undraw_stick(win, guesses):
    '''

    :param win: Takes the parameter win to draw the stick figure to the window
    :return: Returns None

    '''
    # Set the points for the limbs
    left_leg_tr = Point(WINSIZE/2, WINSIZE/1.5)
    left_leg_bl = Point(WINSIZE/5.3, WINSIZE/1.1)
    right_leg_tl = Point(WINSIZE/2, WINSIZE/1.5)
    right_leg_br = Point(WINSIZE/1.3, WINSIZE/1.1)
    right_arm_bl = Point(WINSIZE/2, WINSIZE/2.4)
    right_arm_tr = Point(WINSIZE/1.19, WINSIZE/4)
    left_arm_br = Point(WINSIZE/2, WINSIZE/2.4)
    left_arm_tl = Point(WINSIZE/6.4, WINSIZE/4)
    body_top = Point(WINSIZE/2, WINSIZE/3.7)
    body_bottom = Point(WINSIZE/2, WINSIZE/1.5)
    head = Point(WINSIZE/2, WINSIZE/7)
    radius = WINSIZE / 8

    # Creates the start and end points
    left_leg = Line(left_leg_tr, left_leg_bl)
    right_leg = Line(right_leg_tl, right_leg_br)
    body = Line(body_top, body_bottom)
    right_arm = Line(right_arm_bl, right_arm_tr)
    left_arm = Line(left_arm_br, left_arm_tl)
    h = Circle(head, radius)

    # Set width so the stick is noticeable
    left_leg.setWidth(5)
    right_leg.setWidth(5)
    body.setWidth(5)
    right_arm.setWidth(5)
    left_arm.setWidth(5)
    h.setWidth(5)

    if guesses == 0:
        # Draw the stick to the graphics window
        left_leg.draw(win)
        right_leg.draw(win)
        body.draw(win)
        right_arm.draw(win)
        left_arm.draw(win)
        h.draw(win)
        win.setBackground('white')
    # Each guess removes a body part
    if guesses == 1:
        left_leg.setFill('white')
        left_leg.setOutline('white')
        left_leg.draw(win)
    if guesses == 2:
        right_leg.setFill('white')
        right_leg.setOutline('white')
        right_leg.draw(win)
    if guesses == 3:
        left_arm.setFill('white')
        left_arm.setOutline('white')
        left_arm.draw(win)
    if guesses == 4:
        right_arm.setFill('white')
        right_arm.setOutline('white')
        right_arm.draw(win)
    if guesses == 5:
        body.setFill('white')
        body.setOutline('white')
        body.draw(win)
    if guesses == 6:
        h = Circle(head, radius)
        h.setWidth(8)
        h.setFill('white')
        h.setOutline('white')
        h.draw(win)


# -----------------------------------------------------------------------------


def remove_duplicates(lists):
    # Removes the duplicate items in the lists passed to it
    return list(set(lists))


# -----------------------------------------------------------------------------


def frequency_of_letter(list):
    '''
    Parameter: List
    Description: Gets the list of words and makes sure that there
                 is more than one word and also tallies the totals
                 of each letter
    '''
    char_in_list = []  # Create the empty list for words to be entered

    for i in list:  # If there are words, then read in each word
        for char in i:
            char_in_list.append(char)  # Add the words to the list
    # Checks each letter in the string
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        # Gets the character counts and prints
        print(letter, ': ', char_in_list.count(letter.lower()), sep='')

# -----------------------------------------------------------------------------


def similarity(guess, letter_pos, sw, dictionary, secret_word_list,
               wrong_letters, correct_letters):
    '''
    :param guess: Gets the entered letter
    :param letter_pos: Gets the position of that letter in the word
    :param sw is the secret word
    :param dictionary: Gets the whole dictionary so we can compare words
    :param secret_word_list: This is the list that is passed back and forth
    to get an updated list of the words with specific characters
    :return: list_of_matched_words returns the first set of words. For ex,
    if the word is BUFF, and 'B' was entered, it will return 'BUFF, BUZZ'
    etc and secret_word_list will gain of those words
    '''
    # Create an empty list store the first set of words
    # to the first matched character
    list_of_matched_words = []
    # Creates a variable that allows us to start with the original dictionary
    # Then afterwards it starts using the dictionary with the possible words
    x = 0
    if len(secret_word_list) == 0:
        x = dictionary
    elif len(secret_word_list) > 0:
        # Merges multiple lists into one
        x = list(itertools.chain(*secret_word_list))
    while len(secret_word_list) > -1:
        for word in x:  # Gets each word
            position_in_word = -1  # To get position in word
            # To count the amount of correct letters
            counter = len(correct_letters) - 1
            if len(sw) == len(word):  # Makes sure the lengths match
                for char in word:
                    if wrong_letters == []:  # If there are no wrong letters
                        position_in_word += 1
                        if char.upper() == guess:  # Matched letter check
                            # Are the letters of the word in the same position
                            if position_in_word == letter_pos:
                                counter += 1
                                if len(correct_letters) == counter:
                                    list_of_matched_words.append(word.upper())
                    # Checks when there are wrong letters
                    if wrong_letters != []:
                        position_in_word += 1
                        # If any of the wrong letters are in the words,
                        # remove the word and go to the next word
                        if any(i in word.upper() for i in wrong_letters):
                            # Exits the loop to go to the next word
                            continue
                        else:
                            counter = len(correct_letters) - 1
                            if char.upper() == guess:
                                if position_in_word == letter_pos:
                                    counter += 1
                                    if len(correct_letters) == counter:
                                        list_of_matched_words.\
                                            append(word.upper())
        return list_of_matched_words
# -----------------------------------------------------------------------------


def matching_words(word, list):
    """
    Parameters: Word(gets the secret word), List(gets the list of words)
    Description: Gets the length of the secret word and checks for the
                 amount of words that match that length before starting
                 the guessing
    """
    count = 0
    new = []
    for i in list:
        if len(word) == len(i):
            count += 1
            new.append(i)
    print("Possible words matching the pattern:", count)
    return new


# -----------------------------------------------------------------------------

def guess_word(secret_word, win, list):
    """
    :param secret_word: Passes the random word
    :param win: Passes the windows so we can remove body parts
    :param list: The initial list of words is passed
    :return: None
    """
    secret_word = secret_word.upper()  # Changes all input to uppercase
    word = []                          # Creates a list for the underscores
    revealed_word = []                 # List for the incorrect characters
    new_list = []           # List for possible words with correct characters
    # Variable to track if the same ammount of chars == len(secret_word)
    guess_count = 0
    too_many_guesses = 0    # Variable to keep track of incorrect guesses
    # List for invalid characters
    invalid_chars = '~!@#$%^&*()_+`[]\;,./{}|:<>?"' + "' "
    correct_letters = []

    # Knows the amount of underscores to draw for each letter in word
    for char in secret_word:
        word += '_'

    # Makes sure that the secret random word is greater than the length of 1
    while len(secret_word) > 1:
        # Also checks if you guessed too many times
        # So there are equal wrong guesses to the
        # amount of body parts the stick is composed of (6)
        while too_many_guesses < 6:
            count = 0
            print('\tHint: ', end='')

            # Prints the under scores and adds spaces between them
            for j in word:
                print(j, ' ', end='')
            # Prints the list of letters that are not in the word
            print('\n\tNot in the word:', revealed_word)
            # Not mentioned in the instructions but un the grading rubric
            print("\tYou have", (6 - too_many_guesses), 'guesses left!')

            # Asks for the guess then changes it to uppercase
            # to compare it to the uppercase secret word
            guess = input("\nGuess: ")
            guess = guess.upper()

            # Makes sure that the user only enters one character
            while len(guess) > 1:
                print("Enter one letter!")
                guess = input('Guess: ')
                guess = guess.upper()

            # Checks to see if the guess is in the
            # list of characters that are wrong
            if guess in revealed_word:
                print('You have already guessed that! Try again')
                # Makes sure the guess is not counted if
                # you already have that guess in the list
                too_many_guesses -= 1

            # If the guess is not in the secret word and your
            # guess in not numeric then add a guess
            # Then makes a call to the remove body part function
            if guess not in secret_word and not guess.isnumeric()\
                    and guess not in invalid_chars:
                too_many_guesses += 1
                print("Sorry,", guess, "is not in the secret word.\n")
                draw_and_undraw_stick(win, too_many_guesses)

                # If the users guess is not in the "Incorrect" list then add it
                if guess not in revealed_word and guess not in invalid_chars:
                    revealed_word.append(guess)

            for special_char in invalid_chars:
                if guess == special_char:
                    print("Sorry,", guess, "is not in the secret word.\n")
                    print("Please enter a valid character!")

            # Reminds the user to enter a letter and not a number
            if guess.isnumeric():
                print("Please enter a letter!")
            for j in word:
                if guess == j:
                    print("You have already got that correct!",
                          "Please enter another letter.")
                    guess_count -= 1

            # Checks to see each entered letter is in the word.
            # If it is, then it adds to the counter.
            for i in secret_word:
                if guess == i:  # Makes sure the letters match
                    word[count] = guess  # Adds the letter to the HINT
                    correct_letters.append(i)
                    guess_count += 1  # Adds to the counter of correct letters
                    # Calls the simliar word function to get the
                    # similar words with that letter positon
                    x = similarity(guess, count,
                                   secret_word, list, new_list,
                                   revealed_word, correct_letters)
                    new_list = []
                    # Adds to the list to send back the words to similarity
                    new_list.append(x)
                    # Won't print it when you solve the word
                    if guess_count != len(secret_word):
                        # Calls function to get the number of possible words
                        matching_words(secret_word, x)
                count += 1  # Increments counter for HINT _ _ _ _
            revealed_word.sort()        # Sort the list of incorrect guesses

            # Checks to see if the word matches essentially, but
            # I couldn't use the guessed word because there were
            # spaces in it, and did not want to take out all spaces.
            if guess_count == len(secret_word):
                print('You got it! The word was:', secret_word)
                return
        # Return to main to ask if you want to play another game
        return print("You had too many guesses! The word was:", secret_word)
# -----------------------------------------------------------------------------


def main():
    # Asks the user for the dictionary
    file_name = input("Enter a dictionary filename:")
    file_text = readfile(file_name)  # Reads the file by calling the function
    list_of_words = remove_duplicates(file_text)  # Removes the duplicate words
    if len(list_of_words) == 0:  # Makes sure the dictionary is not blank
        print("Sorry, there are no usable words!")
        exit(1)
    print("\nNeato dictionary pal. Here is some info about it.\n",
          ' Size of dictionary:', len(list_of_words))
    print(' Frequency of each letter:')
    # Calls the function to get character counts
    frequency_of_letter(list_of_words)

    game = input("Would you like to play a nice game of Ghost Word?")
    if game.upper() == "N" or game.upper() == "NO":
        print("Have a super day my friend!")
        exit(1)
    # Checks to see if they say anything other than yes or no
    while game.upper() != "YES" and game.upper() != "Y":
        game = input("Would you like to play a nice game of Ghost Word?")
        # Checks to see if they say no
        if game.upper() == 'N' or game.upper() == 'NO':
            print("Have a super day my friend!")  # Print a nice message
            exit(1)                               # Exit if they say no
        # Checks to see if they say yes

    win = create_win()  # Create the board
    # Calls the rand word function in ghost_support
    rand_word = choose_word(list_of_words)
    print(rand_word)
    # Gets the amount of words with same length
    m = matching_words(rand_word, list_of_words)
    # Calls the guess word function
    guess_word(rand_word, win, m)

    # Asks if they want to play again
    game = input("Would you like to play again?")
    win.close()  # Close window if they say yes or no
    if game.lower() == 'y' or game.lower() == 'yes':
        main()  # Recalls main to start the program over
    else:                                               # Else no
        print("Have a super day my friend!")            # Print a nice message
        exit(1)                                         # Exit the game

main()
