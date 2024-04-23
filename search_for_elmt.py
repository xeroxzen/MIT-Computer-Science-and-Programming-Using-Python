"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""


def search_for_elmt(data_list, e):
    for i in data_list:
        if i == e:
            return True
    return False

