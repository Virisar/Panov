def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, (list, tuple)):
        for item in data:
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов
    elif isinstance(data, dict):
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Рекурсивный вызов для ключей
            total_sum += calculate_structure_sum(value)  # Рекурсивный вызов для значений
    elif isinstance(data, str):
        total_sum += len(data)  # Длина строки
    elif isinstance(data, (int, float)):
        total_sum += data  # Суммируем числа

    return total_sum

# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)