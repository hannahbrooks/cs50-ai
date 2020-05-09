"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    for i in board:
        for j in i:
            if j == X:
                x_count+=1
            elif j == O:
                o_count+=1

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i in range (3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception

    board_copy = deepcopy(board)
    board_copy[action[0]][action[1]] = player(board_copy)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # rows
    if (board[0][0] == board[0][1]) and (board[0][0] == board[0][2]) and (board[0][0] != EMPTY):
        return board[0][0]
    if (board[1][0] == board[1][1]) and (board[1][0] == board[1][2]) and (board[1][0] != EMPTY):
        return board[1][0]
    if (board[2][0] == board[2][1]) and (board[2][0] == board[2][2]) and (board[2][0] != EMPTY):
        return board[2][0]
    # columns
    if (board[0][0] == board[1][0]) and (board[0][0] == board[2][0]) and (board[0][0] != EMPTY):
        return board[0][0]
    if (board[0][1] == board[1][1]) and (board[0][1] == board[2][1]) and (board[0][1] != EMPTY):
        return board[0][1]
    if (board[0][2] == board[1][2]) and (board[0][2] == board[2][2]) and (board[0][2] != EMPTY):
        return board[0][2]
    # diags
    if (board[0][0] == board[1][1]) and (board[0][0] == board[2][2]) and (board[1][1] != EMPTY):
        return board[0][0]
    if (board[0][2] == board[1][1]) and (board[0][2] == board[2][0]) and (board[1][1] != EMPTY):
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    curr_winner = winner(board)

    if curr_winner == X:
        return 1
    elif curr_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif board == initial_state():
        return 0, 1
    else:
        curr_player = player(board)
        best_value = float("-inf") if curr_player == X else float("inf")

        for action in actions(board):
            new = perform_minimax(result(deepcopy(board), action), best_value)

            if curr_player == X:
                new = max(best_value, new)
            elif curr_player == O:
                new = min(best_value, new)

            if new != best_value:
                best_value = new
                move = action

        return move
 

def perform_minimax(board, best_value):
    if terminal(board):
        return utility(board)
    else:
        curr_player = player(board)
        value = float("-inf") if curr_player == X else float("inf")

        for action in actions(board):
            new = perform_minimax(result(board, action), value)

            if curr_player == X:
                if new > best_value:
                    return new
                value = max(value, new)
            elif curr_player == O:
                if new < best_value:
                    return new
                value = min(value, new)

        return value








