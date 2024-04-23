"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""


def search(data_list, e):
    """
    1. must only look until reach a number greater than e
    2. O(len(L)) for the loop * O(1) to test if e == L[i]
    3. Overall complexity is O(n) - where n is the len(L)
    """
    for i in range(len(data_list)):
        if data_list[i] == e:
            return True
        elif data_list[i] > e:
            return False
        return False
