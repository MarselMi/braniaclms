from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name="Email", unique=True)
    age = models.SmallIntegerField(blank=True, null=True, verbose_name='Возраст')
    avatar = models.ImageField(upload_to='users', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'