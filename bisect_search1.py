"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""


def bisect_search1(data_list, e):
    """where data_list is list and e is element"""
    if data_list == []:
        return False
    elif len(data_list) == 1:
        return L[0] == e
    else:
        half = len(data_list) // 2
        if data_list(half) > e:
            return bisect_search1(data_list[:half], e)
        else:
            return bisect_search1(data_list[half:], e)


test_list = [1, 2, 3, 5, 7, 9, 18, 27]
