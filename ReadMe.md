# REST API для блога

## Описание
Реализация REST API для системы комментариев блога

## Установка

```console
git clone https://github.com/expmax85/blog
cd blog/
python3 -m pip install -r requirements.txt
```
Cоздать файл `.env` и заполнить его по шаблону файла `.env.template`, или переименовать `.env.template`.
В случае использования иной БД, указанной в шаблоне, установить данную БД и заполнить все поля файла `.env`
```console
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```

> [!NOTE]
> При установке в OS Windows использовать `python` вместо `python3`.

### Тестовые данные
Если необходимо, можно заполнить проект тестовыми данными, выполнив следующие команды перед командой `runserver`:
```console
python manage.py loaddata fixtures/posts.json
python manage.py loaddata fixtures/comments.json
```

## Docker

Чтобы запустить проект через docker-compose, необходимо переименовать файл `.env-docker.template` в `.env`, внести правки при необходимости в нем и файле docker-compose.
В контейнере используются python3.8 и postgres последней версии.
И выполнить поочередно следующие команды:
```console
docker compose build
docker compose up
```

## Добавление статьи

##### request
|type|url|data |
|----|---|-----------|
|POST |/api/posts/|`{"title": "post title","content": "post content", "owner": "post owner"}`|

Либо доступно по адресу в POST-форме:
```
/api/posts/
```

## Добавление комментария к статье
|type|url|data |
|----|---|-----------|
|POST |/api/comments/|`{"text": "comment text","author": "comment author", "post": <int:post_id>}`|

Либо доступно по адресу в POST-форме:
```
/api/comments/
```

## Добавление коментария в ответ на другой комментарий
|type|url|data |
|----|---|-----------|
|POST |/api/comments/|`{"text": "comment text","author": "comment author", "post": <int:post_id>, "parent": <int:comment_id>}`|

Либо доступно по адресу в POST-форме:
```
/api/comments/
```

## Получение всех комментариев к статье вплоть до 3 уровня вложенности
1. Через кнопку Filters c указанием параметра `Level is less than or equal to:` = 3
2. Вручную:
```
/api/comments/?level__lte=3
```

## Получение всех вложенных комментариев для комментария 3 уровня
```
/api/comments/<int:comment_id>/?nested=true
```

Можно включить и сам комментарий, вложенность которого выводим:
```
/api/comments/<int:comment_id>/?nested=true&include_self=true
```

## Swagger
```
/swagger/
```
