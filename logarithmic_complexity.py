"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

"""
What we know.

1. Only have to look at the loop as there are  no function calls
2. Within while loop, constant number of steps
3. How many times through loop?
    i. how many times can one divide i by 10
    ii. O(log(i)), log base 10 for the size of i
    Nugget: It is linear in the number of digits in n, but log in the size of n and since we decided to measure this in the size of the input it is logarithmic 
"""


def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    res = ''
    while i > 0:
        res = digits[i % 10] + res
        i = i // 10
    return res
