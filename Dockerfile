FROM python:3.12-slim

# Установка зависимостей
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копирование исходников
COPY . /app
WORKDIR /app

# Открытие порта
EXPOSE 5000

# Запуск Flask-приложения
CMD ["flask", "run", "--host=0.0.0.0"]
