# Weather API

## Описание
Django-приложение с REST API, которое предоставляет информацию о погоде для указанного города.
Приложение проверяет наличие данных в базе, запрашивает погоду у внешнего API при необходимости и сохраняет её в PostgreSQL.

## Функциональность
- Проверка данных в базе (актуальность ≤ 10 минут)
- Запрос к внешнему API (WeatherStack)
- Сохранение и возврат данных в формате JSON
- Авторизация по ролям:
  - **Менеджер** – может добавлять города
  - **Пользователь** – при регистрации выбирает город и может видеть погоду только по нему

## Технологии
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **Simple JWT** (аутентификация)
- **WeatherStack API** (получение данных о погоде)

## Установка и настройка

### 1. Клонирование репозитория
```sh
git clone <репозиторий>
cd weather_app
```

### 2. Создание и активация виртуального окружения
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Установка зависимостей
```sh
pip install -r requirements.txt
```

### 4. Настройка переменных окружения
Создай файл `.env` в корневой папке и добавь в него:
```env
SECRET_KEY=your_secret_key
DEBUG=True  # False в продакшене
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
API_KEY=your_weatherstack_api_key
```

### 5. Применение миграций и запуск сервера
```sh
python manage.py migrate
python manage.py runserver
```

## Использование API

### 1. Регистрация пользователя
```http
POST /api/register/
```
#### Тело запроса:
```json
{
  "username": "user1",
  "password": "securepassword",
  "role": "user",
  "city": "London"
}
```

### 2. Авторизация (получение токена)
```http
POST /api/token/
```
#### Тело запроса:
```json
{
  "username": "user1",
  "password": "securepassword"
}
```

### 3. Получение данных о погоде
```http
GET /api/weather/
Authorization: Bearer <your_access_token>
```

## Тестирование
Для запуска тестов используй:
```sh
python manage.py test
```

## Документация API
Автоматическая документация доступна по адресу:
```
http://127.0.0.1:8000/swagger/
```

