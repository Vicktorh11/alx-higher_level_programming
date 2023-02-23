#!/usr/bin/python3
# base.py
"""Defines a base model class"""
import json
import turtle
import csv


class Base:
    """Represent the base model.

    Represent the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_oblects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
