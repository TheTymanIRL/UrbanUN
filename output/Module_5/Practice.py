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
    while True:
        choice = int(input('Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация'))
        if choice == 1:
            login = input('Ведите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                print('ОК')
        if choice == 2:
            user = User(input('Ведите логин: '), password := input('Введите пароль: '), password_2 := input('Повторите пароль: '))
            if password != password_2:
                exit()
            database.add_user(user.username, user.password)
        print('Ваш пользователь был успешно добавлен')
