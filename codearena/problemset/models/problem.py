from django.db import models


class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=50, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='Условие')
    notes = models.TextField(verbose_name='Примечание', null=True, blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, verbose_name='Сложность')
    tags = models.ManyToManyField('problemset.tag', verbose_name='Теги')
    points = models.PositiveIntegerField(verbose_name='Баллы')
    contest = models.ForeignKey('contests.Contest', on_delete=models.CASCADE, verbose_name='Контест', related_name='problems')
    time_limit = models.IntegerField(verbose_name='Ограничение по времени')
    memory_limit = models.IntegerField(verbose_name='Ограничение по памяти')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    solved_count = models.PositiveIntegerField(verbose_name='Решений', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
