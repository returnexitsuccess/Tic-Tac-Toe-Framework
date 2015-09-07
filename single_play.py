import Human.human as p1
import CPU.easy_ai as p2

from base_game import *

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

print_board(board)
if winner(board) == 1:
    print "P2 Wins!"
elif winner(board) == -1:
    print "P1 Wins!"
else:
    print "Tie"
