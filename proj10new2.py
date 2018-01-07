# CSE 231, section 13
# project 10 - Minesweeper

import random

class grid(object):
    def __init__(self, mines=5):
        '''Makes a new 5 x 5 grid of cells, 5 of which are mines.'''
        squares = []
        cellList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'M','M','M','M','M']
        #random.shuffle(cellList)

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

        for row in squares:
            i = squares.index(row)
            for cell in row:
                j = row.index(cell)
                # the cell is at point self.squares[i][j]
                if cell == 'M':
                    if 0 <= (j-1) <= 4:
                        #same row, one cell left
                        if squares[i][j-1] != 'M':
                            squares[i][j-1] += 1
                    if 0 <= (j+1) <= 4:
                        # same row, one cell right
                        if squares[i][j+1] != 'M':
                            squares[i][j+1] += 1
                    if 0 <= (i-1) <= 4:
                        # one cell up, same column
                        if squares[i-1][j] != 'M':
                            squares[i-1][j] += 1
                        if 0 <= (j-1) <= 4:
                            # one cell up, one column left
                            if squares[i-1][j-1] != 'M':
                                squares[i-1][j-1] += 1
                        if 0 <= (j+1) <=4:
                            # one cell up, one column right
                            if squares[i-1][j+1] != 'M':
                                squares[i-1][j+1] += 1
                    if 0 <= (i+1) <=4:
                        # one cell down, same column
                        if squares[i+1][j] != 'M':
                            squares[i+1][j] += 1
                        if 0 <= (j+1) <= 4:
                            # one cell down, one column right
                            if squares[i+1][j+1] != 'M':
                                squares[i+1][j+1] += 1
                        if 0 <= (j-1) <= 4:
                            # one cell down, one column left
                            if squares[i+1][j-1] != 'M':
                                squares[i+1][j-1] += 1
        self.squares = squares
        print self.squares

        
    def pick_cell(self, x=0, y=0):
        '''Gets the user's inputs'''
        self.x = x
        self.y = y

        self.pickedCell = self.squares[x][y]
        self.playerView[x][y] = self.pickedCell
        return self.pickedCell

##    def unhide_blanks(self):
##        '''Unhide adjacent blank cells'''
##        if 0 <= x-1 <= 4:
##            if self.squares[y][x-1] == 0:
##                    self.squares[y][x-1] += 1
##        if 0 <= x+1 <= 4:
##            if self.squares[y][x+1] != 'M':
##                    self.squares[y][x+1] +=1
##        if 0 <= y-1 <= 4:
##            if self.squares[y-1][x] != 'M':
##                self.squares[y-1][x] += 1
##            if 0 <= x-1 <= 4:
##                if self.squares[y-1][x-1] != 'M':
##                    self.squares[y-1][x-1] += 1
##            if 0 <= x+1 <=4:
##                if self.squares[y-1][x+1] != 'M':
##                    self.squares[y-1][x+1] += 1
##        if 0 <= y+1 <=4:
##            if self.squares[y+1][x] != 'M':
##                self.squares[y+1][x] += 1
##            if 0 <= j+1 <= 4:
##                if self.squares[y+1][x+1] != 'M':
##                    self.squares[y+1][x+1] += 1
##            if 0 <= j - 1 <= 4:
##                if self.squares[y+1][x-1] != 'M':
##                    self.squares[y+1][x -1] += 1
##            
        
    def isWinner(self):
        '''If there are only 5 squares left uncovered, they must be mines, so we win!'''

        
    def __str__(self):
        strGrid = ''
        rowNum = 1
        print "   1 2 3 4 5"
        print "   ---------"
        for row in self.squares:
            strRow = str(rowNum) + '|'
            for column in row:
                strRow += ' ' + str(column)
            strRow += '\n'
            strGrid += strRow
            rowNum += 1
        return strGrid
    

def ripple_effect(playerPick):
    pass
    '''If the cell is a blank one, do the ripple effect.'''

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
        playerPickx = raw_input('Pick a COLUMN, or x-coordinate, from 1 to 5 or press "q" to quit: ')
        if playerPickx == 'q':
            print "Goodbye!"
            break
        elif '1' <= playerPickx <= '5':
            x = int(playerPickx) - 1
        else:
            print "Umm, you can't do that."
            continue
        playerPicky = raw_input('Pick a ROW, or y-coordinate, from 1 to 5 or press "q" to quit: ')
        if playerPicky == 'q':
            print "Goodbye!"
            break
        elif '1' <= playerPicky <= '5':
            y = int(playerPicky) - 1
            cell = gameGrid.pick_cell(y,x)
            if cell == 'M':
                print gameGrid
                print "BOOM!!!"
                break

        else:
            print "Umm, you can't do that."


play()
