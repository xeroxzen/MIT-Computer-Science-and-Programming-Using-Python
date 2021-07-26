"""
Created on Mon Jul 26 17:23:16 2021

@author: Andile Jaden Mbele
"""

def fact_iter(n):
	"""Assumes n is an int >= 0

	* computes factorial
	* number of steps:
		* ignore additive constants
		* ignore multplicative constants
	"""
	answer = 1
	while n > 1:
		answer *= n 
		n -= 1
	return answer

