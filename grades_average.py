"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

def avg(grades):
    """Assertions; an example of good defensive programming

    >>> avg([68, 89, 96, 88, 75])
    83.2
    >>> avg([68, 50, 91, 80, 65])
    70.8
    >>> avg([49, 60, 81, 97, 55])
    68.4
    """
    assert not len(grades) != 0, 'no grades data'
    return sum(grades) / len(grades)
