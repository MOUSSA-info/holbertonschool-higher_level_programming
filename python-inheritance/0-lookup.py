#!/usr/bin/python3
"""
0-lookup module

Defines the function `lookup` which returns
a list of an object's available attributes and methods.
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attribute/method names available for the object.
    """
    return dir(obj)
