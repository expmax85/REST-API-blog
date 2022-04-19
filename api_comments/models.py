from django.contrib.auth import get_user_model
from django.db import models

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


User = get_user_model()

class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        print(val)
        if val:
            val.replace(microsecond=0)
            return val.isoformat('%Y-%m-%d %H:%M:%S')
        return ''

class Post(models.Model):
    created = CustomDateTimeField(auto_now_add=True, verbose_name='created date')
    title = models.CharField(max_length=100, blank=True, default='', verbose_name='title')
    content = models.TextField(blank=True, default='', verbose_name='content')
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, verbose_name='author')

    def __str__(self):
        return self.title


class Comment(MPTTModel):
    created = CustomDateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, verbose_name='text comment')
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, verbose_name='author')
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE, verbose_name='post')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.text[:20]
