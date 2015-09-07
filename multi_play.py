RUNS = 10

import CPU.hard_rand_ai as p1
import CPU.hard_rand_ai as p2

from base_game import *

i = 0
wins = [0, 0, 0]
while i < RUNS:
    turn = 0
    board = [" "] * 9
    while (not is_game_over(board, turn)):
        if (turn % 2 == 0):
            move = p1.make_move(list(board), turn, "X")
            if board[move] != " ":
                raise Exception
            else:
                board[move] = "X"
        else:
            move = p2.make_move(board, turn, "O")
            if board[move] != " ":
                raise Exception
            else:
                board[move] = "O"
        turn += 1

    if winner(board) == 1:
        wins[1] += 1
    elif winner(board) == -1:
        wins[0] += 1
    else:
        wins[2] += 1

    i += 1

print wins
