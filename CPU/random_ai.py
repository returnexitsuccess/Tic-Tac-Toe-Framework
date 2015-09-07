import random

def make_move(board, turn, symbol):
    empty = []
    for i in range(9):
        if board[i] == " ":
            empty.append(i)
    return random.choice(empty)
