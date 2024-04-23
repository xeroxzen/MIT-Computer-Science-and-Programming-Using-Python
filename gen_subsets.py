"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

"""
Exponential Complexity

1. it's prevalent to think about size of smaller
2. Remember that for a set of size K there are pow(2, k) cases
3. To solve this we need something like pow(2, n-1) + pow(2, n-2) + ... + pow(2, 0)
"""


def gen_subsets(data_list):
    res = []  # empty list
    if len(data_list) == 0:
        return [[]]  # list of an empty list
    # recursive return all subsets without last element
    smaller = gen_subsets(data_list[:-1])

    extra = data_list[-1:]  # create a list of just the last element
    new = []  # again, empty list

    for small in smaller:
        # for all smaller solutions, add one with last element
        new.append(small + extra)

    return smaller + new
