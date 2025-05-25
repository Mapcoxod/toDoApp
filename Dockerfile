# Dockerfile
FROM python:3.11-slim

# Не сохранять байт-код, выводить логи сразу
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Скопировать список зависимостей и установить их
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Скопировать весь код в контейнер
COPY . /app/

# Сделать manage.py исполняемым
RUN chmod +x manage.py