def h(n):
	"""assumes n an int >= 0"""
	answer = 0
	s = str(n)
	for c in s:
		answer += int(c)
	return answer
