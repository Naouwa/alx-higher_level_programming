#!/usr/bin/python3
"""The N queens puzzle
    the challenge of placing N non-attacking queens on an N×N chessboard.
    This is a program that solves the N queens problem.
"""

import sys


def init_board_column(board=[]):
    """initialazing the board"""
    if len(board):
        for row in board:
            row.append(0)
    else:
        for _ in range(N):
            board.append([0])
    return board


def queen(board, row, col):
    """adding the queen"""
    board[row][col] = 1


def is_safe(board, row, col):
    """ is the queen safe """
    x = row
    y = col

    for i in range(1, N):
        if (y - i) >= 0:
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            if board[x][y - i]:
                return False
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def coordinate_format(candidates):
    """convert the board into a list of coordinates"""
    holberton = []
    for x, attempt in enumerate(candidates):
        holberton.append([])
        for i, row in enumerate(attempt):
            holberton[x].append([])
            for j, col in enumerate(row):
                if col:
                    holberton[x][i].append(i)
                    holberton[x][i].append(j)
    return holberton


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print('N must be a number')
        sys.exit(1)

    N = int(sys.argv[1])

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    candidates = []
    candidates.append(init_board_column())

    for col in range(N):
        new_candidates = []
        for matrix in candidates:
            for row in range(N):
                if is_safe(matrix, row, col):
                    temp = [line[:] for line in matrix]
                    queen(temp, row, col)
                    if col < N - 1:
                        init_board_column(temp)
                    new_candidates.append(temp)
        candidates = new_candidates

    for item in coordinate_format(candidates):
        print(item)
