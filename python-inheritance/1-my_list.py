#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A subclass of list that prints the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
