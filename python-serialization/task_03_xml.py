#!/usr/bin/python3
"""
Module for serializing and deserializing dictionaries using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The output XML file name.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        elem = ET.SubElement(root, key)
        elem.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a Python dictionary.

    Args:
        filename (str): The input XML file name.

    Returns:
        dict: The deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for elem in root:
        result[elem.tag] = elem.text

    return result
