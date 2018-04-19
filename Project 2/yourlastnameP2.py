"""
Program: Project 2
Author: Gabriel Duarte
Description: This program wil shuffle a deck if cards (icons) and you have to match each card. If you pick two
             cards that do not match, then you hide them both. If you try clicking on a card that was already
             matched as a pair, then the program simply ignores it. If you click the same card, it should not
             mark itself as a pair. Once you have 24 cards that match, then you win the game and a random
             color screen flashes as the as the border around the cards and should not let you select anything
             else.
"""

from match_graphics import *
from random import seed, shuffle
from graphics import *

def shuffle_cards():

    # Generates a shuffled deck of cards. When done, cards[i][j] is the name of the card in
    # row i and column j. It is a 5x5 grid comprised of 12 card pairs and one extra card.

    # seed the random number generator
    seed()

    # The idea of how to shuffle is the following:
    # shuffle the images
    # pick out 12 of the images (these are the ones that will be pairs)
    # pick out the remaining image (this is the one that will have no pair)
    # gather together 2 of each pair and the extra into a list
    # shuffle that list

    # Use the list of these 25 shuffled cards to build a 5x5 array of cards
    # Creates a list
    cards = []
    # Shuffles the list
    shuffle(images)
    # Creates a list of 25 images by taking 12 and then copying them for pairs and adds one extra
    s1 = (images[:-1]*2) + images[-1:]
    # Shuffles the list now instead of images
    shuffle(s1)
    # Create a variable to go through the list of 25
    count = 0
    for i in range(5):
        row = []
        for j in range(5):
            item = s1[count]
            count += 1
            row.append(item)
        cards.append(row)
    return cards


def show_card(win, cards, i, j):

    # Shows the card at row i and column j in the 5x5 grid in the window.
    # Draw a rectangle with a yellow border of line width 5
    # at the location associated with card (i,j)
    # Ex: card (0,0) has upper-right corner (XMARGIN, YMARGIN) and
    # lower-right corner (XMARGIN+CARD_HEIGHT, YMARGIN+CARD_WIDTH)

    # Calculates the x and y values
    y = YMARGIN + (CARD_HEIGHT*i)
    x = XMARGIN + (CARD_WIDTH * j)

    top_left_point = Point(x, y)
    bottom_right_point = Point(x + CARD_WIDTH, y + CARD_HEIGHT)
    enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
    enclosing_rectangle.setWidth(3)
    enclosing_rectangle.setOutline("yellow")

    # Then, place the image for cards[i][j] at the center of the rectangle.
    card = Image(Point(x + 62.5, y + 62.5), cards[i][j])
    card.draw(win)
    enclosing_rectangle.draw(win)

    return


def hide_card(win, cards, i, j):

    # Takes the window and cards and hides the card at row i and column j.
    # Calculates the x and y values
    y = YMARGIN + (CARD_HEIGHT * i)
    x = XMARGIN + (CARD_WIDTH * j)

    top_left_point = Point(x, y)
    bottom_right_point = Point(x + CARD_WIDTH, y + CARD_HEIGHT)
    enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
    enclosing_rectangle.setWidth(5)
    enclosing_rectangle.setOutline("yellow")
    enclosing_rectangle.setFill("lightgreen")
    enclosing_rectangle.draw(win)


    return


def mark_card(win, cards, i, j):

    # Takes the window and cards and marks the card at row i and column j with a red X.
    # Calculates the x and y values
    y = YMARGIN + (CARD_HEIGHT * i)
    x = XMARGIN + (CARD_WIDTH * j)

    # Creates the points for each rectangle
    top_left_point = Point(x, y)
    bottom_right_point = Point(x + CARD_WIDTH, y + CARD_HEIGHT)
    top_right_point = Point(x + CARD_WIDTH,y)
    bottom_left_point = Point(x, y + CARD_HEIGHT)

    # Makes red X's across the card
    line = Line(top_left_point, bottom_right_point)
    line1 = Line(top_right_point,bottom_left_point)
    line1.setWidth(5)
    line.setWidth(5)
    line1.setOutline('red')
    line.setOutline('red')
    line.draw(win)
    line1.draw(win)
    return


