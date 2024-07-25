immutable_var = (1, 2, 3, [4, 5], 'Str')
print(immutable_var[0])

# immutable_var[0] = 2      Кортеж является неизменяемым типом данных

mutable_list = ['list', 1, 5, 9]
mutable_list[1] = 4
mutable_list[-1] = 'var'
print(mutable_list)