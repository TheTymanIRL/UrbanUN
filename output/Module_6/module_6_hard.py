import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = sides
        self.__color = list(color)
        self.filled = False



    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        valid = False
        if r in range(0, 255):
            if g in range(0, 255):
                if b in range(0, 255):
                    valid = True
                    return valid
                else:
                    return valid
            else:
                return valid
        else:
            return valid

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, new_sides):
        if len(new_sides) == self.sides_count:
            for side in new_sides:
                if side > 0:
                    return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    P = 3.14
    def __init__(self, color, circle_len):
        super().__init__(color, circle_len)
        self.__radius = circle_len / 2 * self.P

    def get_square(self):
        S = self.P * (self.__radius ** 2)
        return S

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_len):
        super().__init__(color, side_len)
        self.__sides = [side_len] * self.sides_count

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())