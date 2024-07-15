#!/usr/bin/python3
"""
Solution for NQueens Problem
"""

import sys


def print_usage():
	"""Function to print the number of Nqueens"""
	print("Usage: nqueens N")
	sys.exit(1)


def print_error(message):
	"""Usage of n_queens custom error"""
	print(message)
	sys.exit(1)


def is_safe(board, row, col):
	"""check this row on the left side"""
	for i in range(col):
		if board[row][i] == 1:
			return False

	# Check the upper diagnol on the left side
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False
	# Check the lower diagnol on the left side
	for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False
	return True


def solve_nqueens_util(board, col, solutions):
	"""Function to solve the NQueens problem"""
	if col >= len(board):
		solutions.append([[i, board[i].index(1)]
					for i in range(len(board))])
		return True
	res = False
	for i in range(len(board)):
		if is_safe(board, i , col):
			board[i][col] = 1
			solve_nqueens_util(board, col + 1, solutions)
			board[i][col] = 0
	return res


def print_solution(board):
	"""Function to print the solution"""
	solution = []
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == 1:
				solution.append([i, j])
	print(solution)


def solve_nqueens(n):
	"""Helper function"""
	board = [[0 for _ in range(n)] for _ in range(n)]
	solutions = []
	solve_nqueens_util(board, 0, solutions)
	for solution in solutions:
		print(solution)

def main():
    if len(sys.argv) != 2:
        print_usage()
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error("N must be a number")
    if N < 4:
        print_error("N must be at least 4")
    solve_nqueens(N)

if __name__ == "__main__":
    main()