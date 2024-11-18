from random import choice

# 1. Lambda-функция для сравнения букв
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Используем lambda-функцию для сравнения
result = list(map(lambda a, b: a == b, first, second))
print(result)  # Вывод: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]


# 2. Замыкание для записи в файл
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(f"{data}\n")

    return write_everything


# Пример использования замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# 3. Класс MysticBall
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Пример использования класса MysticBall
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
