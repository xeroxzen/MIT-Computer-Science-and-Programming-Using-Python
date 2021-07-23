"""
Exponential Complexity

1. it's prevalent to think about size of smaller
2. Remember that for a set of size K there are pow(2, k) cases
3. To solve this we need something like pow(2, n-1) + pow(2, n-2) + ... + pow(2, 0)
"""

def gen_subsets(L):
	res = [] # empty list
	if len(L) == 0:
		return [[]] # list of an empty list
	smaller = gen_subsets(L[:-1]) # recursive return all subsets without last element

	extra = L[-1:] # create a list of just the last element
	new = [] # again, empty list
	
	for small in smaller:
		new.append(small + extra) # for all smaller solutions, add one with last element

	return smaller + new
