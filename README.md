# Проект "telegram_bot_project"

**Описание:**

Этот проект разработан с использованием Django и Django REST framework для создания API и включает в себя функции регистрации пользователей, аутентификации, отправки сообщений и интеграции с Telegram для генерации токенов.

**Требования:**

Для запуска проекта на вашем локальном компьютере вам понадобятся следующие зависимости:

- Python 3.11
- Django 4.2.6
- Django REST framework
- python-telegram-bot

**Установка:**

1. Склонируйте репозиторий на свой локальный компьютер:

git clone https://github.com/yourusername/yourproject.git

2. Создайте виртуальное окружение и активируйте его:

```bash
python -m venv venv
source venv/bin/activate (в Linux/Mac)
venv\Scripts\activate (в Windows)
```
Установите зависимости:
pip install -r requirements.txt

Примените миграции:
python manage.py migrate

Создайте суперпользователя для доступа к админ-панели:
python manage.py createsuperuser

Запустите сервер разработки:
python manage.py runserver

Использование:
Регистрация пользователя:
Чтобы зарегистрировать нового пользователя, отправьте POST-запрос на /register/, передав параметры username, password, first_name, last_name и email. Пример:

curl -X POST http://localhost:8000/register/ -d "username=user1&password=123456&first_name=John&last_name=Doe&email=user1@example.com"
Аутентификация пользователя:
Для аутентификации пользователя отправьте POST-запрос на /login/, передав параметры username и password. В ответ вы получите токен аутентификации. Пример:

curl -X POST http://localhost:8000/login/ -d "username=user1&password=123456"
Генерация токена Telegram:
Чтобы сгенерировать токен Telegram для пользователя, отправьте GET-запрос на /generate_telegram_token/. Токен будет сгенерирован и связан с пользователем. Пример:

curl -X GET http://localhost:8000/generate_telegram_token/ -H "Authorization: Token YOUR_AUTH_TOKEN"
Отправка сообщения:
Чтобы отправить сообщение, отправьте POST-запрос на /send_message/, передав параметр text с текстом сообщения. Пример:

curl -X POST http://localhost:8000/send_message/ -H "Authorization: Token YOUR_AUTH_TOKEN" -d "text=Hello, world!"
Получение сообщений пользователя:
Чтобы получить все сообщения пользователя, отправьте GET-запрос на /get_user_messages/. Пример:
curl -X GET http://localhost:8000/get_user_messages/ -H "Authorization: Token YOUR_AUTH_TOKEN"

Получение всех сообщений:
Чтобы получить все сообщения всех пользователей, отправьте GET-запрос на /get_messages/. Пример:
curl -X GET http://localhost:8000/get_messages/ -H "Authorization: Token YOUR_AUTH_TOKEN"

