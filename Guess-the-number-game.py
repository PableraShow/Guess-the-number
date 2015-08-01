# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# helper function to start and restart the game
def new_game():
    # Initialize the counter to 0 to indicate how many attempts we played
    global count
    count = 0
    # initialize global variables secret number
    global secret_number
    # secret_number is a random number from 0 to 100, not included.
    secret_number = random.randrange(0, 100)
    # We return the secret_numbre and close the function
    return count, secret_number

def range100():
    """button that changes the range to [0,100) and starts a new game"""
    # initialize global variables secret number
    global secret_number
    # secret_number is a random number from 0 to 100, not included.
    secret_number = random.randrange(0, 100)
    print 'The game was restarted with a range between 0 to 100'
    # We return the secret_numbre and close the function
    return secret_number

def range1000():
    """button that changes the range to [0,1000) and starts a new game"""
    # initialize global variables secret number
    global secret_number
    # secret_number is a random number from 0 to 1000, not included.
    secret_number = random.randrange(0, 1000)
    print 'The game was restarted with a range between 0 to 1000'
    # We return the secret_numbre and close the function
    return secret_number
    
def input_guess(guess):
    # We transform the string 'guess' to an integer number
    guess = int(guess)
    # We print a output and we transform the integer number for a new string again to avoid an error
    print 'Guess was ' + str(guess)
    # contamos el numero de veces que hemos preguntado
    # We compare the secret_number and print out a message
    if secret_number < guess:
        print 'Lower'
    elif secret_number > guess:
        print 'Higher'
    else:
        print 'Correct'
    # We increment the count of the games
    global count
    count += 1
    # We print the result of the trials gamed
    print 'you carry ' + str(count) + ' trials played\n'
    # If our count it's the more than or the same to seven
    # print Game Over and Start a new game 
    if count >= 7:
        print 'Game over\nStart a new game\n'
        # start a new game
        new_game()
    # We close the function
    return
    
# create frame
frame = simplegui.create_frame('guess_the_number', 400, 400)

# register event handlers for control elements and start frame
input_guess = frame.add_input('Input guess', input_guess, 50)
restart = frame.add_button('Restart the game', new_game, 120)
range0to100 = frame.add_button('Range between 0 to 100)', range100, 120)
range0to1000 = frame.add_button('Range between 0 to 1000)', range1000, 120)

# call new_game 
new_game()