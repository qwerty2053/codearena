from django.contrib.auth.models import User
from django.db import models


class Contest(models.Model):
    title = models.CharField('Название', max_length=50)
    duration = models.DurationField('Продолжительность')
    start_time = models.DateTimeField('Время начала')
    author = models.ForeignKey(User, verbose_name='Автор', null=True, blank=True, on_delete=models.CASCADE)
    # difficulty = models.

    class Meta:
        verbose_name = 'Контест'
        verbose_name_plural = 'Контесты'

    def __str__(self):
        return self.title
