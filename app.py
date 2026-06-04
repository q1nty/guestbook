from flask import Flask, render_template
from database import init_db, get_all_messages, add_test_messages

# Создаём приложение Flask
app = Flask(__name__)

# Инициализируем базу данных (создаём таблицу)
init_db()

# Добавляем тестовые сообщения (чтобы было что показывать)
add_test_messages()

@app.route('/')
def index():
    """Главная страница - показывает все сообщения"""
    messages = get_all_messages()
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
