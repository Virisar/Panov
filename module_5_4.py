class House:
    houses_history = []  # Атрибут класса для хранения истории созданных объектов

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(self.name)  # Добавляем название в историю при создании объекта

    @classmethod
    def new(cls, name, number_of_floors):
        house = cls(name, number_of_floors)  # Создаем новый объект
        return house  # Возвращаем созданный объект

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')  # Сообщение об удалении объекта

    def go_to(self, new_floor):
        if not isinstance(new_floor, int):
            raise TypeError("new_floor должен быть целым числом")
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def len(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}; Количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        self._check_house(other)
        return self.number_of_floors == other.number_of_floors

    def __gt__(self, other):
        self._check_house(other)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        self._check_house(other)
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        self._check_house(other)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        self._check_house(other)
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        self._check_house(other)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError("value должен быть целым числом")
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if not isinstance(value, int):
            raise TypeError("value должен быть целым числом")
        self.number_of_floors += value
        return self

    def _check_house(self, other):
        if not isinstance(other, House):
            raise TypeError("other должен быть экземпляром класса House")


# Создание объектов с использованием метода new, и добавляем их в историю
h1 = House.new('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House.new('ЖК Акация', 20)
print(House.houses_history)
h3 = House.new('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2  # Удаляем h2
del h3  # Удаляем h3

print(House.houses_history)  # Печатаем историю после удаления
del h1  # Удаляем h1
