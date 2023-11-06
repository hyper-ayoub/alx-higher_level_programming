#!/usr/bin/python3
'''Method for Only sub class of.'''


def inherits_from(obj, a_class):
    '''he object is an instance of a class that inherited.'''
    return isinstance(obj, a_class) and type(obj) != a_class
