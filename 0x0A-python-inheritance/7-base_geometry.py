#!/usr/bin/python3
"""
This module contains BaseGeometry
"""


class BaseGeometry:
    """A class with public insstance method area and integer validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """check if value is integer and greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
