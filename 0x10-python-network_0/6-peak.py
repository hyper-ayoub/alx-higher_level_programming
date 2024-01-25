#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """
    Write a function that finds a peak in a list of unsorted integers.
    """

    if list_of_integers == []:
        return None
    else:
        peak = 0
        if list_of_integers[0] >= list_of_integers[1]:
            peak = list_of_integers[0]
        elif list_of_integers[-1] >= list_of_integers[-2]:
            peak = list_of_integers[-1]
        else:
            for i in range(1, (len(list_of_integers) - 1)):
                if list_of_integers[i] >= list_of_integers[i - 1]\
                   and list_of_integers[i] >= list_of_integers[i + 1]:
                    peak = list_of_integers[i]
        return peak
