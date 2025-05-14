#!/usr/bin/python3
"""Divides all elements of a matrix by a divisor."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): Matrix of integers/floats.
        div (int/float): Divisor (non-zero).

    Returns:
        list: New matrix with elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is invalid or rows have different sizes.
        ZeroDivisionError: If div is zero.
    """
    # Validate matrix structure and content
    if not (isinstance(matrix, list) and
            all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)) or isinstance(elem, bool):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    # Check row size consistency
    if matrix:
        row_size = len(matrix[0])
        if any(len(row) != row_size for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide and round elements
    return [[round(elem / div, 2) for elem in row] for row in matrix]
