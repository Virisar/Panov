import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создаём таблицу Users, если она ещё не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Удаляем все записи из таблицы для целей тестирования
cursor.execute("DELETE FROM Users")

# Вставляем 10 записей в таблицу Users
users_data = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

# Вставляем записи
cursor.executemany('''
INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
''', users_data)

# Удаляем пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = 6")

# Подсчет общего количества записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0] or 0  # Используем 0, если нет записей

# Вычисляем средний баланс
if total_users > 0:
    average_balance = all_balances / total_users
else:
    average_balance = 0

# Выводим средний баланс на консоль
print(f'Средний баланс всех пользователей: {average_balance:.2f}')

# Закрываем соединение с базой данных
conn.commit()
conn.close()
