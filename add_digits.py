"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

# linear complexity


def add_digits(s):
    val = 0
    for c in s:
        val += int(c)
    return val
