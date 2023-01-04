from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(blank=True, max_length=25, unique=True, verbose_name="Ник")
    first_name = models.CharField(blank=True, max_length=25, verbose_name="Имя")
    last_name = models.CharField(blank=True, max_length=25, verbose_name="Фамилия")
    email = models.EmailField(blank=True, verbose_name="Email", unique=True)
    age = models.SmallIntegerField(blank=True, null=True, verbose_name='Возраст')
    avatar = models.ImageField(upload_to='users', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'