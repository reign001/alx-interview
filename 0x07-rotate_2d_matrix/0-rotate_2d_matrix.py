#!/usr/bin/python3
"""
Rotate  Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90  clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    k = len(matrix)
    for i in range(int(k / 2)):
        y = (k - i - 1)
        for j in range(i, y):
            x = (k - 1 - j)
            # current number
            rot = matrix[i][j]
            # change top for left
            matrix[i][j] = matrix[x][i]
            # change left for bottom
            matrix[x][i] = matrix[y][x]
            # change bottom for right
            matrix[y][x] = matrix[j][y]
            # change right for top
            matrix[j][y] = rot
