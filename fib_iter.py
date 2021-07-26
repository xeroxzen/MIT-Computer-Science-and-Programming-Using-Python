"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

"""
Complexity of the iterative fibonacci
1. Best case: O(1)
2. Worst case: O(1) + O(n) + O(1) => O(n)
"""

def fib_iter(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		fib_i = 0
		fib_ii = 1
		for i in range(n - 1):
			tmp = fib_i
			fib_i = fib_ii
			fib_ii = tmp + fib_ii
		return fib_ii
