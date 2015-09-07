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

def winner(board):
    #rows
    if (board[0] == "X" and board[1] == "X" and board[2] == "X"):
        return -1
    if (board[3] == "X" and board[4] == "X" and board[5] == "X"):
        return -1
    if (board[6] == "X" and board[7] == "X" and board[8] == "X"):
        return -1
    if (board[0] == "O" and board[1] == "O" and board[2] == "O"):
        return 1
    if (board[3] == "O" and board[4] == "O" and board[5] == "O"):
        return 1
    if (board[6] == "O" and board[7] == "O" and board[8] == "O"):
        return 1

    #columns
    if (board[0] == "X" and board[3] == "X" and board[6] == "X"):
        return -1
    if (board[1] == "X" and board[4] == "X" and board[7] == "X"):
        return -1
    if (board[2] == "X" and board[5] == "X" and board[8] == "X"):
        return -1
    if (board[0] == "O" and board[3] == "O" and board[6] == "O"):
        return 1
    if (board[1] == "O" and board[4] == "O" and board[7] == "O"):
        return 1
    if (board[2] == "O" and board[5] == "O" and board[8] == "O"):
        return 1

    #diagonals
    if (board[0] == "X" and board[4] == "X" and board[8] == "X"):
        return -1
    if (board[2] == "X" and board[4] == "X" and board[6] == "X"):
        return -1
    if (board[0] == "O" and board[4] == "O" and board[8] == "O"):
        return 1
    if (board[2] == "O" and board[4] == "O" and board[6] == "O"):
        return 1

    return 0
                    
def is_game_over(board, turn):
    if turn >= 9:
        return True
    return (winner(board) != 0)

