"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

# Algorithm complexity


def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
