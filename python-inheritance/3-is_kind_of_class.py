#!/usr/bin/python3
"""Defines a function that checks object type or inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or inherited from a_class."""
    return isinstance(obj, a_class)
