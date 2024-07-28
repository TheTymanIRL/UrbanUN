import random
numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def random_number():
    result = random.choice(numbers)
    return result
num = random_number()
print('Число из первой вставки: ', num)
def choice_the_password(num):
    numbers = []
    for i in range(1, num):
        for j in range(1, num):
            sum_ = i + j
            if int(num) % int(sum_) == 0 and int(i) != int(j):
                if str(i) and str(j) not in numbers:
                    numbers.append(str(i))
                    numbers.append(str(j))
    numbers = ''.join(numbers)
    return numbers
print('Пароль для числа: ', choice_the_password(num))
