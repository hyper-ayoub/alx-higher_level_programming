#!/usr/bin/python3
''' Module for lookup methode.'''


def lookup(obj):
    ''' look up object attributes and method .
    Args:
        obj (object): the object to list

    Return:
        list: the list of attributes
    '''
    return dir(obj)
