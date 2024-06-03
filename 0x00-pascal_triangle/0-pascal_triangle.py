#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Pascal's Triangle is a triangular array of binomial coefficients.
    Each number in the triangle is the sum of the two numbers directly
    above it.

    Args:
        n (int): The number of rows in Pascal's Triangle to generate.

    Returns:
        list of list of int: A list of lists representing Pascal's Triangle.
        Each inner list represents a row in the triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


# Example usage:
if __name__ == "__main__":
    print(pascal_triangle(5))
