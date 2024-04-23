"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

# Algorithm complexity


def isSubset(data_list_1, data_list_2):
    for e1 in data_list_1:
        matched = False
        for e2 in data_list_2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
