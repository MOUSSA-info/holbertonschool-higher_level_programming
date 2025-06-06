#!/usr/bin/python3
"""
Appends a string at the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns the number of characters added.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to append.

    Returns:
        int: Number of characters added.
    """
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
