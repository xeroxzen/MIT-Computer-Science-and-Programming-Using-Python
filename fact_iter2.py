"""
1. number of times around loop is n
2. number of operations inside loop is a constant
3. overall just O(n)
"""

def fact_iter(n):
	prod = 1
	for i in range(1, n + 1):
		prod *= i
	return prod
