my_dict = {'Artem': 4018, 'Asya': 2911}
print(my_dict)
print(my_dict.get('Artem'))
print(my_dict.get('Andrey'))
my_dict.update({'Andrey': 2020,
                'Sanya': 1074})
print(my_dict.pop('Asya'))
print(my_dict)

my_set = {1, 4, 6, 1, True, 2, 4, 6, 5, (3, 5, 'list')}
my_set.add(10)
my_set.add(15)
my_set.discard(4)
print(my_set)
