#!/usr/bin/python3
""" This finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (list of int): List of integers to find the peak of
    Returns:
        int or None: Peak of list_of_integers or None if list is empty
    """
    size = len(list_of_integers)

    if size == 0:
        return None

    low, high = 0, size - 1

    while low < high:
        mid = (low + high) // 2


        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
