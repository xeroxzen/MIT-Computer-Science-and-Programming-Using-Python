def bubble_sort(L):
	swap = False
	while not swap:
		swap = True
		for j in range(1, len(L)):
			print(L)
			if L[j-1] > L[j]:
				swap = False
				tmp = L[j]
				L[j] = L[j-1]
				L[j-1] = tmp

test = [3, 9, 1, 8, 10, 5, 7, ]
#End here
