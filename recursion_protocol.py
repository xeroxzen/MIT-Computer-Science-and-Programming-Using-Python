# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 05:22:44 2021

@author: Xeroxzen
"""

def compare(L1, L2):
    if len(L1) == len(L2):
        L1, L2 = L1, L2
        return L1, L2
    elif len(L1) > len(L2):
        L1 = L2
        L2 = L1
        return L1, L2
    else:
        return compare(L1, L2)