# CSE 231, section 13
# project 10 Skeleton - Minesweeper

import random

class cell(object):
    def __init__(self, value = 0):
        '''Give a cell its default value.'''
        self.value = value
    def is_hidden(self):
        '''Each cell is hidden by default.  If the user chooses the
        cell, return True.'''
        pass
    def mines_nearby(self):
        '''Check to see if there are any nearby mines.  If there are,
        return this number; otherwise return 0.'''
        pass
    def is_mine(self):
        '''If the cell is a mine, return 1.  Otherwise return 0.'''
        pass
    def __str__(self):
        '''String representation of the cell for printing: value. First check
        is_hidden. If it's true, strValue is an H.'''
        strValue = str(self.value)
        return strValue



class grid(object):
    def __init__(self, mines=5):
        '''Makes a new 5 x 5 grid of cells, 5 of which are mines.'''
        self.squares = []
        self.cellList = ['M','M','M','M','M',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.cellList
        print self.cellList
        for i in range(5):
            row = []
            for j in range(5):
                row.append(0)
            self.squares.append(row)
    def isWinner(self):
        '''If the only squares left on the grid have mines underneath,
        return True. Otherwise return False.'''
        pass
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


def setup():
    pass
    '''Make a new grid.'''

def ripple_effect(playerPick):
    pass
    '''If the cell is a blank one, do the ripple effect.'''

def isMine(playerPick):
    pass
    '''If the cell that the user has picked is a mine, the game ends and
    the player is notified that he/she has lost.'''

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
    mygrid = grid()
    print mygrid

play()
