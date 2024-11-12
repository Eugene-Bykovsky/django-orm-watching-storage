# Пульт охраны банка

Этот проект реализует систему контроля доступа для охраны банка. Система позволяет отслеживать активные пропуска, фиксировать посещения и предоставлять данные о не завершенных визитах. Проект написан на Django и включает модели для учета информации о пропусках и посещениях.

### Как установить

Python3 должен быть уже установлен. 

1. Клонируйте репозиторий на локальный компьютер.

```
git@github.com:Eugene-Bykovsky/django-orm-watching-storage.git
```

2. Установите зависимости командой:

```
pip install -r requirements.txt
```

3. Настройте переменные окружения. Создайте файл .env в корневой директории проекта и добавьте следующие переменные:

DATABASE_ENGINE: Движок базы данных (например, django.db.backends.postgresql).  
DATABASE_HOST: Хост базы данных (например, localhost).  
DATABASE_PORT: Порт базы данных (например, 5432 для PostgreSQL).  
DATABASE_NAME: Имя базы данных.  
DATABASE_USER: Имя пользователя базы данных.  
DATABASE_PASSWORD: Пароль для подключения к базе данных.  
DEBUG: Уровень отладки (например, True для режима разработки и False для продакшн).  

Пример содержимого .env:

DATABASE_ENGINE=django.db.backends.postgresql  
DATABASE_HOST=localhost  
DATABASE_PORT=5432  
DATABASE_NAME=bank_security  
DATABASE_USER=your_user  
DATABASE_PASSWORD=your_password  
DEBUG=True  

4. Запуск проекта  
После установки зависимостей и настройки переменных окружения запустите сервер:

```
python manage.py runserver
```

### Цель проекта

Код написан в образовательных целях.