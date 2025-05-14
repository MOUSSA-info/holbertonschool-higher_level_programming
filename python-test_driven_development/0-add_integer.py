#!/usr/bin/python3


"""
This module provides a function
to add two integers after casting
floats to integers. Handles type
validation and returns integer result.
"""


def add_integer(a, b=98):


    """Adds two integers after casting floats.
    Returns their sum. Raises TypeErrors.
    """


    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
