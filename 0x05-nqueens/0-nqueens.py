#!/usr/bin/python3
"""Program that solves the N queens problem"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    This function checks the row, upper diagonal, and lower diagonal
    on the left side for any existing queens.

    Args:
    board (list of list of int): The chessboard.
    row (int): Row index on the board.
    col (int): Column index on the board.

    Returns:
    bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col):
    """
    Utilizes backtracking to find all solutions for the N queens problem.

    Args:
    board (list of list of int): The chessboard.
    col (int): The current column to place a queen.

    Returns:
    bool: True if a solution is found, False otherwise.
    """
    if col >= len(board):
        print_solution(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0

    return res


def print_solution(board):
    """
    Prints one solution of the N queens problem.

    Args:
    board (list of list of int): The chessboard with queens placed.
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def solve_nqueens(N):
    """
    Solves the N queens problem by initializing the board and calling
    the utility function to solve the problem.

    Args:
    N (int): The size of the chessboard and the number of queens.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens_util(board, 0):
        print("No solution exists")


def main():
    """
    Main function to handle command-line arguments and initiate
    the N queens solution process.
    """
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

    solve_nqueens(N)


if __name__ == "__main__":
    main()
