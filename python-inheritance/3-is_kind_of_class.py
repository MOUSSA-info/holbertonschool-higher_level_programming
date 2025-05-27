#!/usr/bin/python3
"""
This module defines the function is_kind_of_class.

The purpose of this module is to provide a function that checks
if an object is an instance of a specified class or a class that inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or inherits from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        bool: True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
