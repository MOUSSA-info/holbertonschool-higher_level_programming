#!/usr/bin/python3
"""Définit une classe Rectangle héritant de BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Représente un rectangle avec validation via BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialise un nouveau Rectangle.

        Args:
            width (int): Largeur du rectangle.
            height (int): Hauteur du rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calcule l'aire du rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Retourne la représentation en chaîne du rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
