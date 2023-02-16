#!/usr/bin/python3
"""
This module contains a function that reads a file
"""

def read_file(filename=""):
    """function that reads from a file

    Args:
        filename: filename

    Raises
        Excception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        a_file = f.read()
        print(a_file, end='')
