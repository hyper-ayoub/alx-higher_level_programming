#!/usr/bin/python3
'''Write to a file utf8.'''


def write_file(filename="", text=""):
    '''write a string to the UTF-8.'''
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
