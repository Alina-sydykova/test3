import sqlite3

def create_db():
    connection = sqlite3.connect('shopping_list.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            bought INTEGER NOT NULL DEFAULT 0,
            quantity INTEGER NOT NULL DEFAULT 1  -- Новый столбец для количества
        )
    ''')
    connection.commit()
    connection.close()

def add_item(name, quantity):
    connection = sqlite3.connect('shopping_list.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO items (name, bought, quantity) VALUES (?, ?, ?)', (name, 0, quantity))
    connection.commit()
    connection.close()

def get_items():
    connection = sqlite3.connect('shopping_list.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    connection.close()
    return items

def update_item(id, bought):
    connection = sqlite3.connect('shopping_list.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE items SET bought = ? WHERE id = ?', (bought, id))
    connection.commit()
    connection.close()

def delete_item(id):
    connection = sqlite3.connect('shopping_list.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM items WHERE id = ?', (id,))
    connection.commit()
    connection.close()

def add_column_to_existing_table():
    connection = sqlite3.connect('shopping_list.db')
    cursor = connection.cursor()
    # Добавляем новый столбец quantity, если он отсутствует
    try:
        cursor.execute('ALTER TABLE items ADD COLUMN quantity INTEGER NOT NULL DEFAULT 1')
    except sqlite3.OperationalError:
        pass  # Если столбец уже существует, ничего не делаем
    connection.commit()
    connection.close()

# Выполняем миграцию для добавления столбца 'quantity'
add_column_to_existing_table()
