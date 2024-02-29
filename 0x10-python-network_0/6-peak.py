#!/usr/bin/python3
""" This finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (list of int): List of integers to find peak of
    Returns:
        int or None: Peak of list_of_integers or None if list is empty
    """
    size = len(list_of_integers)

    if size == 0:
        return None

    mid_range = size

    mid = size // 2

    while True:
        mid_range = mid_range // 2

        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_range // 2 == 0:
                mid_range = 2
            mid = mid + mid_range // 2
        elif mid_range > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_range // 2 == 0:
                mid_range = 2
            mid = mid - mid_range // 2
        else:
            return list_of_integers[mid]
