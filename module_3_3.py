def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()  # без аргументов
print_params(10)  # только a
print_params(10, 25)  # a и b
print_params(10, 25, False)  # все три параметра
print_params(b=25)  # только b
print_params(c=[1, 2, 3])  # только c

# Распаковка параметров
values_list = [3.14, 'Hello', False]
values_dict = {'a': 42, 'b': 'World', 'c': None}

print_params(*values_list)  # распаковка списка
print_params(**values_dict)  # распаковка словаря

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # вывод: 54.32 'Строка' 42