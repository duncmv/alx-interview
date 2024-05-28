#!/usr/bin/env python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists representing Pascals triangle of n"""
    try:
        if n <= 0:
            return []
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            prev = triangle[i - 1]
            row.extend([prev[j - 1] + prev[j] for j in range(1, i)])
            row.append(1)
            triangle.append(row)
    except Exception as e:
        return []
    return triangle
