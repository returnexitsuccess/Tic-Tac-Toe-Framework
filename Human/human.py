def make_move(board, turn, symbol):
    print_board(board)
    print "You are playing as " + symbol
    print "Where would you like to play?"
    move = int(raw_input())
    while board[move - 1] != " ":
        print "Please select an open square"
        print
        print "Where would you like to play?"
        move = int(raw_input())
    return move - 1

def print_board(board):
    bcopy = list(board)
    for i in range(9):
        if bcopy[i] == " ":
            bcopy[i] = str(i + 1)

    print " " + bcopy[0] + " | " + bcopy[1] + " | " + bcopy[2] + " "
    print "___|___|___"
    print " " + bcopy[3] + " | " + bcopy[4] + " | " + bcopy[5] + " "
    print "___|___|___"
    print " " + bcopy[6] + " | " + bcopy[7] + " | " + bcopy[8] + " "
    print "   |   |   "
