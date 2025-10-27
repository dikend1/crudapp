# FastAPI CRUD App

Это простое CRUD-приложение на FastAPI для управления пользователями и задачами. Приложение использует SQLAlchemy для работы с базой данных PostgreSQL, Alembic для миграций и Pydantic для валидации данных.

## Функциональность

- **Пользователи (Users)**: Создание, чтение, обновление и удаление пользователей.
- **Задачи (Tasks)**: Создание, чтение, обновление и удаление задач, связанных с пользователями.
- **Автоматическая документация API**: Доступна по адресу `/docs` (Swagger UI) и `/redoc` (ReDoc).

## Требования

- Python 3.11+
- PostgreSQL база данных
- Установленные зависимости из `requirements.txt`

## Установка и настройка

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/dikend1/crudapp.git
   cd crudapp
   ```

2. **Создайте виртуальное окружение**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows: venv\Scripts\activate
   ```

3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте базу данных**:
   - Убедитесь, что PostgreSQL запущен.
   - Создайте базу данных (например, `crudapp_db`).
   - Обновите настройки в `app/core/config.py` (DATABASE_URL).

5. **Примените миграции базы данных**:
   ```bash
   alembic upgrade head
   ```

## Запуск приложения

Запустите приложение с помощью Uvicorn:
```bash
uvicorn app.main:app --reload
```

Приложение будет доступно по адресу: `http://127.0.0.1:8000`

- **Документация API**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## API Endpoints

### Пользователи

- `GET /users/` - Получить список всех пользователей
- `POST /users/` - Создать нового пользователя
- `GET /users/{user_id}` - Получить пользователя по ID
- `PUT /users/{user_id}` - Обновить пользователя
- `DELETE /users/{user_id}` - Удалить пользователя

### Задачи

- `GET /tasks/` - Получить список всех задач
- `POST /tasks/` - Создать новую задачу
- `GET /tasks/{task_id}` - Получить задачу по ID
- `PUT /tasks/{task_id}` - Обновить задачу
- `DELETE /tasks/{task_id}` - Удалить задачу

## Структура проекта

```
app/
├── main.py              # Точка входа приложения
├── api/
│   └── routes/          # Маршруты API
├── core/
│   └── config.py        # Конфигурация приложения
├── db/                  # Настройки базы данных
├── models/              # SQLAlchemy модели
├── schemas/             # Pydantic схемы
└── services/            # Бизнес-логика
migrations/              # Alembic миграции
requirements.txt         # Зависимости
alembic.ini             # Конфигурация Alembic
```

## Тестирование

Для тестирования API используйте встроенную документацию Swagger UI (`/docs`) или инструменты вроде Postman.

Примеры запросов:

- Создать пользователя:
  ```json
  POST /users/
  {
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```

- Создать задачу:
  ```json
  POST /tasks/
  {
    "title": "Sample Task",
    "description": "This is a sample task",
    "completed": false,
    "user_id": 1
  }
  ```

## Troubleshooting

- **Ошибка подключения к БД**: Проверьте настройки DATABASE_URL в `config.py` и убедитесь, что PostgreSQL запущен.
- **Миграции не применяются**: Убедитесь, что Alembic правильно настроен и база данных доступна.
- **Импорт ошибок**: Убедитесь, что все зависимости установлены (`pip install -r requirements.txt`).
- **Порт занят**: Измените порт в команде запуска Uvicorn (например, `--port 8001`).

## Разработка

- Для внесения изменений в модели обновите файлы в `app/models/` и создайте новые миграции: `alembic revision --autogenerate -m "Описание изменений"`
- После изменений примените миграции: `alembic upgrade head`
- Тестируйте изменения локально перед коммитом.

## Лицензия

Этот проект является открытым и доступен под лицензией MIT.
