grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrick', 'Aaron'}
jornal = []                                         #Создали журнал
students = sorted(list(students))                   #Отсортировали список учеников
i = 0
while i != 5:
    j = str(students[i])                            #Имя ученика
    AG = sum(grades[i][0:]) / len(grades[i])        #Средняя оценка ученика
    list: list[list[str | float]] = [[j, AG]]
    jornal.extend(list)
    i += 1
jornal = dict(jornal)
print(jornal)

