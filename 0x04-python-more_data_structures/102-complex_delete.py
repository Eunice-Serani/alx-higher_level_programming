#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for a, b in tmp.items():
        if value == b:
            my_dict.pop(a)
    return my_dict
