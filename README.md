# ToDo List API

Минимальный backend-сервис на Django + DRF для управления списком задач (ToDo) с JWT-аутентификацией, Swagger-документацией и возможностью парсинга участников AstanaHub.

---

## 🔧 Функциональность

- **CRUD задач** (`Task`):
  - Создание (`POST /tasks/`):
    - Поля: `title` (обязательно), `description` (опционально), `completed` (по умолчанию `false`)
  - Получение списка (`GET /tasks/`):
    - Фильтрация: `completed`, `title`, `created_at_after/before`, `updated_at_after/before`
    - Поиск по заголовку
  - Просмотр одной задачи (`GET /tasks/{id}/`)
  - Обновление (`PUT/PATCH /tasks/{id}/`)
  - Удаление (`DELETE /tasks/{id}/`)
- **Парсинг участников** AstanaHub Techpark:
  - Команда `python manage.py parse_astanahub`
  - Эндпоинт `POST /tasks/parse/` (только для авторизованных пользователей)
- **Swagger UI** для документации API: `/swagger/`
- **OpenAPI схема** (JSON): `/schema/`
- **JWT-аутентификация**: `POST /auth/login/`, `POST /auth/refresh/`
- **Регистрация**: `POST /auth/register/`
- **Django Admin**: CRUD для `Task` и `Participant`

---

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/your-username/todo-api.git
cd todo-api
```

### 2. Создание `.env`
Скопируйте шаблон и заполните ваши переменные:
```ini
# .env
SECRET_KEY=your_django_secret_key
POSTGRES_DB=todo
POSTGRES_USER=todo_user
POSTGRES_PASSWORD=secret
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

### 3. Запуск контейнеров
```bash
docker compose up --build
```
- **db**: PostgreSQL (порт `POSTGRES_PORT`)
- **web**: Django-сервер на `0.0.0.0:8000`

### 4. Миграции и суперпользователь
Внутри контейнера или локально (если вы не используете Docker):
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 🔍 Использование API

### Аутентификация
- **Регистрация**: `POST /auth/register/`
  ```json
  {
    "username": "user1",
    "email": "user1@example.com",
    "password": "pass1234",
    "password2": "pass1234"
  }
  ```
- **Логин**: `POST /auth/login/`
  ```json
  {
    "username": "user1",
    "password": "pass1234"
  }
  ```
  В ответе приходит `access` и `refresh` токены.
- **Обновление токена**: `POST /auth/refresh/`
  ```json
  { "refresh": "<refresh_token>" }
  ```

Не забывайте передавать в запросах заголовок:
```
Authorization: Bearer <access_token>
```

### CRUD задач
Все эндпоинты `/tasks/` защищены.

- **GET /tasks/** — список задач с фильтрами
- **POST /tasks/** — создать задачу
- **GET /tasks/{id}/** — получить задачу
- **PUT/PATCH /tasks/{id}/** — обновить задачу
- **DELETE /tasks/{id}/** — удалить задачу

Примеры фильтров:
```
GET /tasks/?completed=true
GET /tasks/?title=urgent
GET /tasks/?created_at_after=2025-06-01&created_at_before=2025-06-30
```

### Парсинг участников
- **Команда**: `python manage.py parse_astanahub`
- **API**: `POST /tasks/parse/` — вернёт первые 10 участников, сохранит/обновит их в БД.

---

## 🧰 Администрирование
- Админка Django: `http://localhost:8000/admin/`
- Модели: `Task`, `Participant`

---

## 📄 Лицензия
MIT © Rassul Imyarzhanov
