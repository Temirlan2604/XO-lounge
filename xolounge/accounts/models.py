from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email адрес', unique=True)
    first_name = models.CharField('Имя', max_length=30, blank=True)
    last_name = models.CharField('Фамилия', max_length=30, blank=True)
    is_staff = models.BooleanField('Персонал', default=False,
        help_text='Может заходить в админ-панель')
    is_active = models.BooleanField('Активен', default=True,
        help_text='Считается активным, если галочка стоит')
    date_joined = models.DateTimeField('Дата регистрации', default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email и пароль — обязательны всегда

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
