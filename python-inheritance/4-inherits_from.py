#!/usr/bin/python3
"""
Module 4-inherits_from
Contains function inherits_from that returns True if the object is
an instance of a subclass (strict) of a given class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class
    (but not an instance of a_class itself), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
