#!/usr/bin/python3
import json

def from_json_string(my_str):
    """Convertit une chaîne JSON en objet Python."""
    return json.loads(my_str)
