from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Инициализация SQLAlchemy и Flask-Migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Создаем экземпляр Flask-приложения
    app = Flask(__name__)

    # Загружаем конфигурацию из файла config.py
    app.config.from_object('app.config.Config')

    # Инициализация базы данных с приложением
    db.init_app(app)
    
    # Инициализация миграций с приложением и базой данных
    migrate.init_app(app, db)

    # Импортируем и подключаем маршруты
    from app.routes import main
    app.register_blueprint(main)

    return app

# Импортируем модели после создания приложения и базы данных
# Это нужно, чтобы Flask-Migrate знал о существующих моделях для генерации миграций
from app.models import User, Task, TaskStatus, TaskCategory
