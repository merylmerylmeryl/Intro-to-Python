from cards import *

def makeTableau(deck):
    return [deck.deal() for card in range(5)]

def setup():
    '''
    paramaters: None
    returns a tuple of:
    - a stock (a shuffled deck after dealing 35 cards to tableau and 1 card to foundation)
    - a foundation (with one card)
    - a tableau (list of 7 lists, each has 5 cards)
    '''
    stock = Deck()
    stock.shuffle()
    foundation = [stock.deal()]
    tableau = [makeTableau(stock),makeTableau(stock),makeTableau(stock),\
               makeTableau(stock),makeTableau(stock),makeTableau(stock),\
               makeTableau(stock)]
    
    return (stock, foundation, tableau)


def printGame(stock,fdation,tableau):
    '''
    parameters: a stock, a foundation and a tableau
    returns: Nothing
    prints the current situation of the game
    '''

    print "Tableau"
    for x in range(7):
        s = ""
        tableauRow = tableau[x]
        for y in range(len(tableauRow)):
            s += tableauRow[y].__str__() + " "
        print "Row ", x + 1, ": ", s

    s2 = ""
    for y in range(len(fdation)):
        s2 += fdation[y].__str__() + " "
        
    print "-" * 10
    print "Foundation: ", s2
    print "-" * 10
    print "Stock:", stock.cards_left(), "cards left.\n"
    

def canMove(tRow,tableau,fdation):
    '''
    parameters: a row num, a tableau and a foundation
    returns: Boolean
    tests if the card at the end of the row can be moved to the foundation
    '''

    if len(tableau[(tRow - 1)]) > 0:
        card = tableau[(tRow - 1)][-1]
        topFdation = fdation[-1]

        if card.get_rank() == (topFdation.get_rank() - 1) or card.get_rank() == (topFdation.get_rank() + 1):
            return True
        elif card.get_rank() == 1 and topFdation.get_rank() == 13:
            return True
        elif card.get_rank() == 13 and topFdation.get_rank() == 1:
            return True
        else:
            return False
    else:
        return False
          
def moveToFoundation(tRow,tableau,fdation):
    '''
    parameters: a row num, a tableau and a foundation
    returns: nothing
    moves a card at the end of a row to the foundation if it can
    '''

    if canMove(tRow, tableau, fdation):
        card = tableau[tRow - 1].pop(-1)
        fdation.append(card)
    else:
        print "You can't make that move!"
        return False
        


def dealMoreCards(stock,fdation):
    '''
    parameters: a stock and a tableau
    returns: Boolean
    deal one card from stock to foundation
    returns False if it runs out of cards
    '''
    if stock.cards_left() > 0:
        newCard = stock.deal()
        fdation.append(newCard)
    else:
        return False

def isWinner(tableau):
    '''
    parameters: a tableau
    return: a Boolean
    is this a winning position. No cards left in each tableau row.
    '''
    winCount = 0
    
    for x in range(7):
        if len(tableau[x]) == 0:
            winCount += 1

    if winCount == 7:
        return True
    else:
        return False


def isLoser(stock, fdation, tableau):
    '''
    parameters: a stock, a foundation and a tableau
    return: a Boolean
    is this a Loser position.
    Loser position should satisfy two conditions:
    1. No cards left in stock.
    2. No possible move from tableau
    '''

    loseCount = 0
    
    for x in range(7):
        if not canMove(x+1, tableau, fdation):
            loseCount += 1

    if stock.cards_left() <= 0 and loseCount == 7:
        return True
    else:
        return False


def printRules():
    '''
    parameters: none
    returns: nothing
    prints the rules
    '''
    print "Rules of Golf Relaxed"
    print "Goal, move all the cards to the foundation"
    print "1) All cards move from the tableau (7 rows) to the foundation"
    print "2) Only the last card in each row of the tableau can be moved"
    print "3) You may move a card from the tableau to the foundation when there is a card"
    print "   in the tableau whose rank is adjacent to the rank of the top card of the foundation."
    print "   Ace and King are considered adjacent. "
    print "4) If there are remaining card(s) in the stock. You may deal one card at a time "
    print "   to the top of the foundation. "    
    print ""
    print "Responses are: '1-7' card to move to the foundation"
    print "          'd' to deal one card"
    print "          'q' to quit"


def play():
    ''' 
    main program. Does error checking on the user input. 
    '''
    printRules()
    
    stock, foundation, tableau = setup()

    while True:
        printGame(stock,foundation,tableau)
        if isLoser(stock, foundation, tableau):
            print "You lose!  :("
            break
        elif isWinner(tableau):
            print "You win!!!!!  MY HERO!!!!  :]"
            break
        else:
            move = raw_input("Command: ")
            if move == "q":
                print "Goodbye!"
                break

            elif move == "d":
                dealMoreCards(stock, foundation)
            elif move.isdigit():
                move = int(move)
                if 0 < move < 8:                
                    moveToFoundation(move, tableau, foundation)
                else:
                    print "There aren't that many rows!  ^-^;;"
            else:
                print move + "?", "What? Whatever you're trying to do, it's not gonna work.  Try again!"

play()
