"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""


def bisect_search2(data_list, e):
    def bisect_search_helper_fn(data_list, e, low, high):
        if high == low:
            return dat_list[low] == e
        mid = (low + high) // 2
        if dat_list[mid] == e:
            return True
        elif data_list[mid] > e:
            if low == mid:  # nothing left to search for
                return False
            else:
                return bisect_search_helper_fn(data_list, e, low, mid - 1)
        else:
            return bisect_search_helper_fn(data_list, e, mid + 1, high)
    if len(data_list) == 0:
        return False
    else:
        return bisect_search_helper_fn(data_list, e, 0, len(L) - 1)