def get_col(x):

    # Takes the x-coordinate and returns the column.
    # If the x coordinate is outside the board, returns -1.
    column = int((x - XMARGIN) // CARD_WIDTH) + 1
    return column


def get_row(y):

    # Takes the y-coordinate and returns the row.
    # If it it outside the board, returns -1.
    row = int((y - YMARGIN) // CARD_HEIGHT) + 1
    return row


def main():
    '''
    TODO: describe how your main function works.
    '''

    # generate game window
    win = create_board()

    # shuffle the cards
    cards = shuffle_cards()

    # For Checkpoint A:
    # place all the cards, face-up
    for i in range(5):
        for j in range(5):
            hide_card(win, cards, i, j)


    # For Checkpoint B:
    # forever:
    click = 0
    first_pick = 0
    second_pick = 0
    o = 0
    p = 0
    matched_pairs = []
    try:
        while True:
            # get a mouse click
            c = win.getMouse()
            # Get the coordinates
            x = c.getX()
            y = c.getY()
            # Get the column and row
            i = get_col(x)
            j = get_row(y)
            # Gets the image locations which would be the same as the col and row -1
            m = (i - 1)
            n = (j - 1)
            # For each m in n is what im setting up here. Later on in the code,
            # I will use it as followed: (n,m) to get the card location
            k = cards[n]

            # Checks to see if the click is out of the grid
            if i > 5 or i < 1:
                print('Error: out of bounds. -1')
            elif j > 5 or j < 1:
                print("Error: out of bounds. -1")
            else:
                # Figure out which card was clicked
                # If this is a 'first pick', show the card
                # Using a variable as you described in the instructions as "n" and "n+1"
                click +=1
                # Checks to see if this is the first click
                if click == 1:
                    # Checks to see if the card was already in the matched pairs
                    # If it is, then discard the pick
                    if (n,m) in matched_pairs[:]:
                        click = 0
                        first_pick = 0
                        second_pick = 0

                    else:
                        # If the card is not already a pair, show the card and make it your first pick
                        show_card(win, cards, n, m)
                        first_pick = k[m]
                        # Here I had to use (o,p) to use it to hide the first card
                        o = n
                        p = m

                 # else, if this is a 'second pick':
                 # show the card

                # Checks to see if this is the second click
                if click == 2:
                    # Checks to see if the card was already in the matched pairs
                    # If it is, then discard the second pick
                    if (n,m) in matched_pairs[:]:
                        click = 1
                    else:
                        # If the card is not already a pair, show the card and make it your second pick
                        show_card(win, cards, n, m)
                        second_pick = k[m]

                    # If the first pick is not equal to the second pick then hide them
                    # The zero is there to make sure that when a non-pair card is click first
                    # and then a second paired card is clicked, they dont disappear
                    if first_pick != second_pick and second_pick != 0:
                        # Checks to see if the card was already in the matched pairs
                        # If it is, then discard the pick(s)
                        if (m,n) in matched_pairs[:]:
                            click = 2
                            # wait 1 second
                            game_delay(1)
                            hide_card(win, cards, o, p)
                            hide_card(win, cards, n, m)

                        else:
                            # wait 1 second
                            game_delay(1)
                            hide_card(win, cards, o, p)
                            hide_card(win, cards, n, m)

                    # This checks to see if the first card is the same location as the second
                    # so that it does not mark itself as a pair
                    # resets the second pick and set the variable click back to one
                    # so that the user can pick another card
                    if (o, p) == (n, m):
                        click = 1
                        second_pick = 0

                # Checks to see if the first card is the same as the second card
                # If it is, then mark the card and reset the variables
                # The zero makes sure that if a already paired card was clicked,
                # the previous card will not be marked
                if first_pick == second_pick and first_pick !=0:
                    # wait 1 second
                    game_delay(1)
                    mark_card(win, cards, o, p)
                    mark_card(win, cards, n, m)

                    if (n,m) in matched_pairs:
                        click = 0
                        first_pick = 0
                        second_pick = 0

                    else: # Otherwise append the picks to the list "matched_pairs"
                        matched_pairs.append((o,p))
                        matched_pairs.append((n,m))

                # If there are two picks then reset the picks
                if click == 2:
                    click = 0
                    first_pick = 0
                    second_pick = 0



                # if we just won:
                # call the you_won function.
                if (len(matched_pairs) == 24):
                    you_won(win, delay=0.2)
    except:
        print("The program has been terminated.")

"""
I need to get the grid correct so that there is no extras showing
up at the top or the bottom of the grid on the outside

"""


    #win.getMouse()

main()

#11 mkdir 200{1..3}-{Jan,Feb,Mar}