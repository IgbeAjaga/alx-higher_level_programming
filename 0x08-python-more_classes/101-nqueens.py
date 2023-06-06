#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """Check if it is safe to place a queen at board[row][col]"""
    # Check the current column on the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    """Recursive function to solve the N queens problem"""
    if col >= N:
        # All queens have been placed, print the solution
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen at board[i][col]
            board[i][col] = 1

            # Recur for the next column
            solve_nqueens(board, col + 1)

            # Backtrack and remove the queen from board[i][col]
            board[i][col] = 0

def nqueens(N):
    """Solves the N queens problem"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty N x N chessboard
    board = [[0] * N for _ in range(N)]

    solve_nqueens(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])

