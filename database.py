import sqlite3
from datetime import date

DATABASE = 'guestbook.db'

def get_db_connection():
    """Устанавливает соединение с базой данных"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Позволяет обращаться к колонкам по имени
    return conn

def init_db():
    """Создаёт таблицу messages, если её ещё нет"""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at DATE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_messages():
    """Возвращает все сообщения, отсортированные от новых к старым"""
    conn = get_db_connection()
    messages = conn.execute(
        'SELECT * FROM messages ORDER BY created_at DESC'
    ).fetchall()
    conn.close()
    return messages

def add_test_messages():
    """Добавляет тестовые сообщения (только для проверки)"""
    conn = get_db_connection()
    
    # Проверяем, есть ли уже сообщения
    count = conn.execute('SELECT COUNT(*) FROM messages').fetchone()[0]
    
    if count == 0:
        # Добавляем тестовые сообщения
        test_messages = [
            ('Анна', 'Отличный сайт! Спасибо!', '2026-05-28'),
            ('Иван', 'Очень полезный проект', '2026-05-27'),
            ('Мария', 'Жду продолжения!', '2026-05-26'),
            ('Петр', 'Круто!', '2026-05-25')
        ]
        for name, message, created_at in test_messages:
            conn.execute(
                'INSERT INTO messages (name, message, created_at) VALUES (?, ?, ?)',
                (name, message, created_at)
            )
        conn.commit()
        print("✅ Тестовые сообщения добавлены!")
    
    conn.close()
