# Generated by Django 3.2.18 on 2023-03-02 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='ФИО')),
                ('passport', models.CharField(max_length=12, unique=True, verbose_name='Серия и номер паспорта')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True, verbose_name='Контактный телефон')),
            ],
        ),
        migrations.CreateModel(
            name='UserCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='contacts',
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, upload_to='logos/', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='company',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='usercompany',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Company', to='users.company', verbose_name='Компания'),
        ),
        migrations.AddField(
            model_name='usercompany',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='admission',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='users.company', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='company',
            name='admission_lists',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admission', to='users.admission', verbose_name='Список на допуск'),
        ),
        migrations.AddField(
            model_name='company',
            name='contacts',
            field=models.ManyToManyField(blank=True, related_name='users', through='users.UserCompany', to=settings.AUTH_USER_MODEL, verbose_name='Контакты'),
        ),
    ]