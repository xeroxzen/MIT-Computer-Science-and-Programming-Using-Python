"""
1. Computes n ** 2 very inefficiently
2. Whenk dealing with nested loops, look at the ranges
3. Nested loops, each iterating n times
"""

def g(n):
	"""assume n >= 0 """
	x = 0
	for i in range(n):
		for j in range(n):
			x += 1
	return x