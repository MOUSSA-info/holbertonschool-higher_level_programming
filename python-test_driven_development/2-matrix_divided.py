#!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: Si la matrice contient des éléments non numériques.
        TypeError: Si les lignes ont des tailles différentes.
        TypeError: Si div n'est pas un nombre.
        ZeroDivisionError: Si div est 0.
    Returns:
        list: Nouvelle matrice avec les éléments divisés arrondis à 2 décimales.
    """
    # Validation de la structure de la matrice
    if (not isinstance(matrix, list) 
            or not all(isinstance(row, list) for row in matrix)
            or not all(
                (isinstance(ele, (int, float)) and not isinstance(ele, bool))
                for ele in [num for row in matrix for num in row]
            )):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification de la taille des lignes
    if matrix and not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validation du diviseur
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
