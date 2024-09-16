class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password




class User:
    """
    Класс пользователя содержащий, атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password




if __name__ == '__main__':
    database = Database

    def check(password):
        check_status = False
        password1 = list(password)
        check_numbers = False
        check_len = False
        registr = False
        if '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '10' in password1:
            check_numbers = True
        if len(password1) >= 8:
            check_len = True
        for letter in password1:
            if letter.isupper():
                registr = True
        if check_numbers == True and check_len == True and registr == True:
            check_status = True
        return check_status

    while True:
        choice = input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация')
        User = (input('Ведите логин: '), password := input('Введите пароль: '), password_2 := input('Повторите пароль: '))
        check_password = False
        while check_password != True:
            if check(password) == False:
                print('Неправильно составленный пароль. Попробуйте другой')
                continue
            elif password != password_2:
                print('Пароли не совпадают!')
                continue
            else:
                check_password = True
        database.add_user(*User)
        break
    print('Ваш пользователь был успешно добавлен.')
