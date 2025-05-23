#!/usr/bin/python3
"""
This module defines the Square class, which represents a square
with a private size attribute.
"""


class Square:
    """
    The Square class defines a square by its size, which is stored
    as a private instance attribute.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of one side of the square.
        """
        self.__size = size
