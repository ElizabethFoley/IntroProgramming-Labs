# CMPT 120 Intro to Programming
# Lab #7- Lists and Functions
# Libby Foley
# Nov. 11, 2018

symbol = [" ", "x", "o"]

# matrix --> a list within a list
board = [ [0,1],    # one row   
           [2,3] ]
cell = board[0][0]

def printRow(row):
    # initialize output to the left of the border 
    output = "|"
    # for each square in row
    for cell in row:
        # add to outpu tthe symbol for this square followed by a border
        output += " " + symbol[cell] + " |"
    # print the completed output for this row
    print(output)
    pass

def printBoard(board):
    # print the top border
    print("+-----------+")
    # for each row in the board...
    for i in range(3):
        # print the row
        printRow(board[i])
        # print the next border
        print("+-----------+")
    pass

def markBoard(board, row, col, player):
    # check to see whether the desired square is blank
    if board[row][col] == 0:
        # if so, set it to the top player number
        board[row][col] = player
    else:
        print("invalid move, space is taken")
    pass

def getPlayerMove():
    row = int(input("Pick a row: "))   # prompt the user seperately for the row and column numbers
    col = int(input("Pick a column: "))
    return (row,col)    # then return that row and column instead of (0,0)

def hasBlanks(board):
    # for each row in the board...
    for row in range(3):
        # for each square in the row...
        for col in range(3):
            # check whether the square is blank
            if board[row][col] == 0:
                # if so, return True
                return True
    # if no square is blank, return False
    return False

def main():
    board=[[0, 0, 0],[0, 0, 0],[0, 0, 0]]   # TODO replace this with a three-by-three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1    # switch player for next turn
main()
