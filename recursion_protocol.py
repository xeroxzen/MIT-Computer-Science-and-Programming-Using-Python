# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 05:22:44 2021

@author: Xeroxzen
"""

def compare(data_list_1, data_list_2):
    if len(data_list_1) == len(data_list_2):
        data_list_1, data_list_2 = data_list_1, data_list_2
        return data_list_1, data_list_2
    elif len(data_list_1) > len(data_list_2):
        data_list_1 = data_list_2
        data_list_2 = data_list_1
        return data_list_1, data_list_2
    else:
        return compare(data_list_1, data_list_2)