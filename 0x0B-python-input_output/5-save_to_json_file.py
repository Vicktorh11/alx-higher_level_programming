#!/usr/bin/python3
"""
Module contains a function that saves object to a text file, using JSON rep
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that saves object to a text file using a JSON representation
    Args:
    filename: filename
    my_obj: object

    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'w', encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
