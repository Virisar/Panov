def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Обрабатываем ключи
            total_sum += calculate_structure_sum(value)  # Обрабатываем значения
    elif isinstance(data, (list, tuple, set)):  # Обработка списков, кортежей и множеств
        for item in data:
            total_sum += calculate_structure_sum(item)  # Обрабатываем элементы
    elif isinstance(data, str):
        total_sum += len(data)  # Добавляем длину строки
    elif isinstance(data, (int, float)):
        total_sum += data  # Добавляем число

    return total_sum

# Пример 
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
