#!/usr/bin/python3
"""
Module that defines a custom class with pickle serialization/deserialization.
"""

import pickle


class CustomObject:
    """
    A custom object that can be serialized with pickle.
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)

    def serialize(self, filename):
        """
        Serialize the object to the given file using pickle.

        Args:
            filename (str): The name of the file to write to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            pass  # silently ignore errors during serialization

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return a CustomObject from a file.

        Args:
            filename (str): The name of the file to read from.

        Returns:
            CustomObject or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
