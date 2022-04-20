# Тестовое задание

## Описание
Это тестовое задание по реализации REST API для системы комментариев блога

## Установка
```console
pip install git
git clone https://github.com/expmax85/blog
cd blog/
pip install -r requirenments.txt
python manage.py runserver
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