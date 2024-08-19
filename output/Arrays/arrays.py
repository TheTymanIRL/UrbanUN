from output.module_4.softfunc import bubble_sort, selection_sort

data_1 = [9, 5, 1, 3, 0, 6, 8, 3]
data_2 = [9, 5, 1, 3, 0, 6, 8, 3, 17, 28, 30]
data_3 = [9, 5, 1, 3, 0, 6, 8, 3, 17, 28, 30, 73, 9, 27, 65]

print(bubble_sort(data_1))
print(bubble_sort(data_2))
print(bubble_sort(data_3))

print(selection_sort(data_1))
print(selection_sort(data_2))
print(selection_sort(data_3))
