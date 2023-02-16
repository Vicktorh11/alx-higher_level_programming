#!/usr/bin/python3
"""
Module contains a function that writes into a txt file
"""


def write_file(filename="", text=""):
    """function that writes to a file

    Args:
    filename: filename
    text: text to write

    Raise
        Exception: when the file can be opened

    """

    with open(filename, 'w', encoding="utf-8")  as a_file:
        return a_file.write(text)
