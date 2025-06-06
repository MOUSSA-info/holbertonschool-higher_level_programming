#!/usr/bin/python3
"""
Basic Serialization Module
Provides functions to serialize a dictionary to JSON and
deserialize it back to a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary and saves it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the file where the JSON will be saved.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file into a dictionary.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
