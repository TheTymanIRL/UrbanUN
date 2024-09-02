def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = [1.52, False, (1, 2, 3)]
valuel_dict = {'a': True,
               'b': [2, 4, 5],
               'c': 'English'
               }
print_params(*values_list)
print_params(**valuel_dict)

values_list_2 = ['Dentist', 41.3]
print_params(*values_list_2)
