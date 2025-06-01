#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of the Square."""
        # On utilise self.__size car c’est ce qui représente la taille du carré
        return "[Square] {}/{}".format(self.__size, self.__size)
