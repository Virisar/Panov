class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

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
        if value > 0:
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def _check_house(self, other):
        if not isinstance(other, House):
            raise TypeError("other должен быть экземпляром класса House")


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)
