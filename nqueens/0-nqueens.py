import sys

def is_valid(board, row, col):
    for r in range(row):
        if board[r] == col or \
            board[r] - r == col - row or \
            board[r] + r == col + row:
            return False
    return True

def print_solution(board):
    for row in board:
        line = ""
        for col in range(len(board)):
            if col == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_util(board, 0)

def solve_util(board, row):
    N = len(board)
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_util(board, row + 1)
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
