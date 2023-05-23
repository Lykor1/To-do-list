# Generated by Django 4.2.1 on 2023-05-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todolistitem_date_todolistitem_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolistitem',
            name='content',
            field=models.TextField(verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='todolistitem',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='todolistitem',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Время'),
        ),
    ]
