from django.contrib.auth import get_user_model
from django.db import models

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


User = get_user_model()


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='created date')
    title = models.CharField(max_length=100, blank=True, default='', verbose_name='title')
    content = models.TextField(blank=True, default='', verbose_name='content')
    owner = models.CharField(max_length=50, blank=True, default='', verbose_name='owner')

    def __str__(self) -> str:
        return self.title


class Comment(MPTTModel):
    created = models.DateTimeField(auto_now_add=True, verbose_name='date added')
    text = models.TextField(blank=True, verbose_name='text comment')
    author = models.CharField(max_length=50, blank=True, verbose_name='author')
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE, verbose_name='post')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return f'answer for {self.author} on {self.text[:20]}'
