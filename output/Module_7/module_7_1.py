from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.products_list = []

    def get_products(self):
        file = open(self.__file_name, 'r')
        self.products_list = file.read()
        file.close()
        return self.products_list

    def add(self, *products):
        s1.get_products()

        for new_product in products:
            if Product.__str__(new_product) in self.products_list:
                print(f'Продукт {Product.__str__(new_product)} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(Product.__str__(new_product)+'\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())