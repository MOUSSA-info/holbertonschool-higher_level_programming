#!/usr/bin/python3
"""
Defines a Student class with optional filtering for JSON serialization.
"""

class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned.

        Args:
            attrs (list): Optional list of attribute names to include.

        Returns:
            dict: Dictionary representation of the instance.
        """
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__
