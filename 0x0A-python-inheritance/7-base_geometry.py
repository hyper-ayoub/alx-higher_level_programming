#!/usr/bin/python3
'''Module for Integer validator.'''


class BaseGeometry:
    '''based on 6-base_geometry.py'''
    def area(self):
        '''aises an Exception with the message.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Method that validates value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
             raise ValueError("{} must be greater than 0".format(name))
