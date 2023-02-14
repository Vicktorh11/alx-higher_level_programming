#!/usr/bin/python3
"""
This module contains the function inherit_from
"""

def inherits_from(obj, a_class):
    """returns true if the object of an instaance class that inherited from the specified class, otherwise false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
