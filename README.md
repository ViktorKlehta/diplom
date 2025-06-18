Применение методов машинного обучения для анализа рынка недвижимости 
Веб-приложение для оценки недвижимотси на Django.

Требования
Python 3.9+
Django 4.2+
Установленный Git (для клонирования)

Установка и запуск

1. Клонируйте репозиторий
bash
git clone https://github.com/ViktorKlehta/diplom.git
cd diplom

2. Создайте и активируйте виртуальное окружение (рекомендуется)

Windows:

bash
python -m venv venv
venv\Scripts\activate

Linux/MacOS:

bash
python3 -m venv venv
source venv/bin/activate

3. Установите зависимости

bash
pip install django

4. Настройте базу данных

Примените миграции:
### bash
### python manage.py migrate

5. Создайте суперпользователя (опционально)

bash
python manage.py createsuperuser
(Для доступа к админке: /admin)

6. Запустите сервер

bash
python manage.py runserver

7. Откройте в браузере

Перейдите по адресу:
http://127.0.0.1:8000
