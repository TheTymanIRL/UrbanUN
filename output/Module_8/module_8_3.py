class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message

# Класс Car содержит информацию о автомобиле и его VIN номер
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
            if not isinstance(vin_number, int):
                raise IncorrectVinNumber(f'Некорректный тип vin номера')
            if not 1000000 <= vin_number <= 9999999:
                raise IncorrectVinNumber(f'Неверный диапозон для vin номера')
            else:
                return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumber('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumber('Неверная длина номера')
        else:
            return True

    def get_model(self):
        return self.model

    def get_vin(self):
        return self.__vin

    def get_numbers(self):
        return self.__numbers

    def set_model(self, model):
        self.model = model

    def set_vin(self, vin):
        if self.__is_valid_vin(vin):
            self.__vin = vin
        else:
            raise IncorrectVinNumber(f'Неверный vin номера')

    def set_numbers(self, numbers):
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
        else:
            raise IncorrectCarNumber(f'Неверный номер {numbers}')



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')