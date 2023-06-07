#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard

Attributes:
    board (list): A list of lists representing the chessboard.
    result (list): A list of lists containing results.
"""
import sys


def initial_board(n):
    """Initialize an NxN chessboard"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def copy_board(board):
    """Return a copy of a chessboard."""
    if isinstance(board, list):
        return list(map(copy_board, board))
    return (board)


def get_result(board):
    """Return the list of lists of a solved chessboard."""
    result = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                result.append([r, c])
                break
    return (result)


def xout(board, row, col):
    """X spots on a chessboard.

    Args:
        board (list): The chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
        c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def repetition_solve(board, row, queens, result):
    """Solving the repetition of an N-queens puzzle.

    Args:
        board (list): The chessboard.
        row (int): The row.
        queens (int): The number of queens placed.
        result (list): A list of lists of results.
    Returns:
        result
    """
    if queens == len(board):
        result.append(get_result(board))
        return (result)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = copy_board(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            result = repetition_solve(tmp_board, row + 1,
                                        queens + 1, result)

    return (result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number\n")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4\n")
        sys.exit(1)

    board = initial_board(int(sys.argv[1]))
    result = repetition_solve(board, 0, 0, [])
    for igbe in result:
        print(igbe)

