import random

def make_move(board, turn, symbol):
    if symbol == "X":
        pot_move = check_win_x(list(board))
        if pot_move != -1:
            return pot_move

        pot_move = check_win_o(list(board))
        if pot_move != -1:
            return pot_move
    else:
        pot_move = check_win_o(list(board))
        if pot_move != -1:
            return pot_move

        pot_move = check_win_x(list(board))
        if pot_move != -1:
            return pot_move

    empty = []
    for i in range(9):
        if board[i] == " ":
            empty.append(i)
    return random.choice(empty)

def check_win_x(board):
    empty = []
    for i in range(9):
        if board[i] == " ":
            empty.append(i)

    moves = []
    for i in empty:
        bcopy = list(board)
        bcopy[i] = "X"
        if winner(bcopy) == -1:
            moves.append(i)
    if len(moves) != 0:
        return random.choice(moves)
    return -1

def check_win_o(board):
    empty = []
    for i in range(9):
        if board[i] == " ":
            empty.append(i)

    moves = []
    for i in empty:
        bcopy = list(board)
        bcopy[i] = "O"
        if winner(bcopy) == 1:
            moves.append(i)
    if len(moves) != 0:
        return random.choice(moves)
    return -1

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
