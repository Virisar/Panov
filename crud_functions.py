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
