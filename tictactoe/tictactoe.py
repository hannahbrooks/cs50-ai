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
    # if action not in actions(board):
    #     raise Exception

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
    for i in board:
        for j in i:
            if j == EMPTY:
                return False

    return True


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
    best_x = float('-inf')
    best_o = best = float('inf')
    move = tuple()

    if terminal(board):
        return None
    else:
        curr_player = player(board)
        board_copy = deepcopy(board)

        if curr_player == X:
            for i in range(3):
                for j in range(3):
                    if board_copy[i][j] == EMPTY:
                        board_copy[i][j] = X
                        move = tuple()
                        move = move + (i, j)

                        val = perform_minimax(board_copy, 0, True)

                        if best_x > val:
                            best_x = val
                            move = tuple()
                            move = move + (i, j)                           

        elif curr_player == O:
            for i in range(3):
                for j in range(3):
                    if board_copy[i][j] == EMPTY:
                        board_copy[i][j] = O
                        move = tuple()
                        move = move + (i, j)

                        val = perform_minimax(board_copy, 0, False)

                        if best_o < val:
                            best_o = val
                            move = tuple()
                            move = move + (i, j)

    return move


def perform_minimax(board, depth, is_maximizing):
    if terminal(board):
        return utility(board)

    if is_maximizing:
        best = float('-inf')
        curr_actions = actions(board)

        for action in curr_actions:
            curr_result = result(board, action)
            val = perform_minimax(curr_result, depth + 1, False)
            best = max(val, best)

        return best
    else:
        best = float('inf')
        curr_actions = actions(board)

        for action in curr_actions:
            curr_result = result(board, action)
            val = perform_minimax(curr_result, depth + 1, True)
            best = min(val, best)

        return best

def print_board(board):
    for i in board:
        for j in i:
            print("value of j: " + str(j))









