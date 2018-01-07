# CSE 231, section 13
# project 10 - Minesweeper

import random
import sys

sys.setrecursionlimit(50)

class grid(object):
    def __init__(self, mines=5):
        '''Makes a new 5 x 5 grid of cells, 5 of which are mines.'''
        squares = []
        cellList = [0,0,0,0,0,0,0,0,0,0,'M','M','M','M','M', 0,0,0,0,0,0,0,0,0,0]
        random.shuffle(cellList)

        playerView = []
        for k in range(5):
            eleList = []
            for l in range(5):
                eleList.append('H')
            playerView.append(eleList)
        self.playerView = playerView


        for q in range(5):
            a_row = []
            for t in range(5):
                a_row.append(cellList.pop())
            squares.append(a_row)

        for i in range(5):
            for j in range(5):
                # the cell is at point self.squares[i][j]
                if squares[i][j] == 'M':
                    # same row, one cell left
                    if j > 0 and squares[i][j-1] != 'M':
                        squares[i][j-1] += 1
                    # same row, one cell right
                    if j < 4 and squares[i][j+1] != 'M':
                        squares[i][j+1] += 1
                    # one cell down, same column
                    if i < 4 and squares[i+1][j] != 'M':
                        squares[i+1][j] += 1
                    # one cell up, same column
                    if i > 0 and squares[i-1][j] != 'M':
                        squares[i-1][j] += 1
                    # one cell up, one column left
                    if i > 0 and j > 0 and squares[i-1][j-1] != 'M':
                        squares[i-1][j-1] += 1
                    # one cell up, one column right
                    if i > 0 and j < 4 and squares[i-1][j+1] != 'M':
                        squares[i-1][j+1] += 1
                    # one cell down, one column right
                    if i < 4 and j < 4 and squares[i+1][j+1] != 'M':
                        squares[i+1][j+1] += 1
                    # one cell down, one column left
                    if i < 4 and j > 0 and squares[i+1][j-1] != 'M':
                        squares[i+1][j-1] += 1
                        
        self.squares = squares
        
    def unhide_blanks(self, x, y):
        if self.squares[x][y] == 0:
            self.playerView[x][y] = self.squares[x][y]
            i = x
            j = y
            while i < 5:
                if self.squares[i][y] == 0:
                    self.playerView[i][y] = self.squares[i][y]
                else:
                    break
                i += 1
            i = x
            while i > -1:
                if self.squares[i][y] == 0:
                    self.playerView[i][y] = self.squares[i][y]
                else:
                    break
                i = i - 1
            while j < 5:
                if self.squares[x][j] == 0:
                    self.playerView[x][j] = self.squares[x][j]
                else:
                    break
                j += 1
            j = y
            while j > -1:
                if self.squares[x][j] == 0:
                    self.playerView[x][j] = self.squares[x][j]
                else:
                    break
                j = j - 1


            i = x
            j = y
            while i < 5 and j < 5:
                if self.squares[i][j] == 0:
                    self.playerView[i][j] = self.squares[i][j]
                else:
                    break
                i += 1
                j += 1
            i = x
            j = y
            while i < 5 and j > -1:
                if self.squares[i][j] == 0:
                    self.playerView[i][j] = self.squares[i][j]
                else:
                    break
                i += 1
                j = j - 1
            i = x
            j = y
            while i > -1 and j < 5:
                if self.squares[i][j] == 0:
                    self.playerView[i][j] = self.squares[i][j]
                else:
                    break
                i = i - 1
                j += 1
            i = x
            j = y
            while i > -1 and j > -1:
                if self.squares[i][j] == 0:
                    self.playerView[i][j] = self.squares[i][j]
                else:
                    break
                i = i - 1
                j = j - 1

        else:
            return False
                

    def isLoser(self, x, y):
        if self.squares[x][y] == 'M':
            for i in range(5):
                for y in range(5):
                    self.playerView[i][y] = self.squares[i][y]
            print self.__str__()

    def isWinner(self):
        '''If there are only 5 squares left uncovered, they must be mines, so we win!'''
        squareCount = 0
        for i in range(5):
            for j in range(5):
                if self.squares[i][j] != self.playerView[i][j]:
                    squareCount += 1

        if squareCount == 5:
            return True
        else:
            return False
        
    def __str__(self):
        strGrid = ''
        rowNum = 1
        print "   1 2 3 4 5"
        print "   ---------"
        for row in self.playerView:
            strRow = str(rowNum) + '|'
            for column in row:
                strRow += ' ' + str(column)
            strRow += '\n'
            strGrid += strRow
            rowNum += 1
        return strGrid
    
    
def printRules():
    pass
    '''prints the rules'''
    print "Rules of Minesweeper"
    print "Goal, uncover all cells that are not mines."
    print "1) Pick a cell."
    print "2) If the cell has a mine underneath, you lose!"
    print "3) If the cell has a number on it, then this shows how many"
    print "mines are nearby."
    print "Responses are:   '1-5' pick a row"
    print "                 '1-5' pick a column"
    print "                 'q' to quit"


def play():
    '''main program.Does error checking on the user input.'''
    printRules()
    gameGrid = grid()

    while True:
        print gameGrid
        playerPickx = raw_input('Pick a ROW from 1 to 5 or press "q" to quit: ')
        if playerPickx == 'q':
            print "Scaredy-cat!"
            break
        elif '1' <= playerPickx <= '5':
            x = int(playerPickx) - 1
        else:
            print "Umm, you can't do that."
            continue
        playerPicky = raw_input('Pick a COLUMN from 1 to 5 or press "q" to quit: ')
        if playerPicky == 'q':
            print "Scaredy-cat!"
            break
        elif '1' <= playerPicky <= '5':
            y = int(playerPicky) - 1
            
            if gameGrid.squares[x][y] == 0:
                gameGrid.unhide_blanks(x,y)
            elif gameGrid.squares[x][y] == 'M':
                gameGrid.isLoser(x,y)
                print "\nYOU LOSE!!!!!!!!"
                playAgain = raw_input("Try again?" )
                if playAgain.lower() == 'y':
                    printRules()
                    gameGrid = grid()
                    continue
                else:
                    break
            else:
                gameGrid.playerView[x][y] = gameGrid.squares[x][y]

        else:
            print "Umm, you can't do that."

        if gameGrid.isWinner():
            print "YOU WIN!!!!!"
            playAgain = raw_input("Play again?" )
            if playAgain.lower() == 'y':
                printRules()
                gameGrid = grid()
                continue
            else:
                break


play()