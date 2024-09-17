class Animal:
    def __init__(self, name, alive = True, fed = False):
        self.alive = alive
        self.fed = fed
        self.name = name

class Plant:
    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible

class Mammal(Animal):
    def eat(self, food):
        if food.food_quolity == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if food.food_quolity == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Flower(Plant):
    food_quolity = False

class Fruit(Plant):
    food_quolity = True



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
