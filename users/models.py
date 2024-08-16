from django.contrib.auth.models import AbstractUser

from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to='avatars/', **NULLABLE, verbose_name="Аватар")
    phone_number = models.CharField(max_length=15, **NULLABLE, verbose_name="Телефон")
    country = models.CharField(max_length=50, **NULLABLE, verbose_name="Страна")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    token = models.CharField(max_length=100, **NULLABLE, verbose_name="Токен")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
