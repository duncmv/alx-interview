#!/usr/bin/python3
"""square matrix rotation"""


def rotate_2d_matrix(matrix):
    """square matrix 90 degree clockwise rotation"""
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
