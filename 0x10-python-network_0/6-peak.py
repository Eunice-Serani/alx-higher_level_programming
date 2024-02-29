#!/usr/bin/python3
""" This finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    neat_e = size
    neat = size // 2

    if size == 0:
        return None

    while True:
        neat_e = neat_e // 2
        if (neat < size - 1 and
                list_of_integers[neat] < list_of_integers[neat + 1]):
            if neat_e // 2 == 0:
                neat_e = 2
            neat = neat + neat_e // 2
        elif neat_e > 0 and list_of_integers[neat] < list_of_integers[neat - 1]:
            if neat_e // 2 == 0:
                neat_e = 2
            neat = neat - neat_e // 2
        else:
            return list_of_integers[neat]
