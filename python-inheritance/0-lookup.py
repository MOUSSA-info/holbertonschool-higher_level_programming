#!/usr/bin/python3
"""
This module defines the function lookup.

The purpose of this module is to provide a function that returns
the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings containing the names of the attributes and methods.
    """
    return dir(obj)
