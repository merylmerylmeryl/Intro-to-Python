# proj04
# CSE 231, section 3

import random

chances = 6
wrongLetterList = ""
rightLetterList = ""
spaces = ""
keepGoing = True
stillGoing = True

# Generates a list of letters. The frequency of each letter in the list depends on its frequency
# in the English language.
letterFreqs = []

for x in range(0, 7):
    letterFreqs.append('e')
for x in range(0, 6):
    letterFreqs.append('i')
    letterFreqs.append('t')
for x in range(0, 5):
    letterFreqs.append('s')
    letterFreqs.append('a')
    letterFreqs.append('n')
for x in range(0, 4):
    letterFreqs.append('h')
    letterFreqs.append('u')
    letterFreqs.append('r')
    letterFreqs.append('d')
    letterFreqs.append('m')
for x in range(0,3):
    letterFreqs.append('w')
    letterFreqs.append('g')
    letterFreqs.append('v')
    letterFreqs.append('l')
    letterFreqs.append('f')
    letterFreqs.append('b')
    letterFreqs.append('k')
for x in range(0,2):
    letterFreqs.append('o')
    letterFreqs.append('p')
    letterFreqs.append('j')
    letterFreqs.append('x')
    letterFreqs.append('c')
    letterFreqs.append('z')
letterFreqs.append('y')
letterFreqs.append('q')


print "You like hangman, right?  Well, regardless, you're going to play it"
print "because I had to make it, and you're going to like it. Plus it's a"
print "life-or-death situation, and who doesn't like those?"
print ""
print "You get six chances, so don't screw up."
print "Have someone enter in the phrase to be guessed, and you"
print "have to guess what it is, one letter at a time. Each time you guess a letter"
print "that isn't in the word, you lose one more chance to live."
print ""

# Gets a word or phrase from the player
theWord = raw_input("What's the word you want to guess? ")

# Have a loop going until the player runs out of chances.
# When the counter drops to 0, the player gets a game over. Oh noes!

while keepGoing:

# Look at each character in theWord. Depending on what it is, either copy that character into
# a blank string, or put a "_" where the letter would go.
    while stillGoing:
        spaces = ""
        for char in theWord:
            if char == "-":
                spaces = spaces + "-"
            elif char == " ":
                spaces += " "
            elif char == "'":
                spaces += "'"
            elif char in rightLetterList:
                spaces += char
            else:
                spaces += "_ "
        print "So far: ", spaces
        print ""

        solveYN = raw_input("Would you like to solve the puzzle? ")
        if solveYN == "y" or solveYN == "Y":
            solvePuzzle = raw_input("Solve it then! >>> ")
            if solvePuzzle.lower() == theWord.lower():
                print "You win!"
                playAgain = raw_input("Play again? ")
                if playAgain.lower() == "n":
                    stillGoing = False

        print "Chances left: ", chances
        print ""

        if spaces.find("_") == -1:
            print "YOU WIN!"
            stillGoing = False


        letterGuess = random.choice(letterFreqs)
        while letterGuess in rightLetterList or letterGuess in wrongLetterList:
            letterGuess = random.choice(letterFreqs)
        print letterGuess
        
        if theWord.find(letterGuess) == -1 and theWord.find(letterGuess.upper()) == -1 and theWord.find(letterGuess.lower()) == -1:
            chances -= 1
            wrongLetterList = wrongLetterList + " " + letterGuess
            print "HAH! That letter isn't in the word, and you lose one chance."
            print "chances: ", chances
            print "wrong letters used: ", wrongLetterList
        elif theWord.find(letterGuess.upper()) != -1:
            rightLetterList += letterGuess.upper()
            rightLetterList += letterGuess
        elif theWord.find(letterGuess.lower()) != -1:
            rightLetterList += letterGuess.lower()
            rightLetterList += letterGuess
        else:
            rightLetterList += letterGuess
            print "You're right, woo..."
            print "chances: ", chances
            print "wrong letters used: ", wrongLetterList
    if chances == 0:
        print "GAME OVER!"
        stillGoing = False


    gameAgain = raw_input("Do you want to play again? ")
    
    if gameAgain == "n" or gameAgain == "N" or gameAgain == "no" or gameAgain == "NO":
        keepGoing = False
    else:
        chances = 6
        wrongLetterList = ""
        rightLetterList = ""
        spaces = ""
        theWord = raw_input("What's the word you want to guess? ")
