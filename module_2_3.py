my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
print(len(my_list)-1)
print(my_list[0])
while True:
    if i <= len(my_list)-1:
        if my_list[i] >= 0:
            print(my_list[i])
            i += 1
            continue
        else:
            break
