calls = 0


def count_calls():
    global calls
    calls += 1


def string_info():
    count_calls()
    stroka = str(input('Введите текст: '))
    len_stroka = len(stroka)
    lower_stroka = stroka.lower()
    upper_stroka = stroka.upper()
    tuple_ = (len_stroka, lower_stroka, upper_stroka)
    return tuple_


def is_contains():
    count_calls()
    string = str(input('Введите строку: ')).upper()
    list_to_search = str(input('ВВедите список: ')).split()
    list_to_search_2 = [i.upper() for i in list_to_search]
    if string in list_to_search_2:
        return True
    else:
        return False


print(string_info())
print(string_info())
print(is_contains())
print(is_contains())
print('Количество вызовов функций: ', calls)
