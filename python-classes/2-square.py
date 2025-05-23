#!/usr/bin/python3
"""
This module defines the Square class, which represents a square
and validates the size provided at instantiation.
"""


class Square:
    """
    The Square class defines a square by its size, ensuring
    the size is a non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of one side of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
