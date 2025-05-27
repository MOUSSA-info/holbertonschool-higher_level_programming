#!/usr/bin/python3
"""
This module defines the MyList class.

The purpose of this module is to provide a custom list class
that inherits from the built-in list and adds a method to print
the list sorted in ascending order.
"""


class MyList(list):
    """
    MyList is a subclass of list that provides a method to print
    the list elements in ascending sorted order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method does not modify the original list.
        """
        print(sorted(self))
