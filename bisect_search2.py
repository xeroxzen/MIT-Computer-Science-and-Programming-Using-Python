"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""


def bisect_search2(L, e):
    def bisect_search_helper_fn(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:  # nothing left to search for
                return False
            else:
                return bisect_search_helper_fn(L, e, low, mid - 1)
        else:
            return bisect_search_helper_fn(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper_fn(L, e, 0, len(L) - 1)


test_list = [1, 2, 3, 5, 7, 9, 18, 27]
