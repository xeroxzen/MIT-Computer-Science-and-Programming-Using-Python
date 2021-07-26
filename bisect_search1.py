"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""


def bisect_search1(L, e):
    """where L is list and e is element"""
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L) // 2
        if L(half) > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)


test_list = [1, 2, 3, 5, 7, 9, 18, 27]
