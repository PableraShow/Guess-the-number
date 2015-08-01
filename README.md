# Guess the number game

The game
-------
![png](images4readme/logo-guess.png)
One of the simplest two-player games is “Guess the number”.
The first player thinks of a secret number in some known range
while the second player attempts to guess the number.
After each guess, the first player answers either “Higher”, “Lower” or “Correct!”
depending on whether the secret number is higher, lower or equal to the guess.

Mini-project development process requirements
-------
In this project, you will read a simple interactive program in Python.
Where the computer will take the role of the first player while you play as the second player.
You will interact with your program using an input field and several buttons.
We will ignore the canvas and print the computer's responses in the console.

As you play “Guess the number”, you might notice that a good strategy is to maintain an interval that consists of the highest guess that is “Lower” than the secret number and the lowest guess that is “Higher” than the secret number.
A good choice for the next guess is the number that is the average of these two numbers.
The answer for this new guess then allows you to figure a new interval that contains the secret number and that is half as large.
For example, if the secret number is in the range [0, 100), it is a good idea to guess 50. If the answer is "Higher", the secret number must be in the range [51, 100).
It is then a good idea to guess 75 and so on. This technique of successively narrowing the range corresponds to a well-known computer algorithm known as binary search.
Your final addition will be to restrict the player to a limited number of guesses.

![jpg](images4readme/logo-python.jpg)

*Stars and Forks are welcome :)*