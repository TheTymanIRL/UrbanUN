import threading
import time
import random
import queue
class Table():
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time_to_eat = random.randint(3, 10)
        print(f'{self.name} сел(-а) за стол номер {self.table.number}')
        time.sleep(time_to_eat)
        print(f'{self.name} покушал(-а) и ушёл(ушла)')
class Cafe():
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrivals(self, *guests):
        for guest in guests:
            if any(table.guest is None for table in self.tables):
                for table in self.tables:
                    if table.guest is None:
                        table.guest = guest
                        guest.table = table
                        guest.start()
                        print(f'{guest.name} сел(-а) за стол номер {table.number}')
                        break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty() and table.guest is None:
                        guest = self.queue.get()
                        table.guest = guest
                        guest.table = table
                        print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrivals(*guests)
# Обслуживание гостей
cafe.discuss_guests()