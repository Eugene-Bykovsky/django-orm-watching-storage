# Пульт охраны банка

Этот проект реализует систему контроля доступа для охраны банка. Система позволяет отслеживать активные пропуска, фиксировать посещения и предоставлять данные о не завершенных визитах. Проект написан на Django и включает модели для учета информации о пропусках и посещениях.

## Как установить

Python3 должен быть уже установлен. 

1. Клонируйте репозиторий на локальный компьютер.

   ```
   git@github.com:Eugene-Bykovsky/django-orm-watching-storage.git
   ```

2. Установите виртуальное окружение и активируйте его: 

    ```
    python3 -m venv venv  
    source venv/bin/activate  
    ```

3. Установите зависимости командой:
    
    ```
    pip install -r requirements.txt
    ```

4. Настройте переменные окружения. Создайте файл .env в корневой директории проекта и добавьте следующие переменные:

   * DATABASE_ENGINE: Движок базы данных (например, django.db.backends.postgresql).
   * DATABASE_HOST: Хост базы данных (например, localhost).
   * DATABASE_PORT: Порт базы данных (например, 5432 для PostgreSQL).
   * DATABASE_NAME: Имя базы данных.
   * DATABASE_USER: Имя пользователя базы данных.
   * DATABASE_PASSWORD: Пароль для подключения к базе данных.
   * SECRET_KEY = Секретный ключ джанго
   * DEBUG: Уровень отладки (например, True для режима разработки и False для продакшн).
   
   _**Пример содержимого .env:**_

   * export DATABASE_ENGINE=django.db.backends.postgresql
   * export DATABASE_HOST=localhost
   * export DATABASE_PORT=5432
   * export DATABASE_NAME=bank_security
   * export DATABASE_USER=your_user
   * export DATABASE_PASSWORD=your_password
   * export SECRET_KEY=SECRET_KEY
   * export DEBUG=True
   * export ALLOWED_HOSTS=localhost, 127.0.0.1

## Запуск проекта  
После установки зависимостей и настройки переменных окружения запустите сервер:

   ```
   python manage.py runserver
   ```

## Цель проекта

Код написан в образовательных целях.