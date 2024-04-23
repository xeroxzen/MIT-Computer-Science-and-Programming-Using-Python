def bubble_sort(data_list):
	swap = False
	while not swap:
		swap = True
		for j in range(1, len(data_list)):
			print(data_list)
			if data_list[j-1] > data_list[j]:
				swap = False
				tmp = data_list[j]
				data_list[j] = data_list[j-1]
				data_list[j-1] = tmp

test = [3, 9, 1, 8, 10, 5, 7, ]
#End here
