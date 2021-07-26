"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

"""
1. first nested loop takes len(L1)*len(L2) steps
2. second loop takes at most len(L1) steps
3. Latter term overwhelmed by form term
4. O(len(L1)*len(L2))
"""


def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
    res = []
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
