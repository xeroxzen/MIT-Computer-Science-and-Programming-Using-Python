"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

"""
1. Computes n ** 2 very inefficiently
2. Whenk dealing with nested loops, look at the ranges
3. Nested loops, each iterating n times
"""

def g(n):
	"""assume n >= 0 """
	x = 0
	for _ in range(n):
		for _ in range(n):
			x += 1
	return x
