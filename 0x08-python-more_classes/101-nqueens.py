#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if a queen can be placed at board[row][col]
    # without attacking any previously placed queens

    # Check the current row on the left side
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

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def solve_util(col):
        if col == N:
            # All queens are placed, add the current solution
            solution = []
            for row in range(N):
                for col in range(N):
                    if board[row][col] == 1:
                        solution.append([row, col])
            solutions.append(solution)
            return True

        # Try placing a queen in each row of the current column
        for row in range(N):
            if is_safe(board, row, col, N):
                # Place the queen at board[row][col]
                board[row][col] = 1

                # Recur to place the rest of the queens
                solve_util(col + 1)

                # Backtrack and remove the queen from board[row][col]
                board[row][col] = 0

    solve_util(0)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)

