# БЛОЖ

Моя маленькая личная разработка

## Запуск


## Запуск контейнера в проде

Перед началом необходимо создать файлы окружения .env.prod и .env.prod.db

###.env.prod
```
FLASK_APP=project/__init__.py
FLASK_ENV=production
DATABASE_URL=postgresql://****:****@db:5432/*****
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
APP_FOLDER=/home/app/web
SECRET_KEY='******'
```

###.env.prod.db
```
POSTGRES_USER=*****
POSTGRES_PASSWORD=*****
POSTGRES_DB=*****
```

Запуск
```
$ sudo docker-compose up -d --build
```

Выключение
```
$ sudo docker-compose down
```

Обязательно посетить для создания базы данных
```
ip:port/api/protect/create_db
```