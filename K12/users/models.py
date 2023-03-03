from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Admission(models.Model):
    name = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        verbose_name='ФИО',
    )
    passport = models.CharField(
        max_length=12,
        unique=True,
        blank=False,
        null=False,
        verbose_name='Серия и номер паспорта',
    )
    number = PhoneNumberField(
        unique=True,
        blank=True,
        verbose_name='Контактный телефон',
    )
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
        related_name='company',
        verbose_name='Компания',
    )

    def __str__(self):
        return self.name


class Company(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        blank=False,
        verbose_name='Название',
    )
    contacts = models.ManyToManyField(
        User,
        related_name='users',
        through='UserCompany',
        through_fields=(
            'company',
            'user',
        ),
        blank=True,
        verbose_name='Контакты',
    )
    admission_lists = models.TextField()
    image = models.ImageField(
        'Логотип',
        upload_to='logos/',
        blank=True,
    )

    def __str__(self):
        return self.title


class UserCompany(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="Company",
        verbose_name='Компания',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="User",
        verbose_name='Пользователь',
    )
