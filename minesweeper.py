import random
import sys

sys.setrecursionlimit(50)

class grid(object):
    def __init__(self, mines=5):
        self.InitGrids()

    def InitGrids(self):
        '''Makes a new 5 x 5 grid of cells, 5 of which are mines.'''
        squares = []
        cellList = [0,0,0,0,0,0,0,0,0,0,'M','M','M','M','M', 0,0,0,0,0,0,0,0,0,0]
        random.shuffle(cellList)

        # goes through the now randomly shuffled cellList and appends each
        # element to the 2D array.
        for q in range(5):
            a_row = []
            for t in range(5):
                a_row.append(cellList.pop())
            squares.append(a_row)

        # creates another grid, which is the one the player will be looking at.
        # just has a bunch of H's.
        playerView = []
        for k in range(5):
            eleList = []
            for l in range(5):
                eleList.append('H')
            playerView.append(eleList)
        self.playerView = playerView

        # now finish making the real grid by changing 0's to numbers
        # if there are mines nearby.
        for i in range(5):
            for j in range(5):
                # the cell is at point self.squares[i][j]
                if squares[i][j] == 'M':
                    # west neighbor
                    if j > 0 and squares[i][j-1] != 'M':
                        squares[i][j-1] += 1
                    # east neighbor
                    if j < 4 and squares[i][j+1] != 'M':
                        squares[i][j+1] += 1
                    # south neighbor
                    if i < 4 and squares[i+1][j] != 'M':
                        squares[i+1][j] += 1
                    # north neighbor
                    if i > 0 and squares[i-1][j] != 'M':
                        squares[i-1][j] += 1
                    # northwest neighbor
                    if i > 0 and j > 0 and squares[i-1][j-1] != 'M':
                        squares[i-1][j-1] += 1
                    # northeast neighbor
                    if i > 0 and j < 4 and squares[i-1][j+1] != 'M':
                        squares[i-1][j+1] += 1
                    # southeast neighbor
                    if i < 4 and j < 4 and squares[i+1][j+1] != 'M':
                        squares[i+1][j+1] += 1
                    # southwest neighbor
                    if i < 4 and j > 0 and squares[i+1][j-1] != 'M':
                        squares[i+1][j-1] += 1
                        
        self.squares = squares
        
    def unhide_blanks(self, row, col):
        ''' If the player picks a tile that has a 0 under it, reveal all
        the tiles in the same row, in the same column, and diagonally until
        we get to a tile that isn't a zero.'''
        if self.squares[row][col] == 0:
            self.playerView[row][col] = self.squares[row][col]
            i = row
            j = col
            
            # south mines
            while i < 5:
                if self.squares[i][col] != 'M':
                    self.playerView[i][col] = self.squares[i][col]
                    if self.squares[i][col] != 0:
                        break
                else:
                    break
                i += 1
            i = row
            # 
            while i > -1:
                if self.squares[i][col] != 'M':
                    self.playerView[i][col] = self.squares[i][col]
                    if self.squares[i][col] != 0:
                        break
                else:
                    break
                i = i - 1
            while j < 5:
                if self.squares[row][j] != 'M':
                    self.playerView[row][j] = self.squares[row][j]
                    if self.squares[row][j] != 0:
                        break
                else:
                    break
                j += 1
            j = col
            while j > -1:
                if self.squares[row][j] != 'M':
                    self.playerView[row][j] = self.squares[row][j]
                    if self.squares[row][i] != 0:
                        break
                else:
                    break
                j = j - 1


            i = row
            j = col
            while i < 5 and j < 5:
                if self.squares[i][j] != 'M':
                    self.playerView[i][j] = self.squares[i][j]
                    if self.squares[i][j] != 0:
                        break
                else:
                    break
                i += 1
                j += 1
            i = row
            j = col
            while i < 5 and j > -1:
                if self.squares[i][j] != 'M':
                    self.playerView[i][j] = self.squares[i][j]
                    if self.squares[i][j] != 0:
                        break
                else:
                    break
                i += 1
                j = j - 1
            i = row
            j = col
            while i > -1 and j < 5:
                if self.squares[i][j] != 'M':
                    self.playerView[i][j] = self.squares[i][j]
                    if self.squares[i][j] != 0:
                        break
                else:
                    break
                i = i - 1
                j += 1
            i = row
            j = col
            while i > -1 and j > -1:
                if self.squares[i][j] != 'M':
                    self.playerView[i][j] = self.squares[i][j]
                    if self.squares[i][j] != 0:
                        break
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
            print(self.__str__())

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
        print("   1 2 3 4 5")
        print("   ---------")
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
    print("Rules of Minesweeper")
    print("Goal, uncover all cells that are not mines.")
    print("1) Pick a cell.")
    print("2) If the cell has a mine underneath, you lose!")
    print("3) If the cell has a number on it, then this shows how many")
    print("mines are nearby.")
    print("Responses are:   '1-5' pick a row")
    print("                 '1-5' pick a column")
    print("                 'q' to quit")


def play():
    '''main program. Does error checking on the user input.'''
    printRules()
    gameGrid = grid()

    while True:
        print(gameGrid)
        playerPickx = input('Pick a ROW from 1 to 5 or press "q" to quit: ')
        if playerPickx == 'q':
            print("Scaredy-cat!")
            break
        elif '1' <= playerPickx <= '5':
            x = int(playerPickx) - 1
        else:
            print("Umm, you can't do that.")
            continue
        playerPicky = input('Pick a COLUMN from 1 to 5 or press "q" to quit: ')
        if playerPicky == 'q':
            print("Scaredy-cat!")
            break
        elif '1' <= playerPicky <= '5':
            y = int(playerPicky) - 1

            # 
            if gameGrid.squares[x][y] == 0:
                gameGrid.unhide_blanks(x,y)
            elif gameGrid.squares[x][y] == 'M':
                gameGrid.isLoser(x,y)
                print("\nYOU LOSE!!!!!!!!")
                playAgain = input("Try again? ")
                if playAgain.lower() == 'y':
                    printRules()
                    gameGrid = grid()
                    continue
                else:
                    break
            else:
                gameGrid.playerView[x][y] = gameGrid.squares[x][y]

        else:
            print("Umm, you can't do that.")

        if gameGrid.isWinner():
            print("YOU WIN!!!!!")
            playAgain = input("Play again? ")
            if playAgain.lower() == 'y' or playAgain.lower() == 'yes':
                printRules()
                gameGrid = grid()
                continue
            else:
                break


play()
