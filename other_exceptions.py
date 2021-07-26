# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:36:05 2021

@author: Andile Jaden Mbele
"""

try:
    a = int(input('Give me a number: '))
    b = int(input('Give me another number: '))
    print(a/b) # a / b
    print(a + b)
except ZeroDivisionError:
    print('You cannot divide by zero')
except ValueError:
    print('Cannot str to int')
except:
    print('Something is very very wrong')
print('Outside the try statement')


