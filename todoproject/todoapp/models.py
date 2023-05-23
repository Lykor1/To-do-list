from django.db import models

class TodoListItem(models.Model):
    content = models.TextField(verbose_name='Задача')
    date = models.DateField(null=True, blank=True, verbose_name='Дата')
    time = models.TimeField(null=True, blank=True, verbose_name='Время')

    def __str__(self):
        return self.content