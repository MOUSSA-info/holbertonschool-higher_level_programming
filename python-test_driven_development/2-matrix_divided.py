#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numeric elements.
        TypeError: If rows have different sizes.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    Returns:
        list: New matrix with elements divided and rounded to 2 decimals.
    """
    # Validate matrix structure
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(
                (isinstance(ele, (int, float)) and not isinstance(ele, bool))
                for ele in [num for row in matrix for num in row]
            )):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Check row sizes
    if matrix and not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate divisor
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(x / div, 2) for x in row]
        for row in matrix
    ]
