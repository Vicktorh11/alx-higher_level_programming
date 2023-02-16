#!/usr/bin/python3
"""
Module contains a function that creates an object from JSON file
"""

import json

def load_from_json_file(filename):
    """Functiont that creates an object from JSON file

    Args:
        filename: filename
    
    Raises:
        Exception: when the object cant't be encoded
    """
    with open(filename, 'r', encoding="utf-8") as a_file:
        return json.load(a_file)
