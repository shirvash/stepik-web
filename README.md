# Проект для курса по web-технологиям на Stepik.org
<a href="https://stepik.org/course/154/info">Web-технологии</a>


## Локальная установка 
1. Клонируем репозиторий
```
cd git
https://github.com/shirvash/Stepik_web.git
cd Stepik_web
```
2. Устанавливаем зависимости
```
python -m venv env
. env/bin/activate
pip install -r requirements.txt
```
3. Устанавливаем миграции и создаём пользователя 
```
python manage.py migrate
# Создаём пользователя админа
python manage.py createsuperuser
username: admin
password: ********
```

4. Запускаем приложение
```
python manage.py runserver
# Админ http://127.0.0.1:8000/admin
```

## Enjoy it!
