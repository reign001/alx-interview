#!/usr/bin/python3
"""
0. Pascal's Triangle
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    res = []
    if n > 0:
        for m in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, m + 1):
                level.append(C)
                C = C * (m - j) // j
            res.append(level)
    return res