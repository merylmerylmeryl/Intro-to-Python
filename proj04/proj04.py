# proj04
# CSE 231, section 3

import random

keepGoing = True
totallyGoing = True

# creates a list of letters based on the frequency
# of the letters' appearances in the English language
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
print "have to guess one letter at a time what it is, or you can guess the whole word. Each time you guess a letter"
print "that isn't in the word, you lose one more chance to live."
print ""

# asks which version of the game the user wants to play
while totallyGoing:
    choose = raw_input("Would you like to guess the letters or would you like the computer to guess the letters for you? (type either \"me\" or \"computer\") ")

# if the user says "me", then initiate that version of the game
    if choose == "me":
        theWord = raw_input("What's the word you want to guess? ")
        chances = 6
        wrongLetterList = ""
        rightLetterList = ""
        spaces = ""

    # Look at each character in theWord. Depending on what it is, either copy that character into
    # a blank string, or put a "_" where the letter would go.
        while chances > 0:
            spaces = ""
            for char in theWord:
                if char.isdigit() == False and char.isalpha() == False:
                    spaces += char
                elif char in rightLetterList:
                    spaces += char
                else:
                    spaces += "_ "
            print spaces
            print ""
            print "Chances left: ", chances
            print ""

            if spaces.find("_") == -1:
                print "YOU WIN!!!!!!!!!!!"
                print ""
                gameAgain = raw_input("Do you want to play again? Y/N? ")
                if gameAgain.lower() == "n":
                    totallyGoing = False
                    break
                else:
                    break

            # asks the user to guess a letter.  Adds the letter to the rightLetterList
            # if the letter is right and the wrongLetterList if the letter is wrong.
            # if the user types in a letter they've already guessed or tries typing
            # in something that isn't even a letter, ask again.
            letterGuess = raw_input("Guess a letter: ")

            while letterGuess in rightLetterList or letterGuess in wrongLetterList:
                print "You've already guessed that letter. Please guess again."
                print ""
                letterGuess = raw_input("Guess a letter: ")
            while letterGuess.isalpha() == False:
                print "That isn't a letter. Try again, stupid."
                letterGuess = raw_input("Guess a letter: ")
                
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
        if chances <= 0:
            print "GAME OVER!"

            gameAgain = raw_input("Do you want to play again? Y/N? ")
            if gameAgain.lower() == "n":
                totallyGoing = False
                break

    # if the user wants the computer to choose the letters...
    elif choose == "computer":
        
        theWord = raw_input("What's the word you want to guess? ")
        chances = 6
        wrongLetterList = ""
        rightLetterList = ""
        spaces = ""
        print ""

        # the computer keeps "guessing" letters until it runs out of chances, or until the user decides to guess the word/phrase
        while chances > 0:
            spaces = ""

            # randomly pick a letter from the letterFreqs list. if the letter has already been chosen - that is, if it's already present in the rightLetterList or the wrongLetterList, then randomly pick a letter again.
            letterGuess = random.choice(letterFreqs)

            while letterGuess in rightLetterList or letterGuess in wrongLetterList:
                letterGuess = random.choice(letterFreqs)

            print "The computer guessed: ", letterGuess

            # if the computer guesses incorrectly, subtract 1 from remaining chances
            if theWord.find(letterGuess.upper()) == -1 and theWord.find(letterGuess.lower()) == -1:
                chances -= 1
                if chances == 0:
                    print "You ran out of chances!  Hooray for me!  GAME OVER!"
                    gameAgain = raw_input("Do you want to play again? Y/N? ")
                    if gameAgain.lower() == "n":
                        totallyGoing = False
                        break
                    break

                wrongLetterList = wrongLetterList + " " + letterGuess

                print ""
                print "HAH! That letter isn't in the word, and you lose one chance."
                print "chances: ", chances
                print "wrong letters used: ", wrongLetterList

            # if the computer guesses correctly, add it to the list of right letters
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

            # generate spaces, a variable containing the partially guessed phrase, all the letter placeholders "_", and so on
            for char in theWord:
                if char.isdigit() == False and char.isalpha() == False:
                    spaces += char
                elif char in rightLetterList:
                    spaces += char
                else:
                    spaces += "_ "
            print spaces
            print ""
            print "Chances left: ", chances
            print ""

            # if the computer gets all the letters right, the user wins and is asked whether they would like to play again
            if spaces.find("_") == -1:
                print "YOU WIN!!!!!!!!!!!"
                print ""
                gameAgain = raw_input("Do you want to play again? Y/N? ")
                if gameAgain.lower() == "n":
                    totallyGoing = False
                    break
                break

            solveYN = raw_input("Would you like to solve the puzzle? Y/N? ")
            print ""

            # if the user correctly solves the puzzle, they win and are asked whether they would like to play again
            if solveYN.lower() == "y":
                solvePuzzle = raw_input("Okay hotshot, solve the puzzle: ")
                if solvePuzzle.lower() == theWord.lower():
                    print "You win!"
                    gameAgain = raw_input("Do you want to play again? ")
                    if gameAgain == "n" or gameAgain == "N" or gameAgain == "no" or gameAgain == "NO":
                        totallyGoing = False
                        break
                    break
                # if the user incorrectly solves the puzzle, they lose and are asked whether they would like to play again
                else:
                    print "Wrong!  Aha, you lose!"
                    gameAgain = raw_input("Do you want to play again? Y/N? ")
                    if gameAgain.lower() == "n":
                        totallyGoing = False
                        break
                    break
