#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
