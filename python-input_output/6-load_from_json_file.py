#!/usr/bin/python3
"""
Creates a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a “JSON file”.

    Args:
        filename: The name of the file to read from.
    Returns:
        The Python object created from the JSON content.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
