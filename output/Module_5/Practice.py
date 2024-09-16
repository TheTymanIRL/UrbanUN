class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database
    user = User(input('Логин: '), input('Пароль: '), input('Повтор пароля: '))
    database.add_user(user.username, user.password)
