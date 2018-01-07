# proj 11
# CSE 231, section 13

filename = open('stats.txt', 'a')
x = 0
dataList = []

def makeInfoList():
    infoList = []
    name = raw_input("What is your name? (just first name is fine)  ")
    infoList.append(name)
    age = raw_input("What is your age?  ")
    infoList.append(age)
    siblings = raw_input("How many siblings do you have? ")
    infoList.append(siblings)
    color = raw_input("What is your favorite color? ")
    infoList.append(color)
    season = raw_input("What is your favorite season? ")
    infoList.append(season)
    return infoList

print "*!* PLAYER 1 *!*"
infoList_1 = makeInfoList()
print "\n" * 3
print "*!* PLAYER 2 *!*"
infoList_2 = makeInfoList()
    
while x < 5:
    print "The hotel has lost both your suitcases.  Coincidentally, both suitcases were exactly"
    print "the same and contained exactly the same contents.  We apologize sincerely."
    print ""
    print "Each of you will be independently allowed to guess the amount of money the suitcase was worth."
    print ""
    print "If you both enter the same amount of money, that will be regarded as the true value of the suitcase"
    print "you will both receive that amount of money."
    print ""
    print "Otherwise, if one of you enters a greater amount of money, the LOWER value will be regarded as the"
    print "true value.  The lower guesser will receive that amount of money PLUS $2, "
    print "and the higher guesser will receive the lower amount of money MINUS $2."

    while True:
        try:
            amount_1 = int(raw_input("First traveler, please enter your amount:  $"))
        except ValueError:
            print ""
            print "Something was wrong with the amount you entered."
            continue
        if 2 <= amount_1 <= 100:
            break
        else:
            print "Something was wrong with the amount you entered."


    print "\n" * 100

    while True:
        try:
            amount_2 = int(raw_input("Second traveler, please enter your amount:  $"))
        except ValueError:
            print ""
            print "Something was wrong with the amount you entered."
            continue
        if 2 <= amount_2 <= 100:
            break
        else:
            print "Something was wrong with the amount you entered."

    guessTup = (str(amount_1), str(amount_2))    

    print "Traveler 1 entered $%i and Traveler 2 entered $%i."%(amount_1, amount_2)

    if amount_1 > amount_2:
        newAmount_1 = amount_2 - 2
        newAmount_2 = amount_2 + 2
    elif amount_2 > amount_1:    
        newAmount_2 = amount_1 - 2
        newAmount_1 = amount_1 + 2
    else:
        newAmount_1 = amount_1
        newAmount_2 = newAmount_1
        print "Both travelers entered the same amount."
    print "Traveler 1 receives $%i."%(newAmount_1)
    print "Traveler 2 receives $%i."%(newAmount_2)

    print ""
    print ""
    print ""

    dataList.append(guessTup)
    x += 1

    if x == 5:
        print "Thanks for playing!"
    
    if amount_1 == 2 or amount_2 == 2:
        print "Thanks for playing!"
        break

filename.write(str(x))
filename.write('\n')

for item in infoList_1:
    filename.write(item)
    if infoList_1.index(item) != (len(infoList_1) - 1):
        filename.write(',')
filename.write("\n")

for item in infoList_2:
    filename.write(item)
    if infoList_2.index(item) != (len(infoList_2) - 1):
        filename.write(',')
filename.write("\n")

for tup in dataList:
    filename.write(tup[0])
    filename.write(' ')
    filename.write(tup[1])
    if dataList.index(tup) != (len(dataList) - 1):
        filename.write(',')

filename.write('\n')
filename.write('\n')
filename.close()

