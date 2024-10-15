class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_names = {line.split(', ')[0] for line in existing_products if line}

        for product in products:
            if product.name in existing_names:
                print(f"Продукт {product} уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(f"{product}\n")


# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str

s1.add(p1, p2, p3)

print(s1.get_products())
