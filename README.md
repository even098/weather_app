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
git clone https://github.com/even098/weather_app.git
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
Для начала нужно зарегистрироваться в ```https://weatherstack.com/``` и скопировать API ключ. Далее:
Создай файл `.env` в корневой папке и добавь в него:
```env
SECRET_KEY=your_secret_key
DEBUG=True  
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
POST /api/registration/
```
#### Тело запроса:
```json
{
  "username": "user1",
  "password": "securepassword",
  "role": "user",
  "location_name": "London"
}
```
#### Пример ответа:
```json
{
  "username": "user1",
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
#### Пример ответа:
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 3. Добавление города, по которому будет доступна погода
```http
POST /api/weather/add/
```
#### Тело запроса:
```json
{
  "location": "new york"
}
```
#### Пример ответа:
```json
{
    "detail": "Location successfully added.",
    "Location weather": {
        "location": "New York",
        "country": "United States of America",
        "temperature": "-6",
        "feelslike": "-12",
        "weather_descriptions": "Clear",
        "wind_speed": "18",
        "humidity": "50",
        "visibility": "16",
        "updated_at": "2025-02-20T06:16:27.756341Z"
    }
}
```


### 4. Получение данных о погоде
```http
GET /api/weather/
Authorization: JWT <your_access_token>
```
#### Пример ответа:
```json
{
    "data": {
        "location": "Almaty",
        "country": "Kazakhstan",
        "temperature": "1",
        "feelslike": "0",
        "weather_descriptions": "Smoke",
        "wind_speed": "4",
        "humidity": "64",
        "visibility": "3",
        "updated_at": "2025-02-20T06:17:20.488188Z"
    }
}
```
