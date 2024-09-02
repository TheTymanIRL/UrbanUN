def ends(i, j):
    endings = ['.com', '.ru', 'net']
    arg = 0
    for u in endings:
        if u in i:
            arg += 1
    for u in endings:
        if u in j:
            arg += 1
    if arg < 2:
        return False
    else:
        return True
"""
Если True, то подходит
Если False, то не подходит
"""


def send_email_2(message, recipient, sender = 'unvirsity.help@gmail.com'):
    if '@' in recipient and '@' in sender:
        if sender != recipient:
            if ends(i = recipient, j = sender) == True:
                if sender == 'unvirsity.help@gmail.com':
                    print("Письмо успешно отправлено с адреса ", sender, ' на адрес ', recipient, '.')
                else:
                    print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', recipient, '.')
            else:
                print("Невозможно отправить письмо с адреса ", sender, ' на адрес ', recipient, '.')
        else:
            print('Нельзя отправить письмо самому себе!')
    else:
        print("Невозможно отправить письмо с адреса ", sender, ' на адрес ', recipient, '.')



send_email_2(
    'Это сообщение для проверки связи',
    'vasyok1337@gmail.com')
send_email_2(
    'Вы видите это сообщение как лучший студент курса!',
    'urban.fan@mail.ru',
    sender='urban.info@gmail.com')
send_email_2(
    'Пожалуйста, исправьте задание',
    'urban.student@mail.ru',
    sender='urban.teacher@mail.uk')
send_email_2(
    'Напоминаю самому себе о вебинаре',
    'urban.teacher@mail.ru',
    sender='urban.teacher@mail.ru')
