#!/usr/bin/python3
"""
This module contains a function `rotate_2d_matrix` that rotates
a given n x n 2D matrix by 90 degrees clockwise.

The rotation is achieved in two steps:
1. Transposing the matrix: This step converts rows into columns.
2. Reversing each row: After transposition, each row is reversed to complete
   the 90-degree clockwise rotation.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
    matrix (list of list of int): The n x n 2D matrix to rotate.

    Returns:
    None: The matrix is modified in place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
