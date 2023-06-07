#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard

Attributes:
    N (int): base number of queens, and length of board side in piece positions
    players (list) of (list) of (list) of (int): list of all successful
        solutions for given amount of columns checked

"""
from sys import argv

if len(argv) is not 2:
    print('Usage: nqueens N\n')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number\n')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4\n')
    exit(1)


def board_column(board=[]):
    """Adds a vertical zeroes to the right of the board
    for queen arrangements in that column.

    Args:
        board (list) of (list) of (int): testing the rightmost
        column for queen conflicts.

    Returns:
        modified 2D list

    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def adding_queen(board, row, col):
    """Sets queen to coordinates given in board.

    Args:
        board (list) of (list) of (int): testing the rightmost
        column for queen conflicts.
        row (int): first index
        col (int): second index

    """
    board[row][col] = 1


def new_safe_queen(board, row, col):
    """checking that for a new queen placed in the rightmost
    column is safe.

    Args:
        board (list) of (list) of (int): testing the rightmost
        column for queen conflicts.
        row (int): first index
        col (int): second index

    Returns:
        True if no left side conflicts found for new queen, or False if a
    conflict is found.

    """
    a = row
    b = col

    for i in range(1, N):
        if (b - i) >= 0:
            if (a - i) >= 0:
                if board[a - i][b - i]:
                    return False
            if board[a][b - i]:
                return False
            if (a + i) < N:
                if board[a + i][b - i]:
                    return False
    return True


def coordinate_approach(players):
    """Change a board to a series of row and column
    indicies of each queen.

    Args:
    players (list) of (list) of (list) of (int): list of all successful
        solutions for number of colums checked lastly

    Attributes:
        igbe (list) of (list) of (int): each member list contains the row
    column number for each queen found

    Returns:
        igbe, the list of coordinates

    """
    igbe = []
    for a, attempt in enumerate(players):
        igbe.append([])
        for i, row in enumerate(attempt):
            igbe[a].append([])
            for j, col in enumerate(row):
                if col:
                    igbe[a][i].append(i)
                    igbe[a][i].append(j)
    return igbe

players = []
players.append(board_column())

for col in range(N):
    new_players = []
    for matrix in players:
        for row in range(N):
            if new_safe_queen(matrix, row, col):
                temp = [line[:] for line in matrix]
                adding_queen(temp, row, col)
                if col < N - 1:
                    board_column(temp)
                new_players.append(temp)
    players = new_players

for item in coordinate_approach(players):
    print(item)
