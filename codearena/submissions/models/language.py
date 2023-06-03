from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
