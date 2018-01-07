# proj03
# CSE 231, section 13

# This program gets a square number from the user, then displays
# the two triangular numbers whose sum is that square number.

import math

# Get the number from the user. Then set a variable equal to the square root of that number.
number = int(raw_input("Give me a number or I'll eat your face. "))
root = math.sqrt(number)

# Check to make sure the number is in fact a square number.  If not,
# the program gets angry and stops running.

# If the number is a square, get the two triangular numbers and present them
# to the eagerly awaiting user.  Basically, "n" is the same thing as the
# square root of the square number.

# The triangular numbers come from plugging "n" and "n-1" into the
# triangular number equations.

# Happy program and happy user. yay!
if number % root != 0:
    print "Eww, what do you think you're doing?  That is NOT a square number."
else:
    triOne = int(((root ** 2) + root) / 2)
    triTwo = int((((root - 1) ** 2) + (root - 1)) / 2)
    print "The two triangular that sum to the square number", number, "are", triOne, "and", triTwo
    print triOne, "+", triTwo, "=", triOne + triTwo
