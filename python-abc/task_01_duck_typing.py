# task_01_duck_typing.py

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculer l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculer le périmètre de la forme."""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Affiche l'aire et le périmètre de la forme donnée."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
