"""
1. Computes factorial recursively
2. if you time it, may notice that it runs a bit slower than the iterative version due to function calls.
3. Still O(n) because the number of function calls is lineat in n
4. iterative and recursive factorial implementations are the order of growth
"""

def fact_recur(n):
	"""assumes n >= 0 """
	if n <= 1:
		return 1
	else:
		return n * fact_recur(n - 1)
