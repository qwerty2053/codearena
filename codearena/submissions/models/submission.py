from django.contrib.auth.models import User
from django.db import models


# def get_testset_path


class Submission(models.Model):
    STATUS_CHOICES = [
        ('in queue', 'In queue'),
        ('running', 'Running'),
        ('accepted', 'Accepted'),
        ('wrong answer', 'Wrong answer'),
        ('time limit exceeded', 'Time limit exceeded'),
        ('runtime error', 'Runtime error'),
        ('compilation error', 'Compilation error'),
        ('ignored', 'Ignored'),
    ]

    # TO DO: replace User to the custom user
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    problem = models.ForeignKey('problemset.problem', on_delete=models.CASCADE, verbose_name='Задача')
    submit_time = models.DateTimeField(auto_now_add=True, verbose_name='Время посылки')
    status = models.CharField(max_length=19, choices=STATUS_CHOICES, verbose_name='Вердикт', null=True, blank=True)
    memory_consumed = models.PositiveIntegerField(default=0, verbose_name='Память', null=True, blank=True)
    time_consumed = models.PositiveIntegerField(default=0, verbose_name='Время', null=True, blank=True)
    language = models.ForeignKey('submissions.language', on_delete=models.SET_DEFAULT, default='Unknown', verbose_name='Язык')
    source_code = models.TextField(verbose_name='Исходный код')
    points = models.PositiveIntegerField(null=True, blank=True, verbose_name='Баллы')
    passed_tests_count = models.PositiveIntegerField(default=0, verbose_name='Количество пройденных тестов', null=True, blank=True)
    # testset_dir = models.FilePathField(verbose_name='Тестовые данные', path='static/tests/')
    contest = models.ForeignKey('contests.contest', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Контест')
    relative_time = models.PositiveIntegerField(verbose_name='Время прошедшее с начала контеста', null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Посылка'
        verbose_name_plural = 'Посылки'
