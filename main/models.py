from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

def upload_dir(instance, file):
    return f'{instance.num}/{file}'

class Post(models.Model):
    num = models.UUIDField(default=uuid.uuid4, verbose_name='Артикль')
    photo = models.ImageField(upload_to=upload_dir, verbose_name='Изображение')
    author = models.CharField(max_length=100, blank=True, null=True, verbose_name='Автор')
    tags = TaggableManager()
    posted_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='posted_by_user', verbose_name='Добавлено пользователем')
    views = models.ManyToManyField('IpModel', verbose_name='Просмотры')
    likes = models.ManyToManyField(User, verbose_name='Нравится')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return str(self.pk)
    
    def get_absolute_url(self):
        return reverse('show_post', kwargs={'post_uuid': self.num})
    
    def total_views(self):
        return f'{self.views.count():,d}'
    
    def total_likes(self):
        return f'{self.likes.count():,d}'
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create']

class IpModel(models.Model):
    ip = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'ip'
        verbose_name_plural = 'ip'

    def __str__(self):
        return self.ip