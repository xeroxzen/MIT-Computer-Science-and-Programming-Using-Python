# linear complexity
def add_digits(s):
	val = 0
	for c in s:
		val += int(c)
	return val
