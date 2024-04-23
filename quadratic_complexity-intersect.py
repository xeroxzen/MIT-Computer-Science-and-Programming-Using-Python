"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

"""
1. first nested loop takes len(data_list_1)*len(data_list_2) steps
2. second loop takes at most len(data_list_1) steps
3. Latter term overwhelmed by form term
4. O(len(data_list_1)*len(data_list_2))
"""


def intersect(data_list_1, data_list_2):
    tmp = []
    for e1 in data_list_1:
        for e2 in data_list_2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
