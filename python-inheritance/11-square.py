#!/usr/bin/python3
"""Définit une classe Square héritant de Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Représente un carré avec validation via Rectangle."""

    def __init__(self, size):
        """
        Initialise un nouveau Carré.

        Args:
            size (int): Taille du carré.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Retourne la représentation en chaîne spécifique au carré."""
        return f"[Square] {self.__size}/{self.__size}"
