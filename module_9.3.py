first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка для разницы длин строк, если их длины не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка для сравнения длин строк в одинаковых позициях
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))
print(list(second_result))