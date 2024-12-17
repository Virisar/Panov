import sqlite3


def initiate_db():
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()

    # Создаём таблицу Products, если она ещё не создана
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')

    # Создаём таблицу Users, если она ещё не создана
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL DEFAULT 1000
    )
    ''')

    # Пополнение таблицы Products 4 записями
    products_data = [
        ('Product1', 'Описание продукта 1', 100),
        ('Product2', 'Описание продукта 2', 200),
        ('Product3', 'Описание продукта 3', 300),
        ('Product4', 'Описание продукта 4', 400)
    ]

    cursor.executemany('''
    INSERT INTO Products (title, description, price) VALUES (?, ?, ?)
    ''', products_data)

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()

    cursor.execute("SELECT title, description, price FROM Products")
    products = cursor.fetchall()

    conn.close()
    return products


def add_user(username, email, age):
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)
    ''', (username, email, age, 1000))

    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ?", (username,))
    exists = cursor.fetchone()[0] > 0  # Возвращает True, если пользователь существует

    conn.close()
    return exists