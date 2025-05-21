#!/usr/bin/python3
class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        self.__size = size  # Private attribute using name mangling
