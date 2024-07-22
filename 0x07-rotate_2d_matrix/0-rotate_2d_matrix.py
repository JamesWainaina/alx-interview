#!/usr/bin/python3
"""
Rotating a 2d array
"""


def rotate_2d_matrix(matrix):
    """
    Function for rotating a 2d array
    """
    N = len(matrix)

    for r in range(N):
        for c in range(r):
            # first you transpose then you reverse
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for r in matrix:
        r.reverse()
