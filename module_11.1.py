# №1 работа с requests

import requests

# Отправка GET-запроса
response = requests.get('https://api.github.com')
# Вывод JSON-ответа
print(response.json())
# Получение статуса ответа
print(response.status_code)
# Вывод заголовков ответа
print(response.headers)

# №2 работа с pandas as pd

import pandas as pd

# Чтение данных из CSV файла
data = pd.read_csv('data.csv')

# Вывод первых 5 строк
print("Первые 5 строк данных:")
print(data.head())

# Описание статистики данных
print("\nСтатистическое описание данных:")
print(data.describe())

# Группировка данных по столбцу и суммирование
print("\nГруппировка данных по 'column_name' и суммирование:")
print(data.groupby('column_name').sum())

# №3  работа с numpy as np

import numpy as np

# Создание массива
array = np.array([1, 2, 3, 4])
# Выполнение арифметической операции
squared = array ** 2
print(squared)
# Вычисление среднее значение
mean_value = np.mean(array)
print(mean_value)
# Создание двумерного массива
matrix = np.array([[1, 2], [3, 4]])
print(np.linalg.inv(matrix))  # Обратная матрица
