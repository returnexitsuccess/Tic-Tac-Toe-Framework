import random

def make_move(board, turn, symbol):
    if symbol == "X":
        result = ai_x_turn(board, turn)
    else:
        result = ai_o_turn(board, turn)
    return result[0]

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

def ai_o_turn(board, turn):
    empty = []
    for i in range(9):
        if board[i] == " ":
            empty.append(i)
    if winner(board) != 0:
        return [empty[0], winner(board)]
    if (turn == 8):
        bcopy = list(board)
        bcopy[empty[0]] = "O"
        return [empty[0], winner(bcopy)]
    else:
        current_max = -1
        max_moves = []
        for i in empty:
            bcopy = list(board)
            bcopy[i] = "O"
            score = ai_x_turn(bcopy, turn + 1)[1]
            if score > current_max:
                current_max = score
                max_moves = [i]
            elif score == current_max:
                max_moves.append(i)

        return [random.choice(max_moves), current_max]

def ai_x_turn(board, turn):
    empty = []
    for i in range(9):
        if board[i] == " ":
            empty.append(i)
    if winner(board) != 0:
        return [empty[0], winner(board)]
    if (turn == 8):
        bcopy = list(board)
        bcopy[empty[0]] = "X"
        return [empty[0], winner(bcopy)]
    else:
        current_min = 1
        min_moves = []
        for i in empty:
            bcopy = list(board)
            bcopy[i] = "X"
            score = ai_o_turn(bcopy, turn + 1)[1]
            if score < current_min:
                current_min = score
                min_moves = [i]
            elif score == current_min:
                min_moves.append(i)

        return [random.choice(min_moves), current_min]
