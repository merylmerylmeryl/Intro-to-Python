# proj04
# CSE 231, section 3

x = 6
wrongLetterList = ""
rightLetterList = ""
spaces = ""
keepGoing = True

print "You like hangman, right?  Well, regardless, you're going to play it"
print "because I had to make it, and you're going to like it. Plus it's a"
print "life-or-death situation, and who doesn't like those?"
print ""
print "You get six chances, so don't screw up."
print "Have someone enter in the phrase to be guessed, and you"
print "have to guess one letter at a time what it is. Each time you guess a letter"
print "that isn't in the word, you lose one more chance to live."
print ""

# Gets a word or phrase from the player
theWord = raw_input("What's the word you want to guess? ")

# Have a loop going until the player runs out of chances.
# When the counter drops to 0, the player gets a game over. Oh noes!

# keepGoing starts out as True...
while keepGoing:

# Look at each character in theWord. Depending on what it is, either copy that character into
# a blank string, or put a "_" where the letter would go.
    while x > 0:
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
        print spaces
        print ""
        print "Chances left: ", x
        print ""

        if spaces.find("_") == -1:
            print "YOU WIN!"
            break
        letterGuess = raw_input("Guess a letter: ")
        if theWord.find(letterGuess) == -1 and theWord.find(letterGuess.upper()) == -1 and theWord.find(letterGuess.lower()) == -1:
            x -= 1
            wrongLetterList = wrongLetterList + " " + letterGuess
            print "HAH! That letter isn't in the word, and you lose one chance."
            print "chances: ", x
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
            print "chances: ", x
            print "wrong letters used: ", wrongLetterList
    if x == 0:
        print "GAME OVER!"

    gameAgain = raw_input("Do you want to play again? ")
    if gameAgain == "n" or gameAgain == "N" or gameAgain == "no" or gameAgain == "NO":
        keepGoing = False
    else:
        x = 6
        wrongLetterList = ""
        rightLetterList = ""
        spaces = ""
        theWord = raw_input("What's the word you want to guess? ")
