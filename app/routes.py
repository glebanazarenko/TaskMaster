from flask import Blueprint, jsonify, request
from app.models import Task, User
from app import db

# TODO: Валидация данных на вход. Может схема для входа и выхода.
# TODO: использовать sqlalchemy

main = Blueprint('main', __name__)

# Простой маршрут для проверки работы приложения
@main.route('/')
def index():
    return jsonify({"message": "Welcome to TaskMaster!"})

### Маршруты для работы с задачами (Tasks)

# Получение всех задач
@main.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    tasks_list = [{"id": task.id, "title": task.title, "status": task.status_id} for task in tasks] # TODO: исправить
    return jsonify({"tasks": tasks_list})

# Создание новой задачи
@main.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    import datetime
    new_task = Task(title=data['title'], description=data.get('description'), status_id=1, category_id=2, user_id=2, due_date=datetime.datetime(2024, 9, 30, 18, 0)) # TODO: сделать по выбору
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created!"}), 201

# Обновление задачи
@main.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    db.session.commit()
    return jsonify({"message": "Task updated!"})

# Удаление задачи
@main.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted!"})


### Маршруты для работы с пользователями (Users)

# Получение всех пользователей
@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{"id": user.id, "email": user.email, "role": user.role} for user in users]
    return jsonify({"users": users_list})

# Получение пользователя по ID
@main.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        "id": user.id,
        "email": user.email,
        "role": user.role,
        "created_at": user.created_at
    })

# Создание нового пользователя
@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(email=data['email'], password=data['password'], role=data.get('role', 'user'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 201

# Обновление пользователя
@main.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    user.role = data.get('role', user.role)
    db.session.commit()
    return jsonify({"message": "User updated!"})

# Удаление пользователя
@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted!"})
