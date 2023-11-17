#!/usr/bin/python3
import sys


def is_valid(board, row, col):
    for r in range(row):
        if board[r] == col or \
                board[r] - r == col - row or \
                board[r] + r == col + row:
            return False
    return True


def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_util(board, 0, solutions)
    for sol in solutions:
        print(sol)


def solve_util(board, row, solutions):
    N = len(board)
    if row == N:
        sol = []
        for i in range(N):
            sol.append([i, board[i]])
        solutions.append(sol)
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_util(board, row + 1, solutions)
            board[row] = -1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
