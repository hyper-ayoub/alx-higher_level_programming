#!/usr/bin/python3
''' Module for MyList class.'''


class MyList(list):
    '''MyList class.'''
    def print_sorted(self):
        ''' prints the list, but sorted.'''
        print(sorted(self))
