"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""


def search(L, e):
    """
    1. must only look until reach a number greater than e
    2. O(len(L)) for the loop * O(1) to test if e == L[i]
    3. Overall complexity is O(n) - where n is the len(L)
    """
    for i in range(len(L)):
        if L[i] == e:
            return True
        """You can return the value found ```return e```"""
        elif L[i] > e:
            return False
    return False
