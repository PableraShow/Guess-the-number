# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

# helper function to start and restart the game
def new_game():
    # initialize global variables secret number
    global secret_number
    # secret_number is a random number from 0 to 100, not included.
    secret_number = random.randrange(0, 100)
    # We return the secret_numbre and close the function
    return secret_number


# define event handlers for control panel
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
    guess =  int(guess)
    # We print a output and we transform the integer number for a new string again to avoid an error
    print 'Guess was ' + str(guess)
    # We compare the secret_number and print out a message
    if secret_number < guess:
        print 'Lower'
    elif secret_number > guess:
        print 'Higher'
    else:
        print 'Correct'
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














"""

project description — “Guess the number” game

One of the simplest two-player games is “Guess the number”.
The first player thinks of a secret number in some known range
while the second player attempts to guess the number.
After each guess, the first player answers either “Higher”, “Lower” or “Correct!”
depending on whether the secret number is higher, lower or equal to the guess.
In this project, you will build a simple interactive program in Python
where the computer will take the role of the first player while you play as the second player.

When discussing ranges in this mini-project, we will follow the standard Python convention
of including the low end of the range and excluding the high end of the range.
Mathematically, we will express ranges via the notation [low, high).
The square bracket of the left of the range indicates that the corresponding bound should be included.
The left parenthesis on the right of the range indicates
that corresponding bound should be excluded.
For example, the range [0, 3) consists of numbers starting at 0 up to, but not including 3.
In other words 0, 1, and 2.

You will interact with your program using an input field and several buttons.
For this project, we will ignore the canvas
and print the computer's responses in the console.
Building an initial version of your project that prints information
in the console is a development strategy that you should use in later projects as well.
Focusing on getting the logic of the program correct before trying to make it display
the information in some “nice” way on the canvas usually saves lots of time
since debugging logic errors in graphical output can be tricky.




As you play “Guess the number”, you might notice that a good strategy
is to maintain an interval that consists of the highest guess that is “Lower” 
than the secret number and the lowest guess that is “Higher” than the secret number.
A good choice for the next guess is the number that is the average of these two numbers.
The answer for this new guess then allows you to figure a new interval that
contains the secret number and that is half as large.
For example, if the secret number is in the range [0, 100),
it is a good idea to guess 50. If the answer is "Higher",
the secret number must be in the range [51, 100).
It is then a good idea to guess 75 and so on. This technique of successively narrowing
the range corresponds to a well-known computer algorithm known as binary search.

Your final addition to “Guess the number” will be to restrict the player
to a limited number of guesses. After each guess, your program should include
in its output the number of remaining guesses. Once the player has used up those guesses,
they lose, the game prints out an appropriate message, and a new game immediately starts.

Since the strategy above for playing “Guess the number” approximately halves the rang
of possible secret numbers after each guess, any secret number in the range [low, high)
can always be found in at most n guesses where n is the smallest integer
such that 2 ** n >= high - low + 1. For the range [0, 100), n is seven.
For the range [0, 1000), n is ten. In our implementation, the function new_game(
set the number of allowed guess to seven when the range is [0, 100)
or to ten when the range is [0, 1000).
For more of a challenge, you may compute n from low and high using
the functions math.log and math.ceil in the math module.

When your program starts, the game should immediately begin in range [0, 100).
When the game ends (because the player either wins or runs out of guesses),
a new game with the same range as the last one should immediately
begin by calling new_game(). Whenever the player clicks one of the range buttons,
the current game should stop and a new game with the selected range should begin.





Grading rubric — 11 pts total (scaled to 100 pts)

Your peers will assess your mini-project according to the rubric given below.
To guide you in determining whether your project satisfies each item in the rubric,
please consult the video that demonstrates our implementation of “Guess the number”.
Small deviations from the textual output of our implementation are fine.
You should avoid potentially confusing deviations (such as printing “Too high” or “Too low”
    instead of “Lower” and “Higher”). Whether moderate deviations
satisfy an item of the grading rubric is at your peers' discretion during their assessment.


Here is a break down of the scoring:

1 pt — The game starts immediately when the “Run” button in CodeSkulptor is pressed.
1 pt — A game is always in progress. Finishing one game immediately starts another in the same range.
1 pt — The game reads guess from the input field and correctly prints it out.
3 pts — The game correctly plays “Guess the number” with the range [0, 100) and prints understandable output messages to the console. Play three complete games: 1 pt for each correct game.
2 pts — The game includes two buttons that allow the user to select the range [0, 100) or the range [0, 1000) for the secret number. These buttons correctly change the range and print an appropriate message. (1 pt per button.)
2 pts — The game restricts the player to a finite number of guesses and correctly terminates the game when these guesses are exhausted. Award 1 pt if the number of remaining guesses is printed, but the game does not terminate correctly.
1 pt — The game varies the number of allowed guesses based on the range of the secret number — seven guesses for range [0, 100), ten guesses for range [0, 1000).

To help aid you in gauging what a full credit project might look like,
the video lecture on the “Guess the number” project includes a demonstration of
our implementation of this project. You do not need to validate that the input
number is in the correct range.
(For this game, that responsibility should fall on the player.)

"""


