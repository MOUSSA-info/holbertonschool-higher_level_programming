#!/usr/bin/python3
"""
Returns a Python object represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python object.

    Args:
        my_str: The JSON string to convert.

    Returns:
        The corresponding Python object.
    """
    return json.loads(my_str)
