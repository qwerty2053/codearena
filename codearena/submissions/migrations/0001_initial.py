# Generated by Django 4.2.1 on 2023-06-03 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problemset', '0005_alter_problem_title'),
        ('users', '0001_initial'),
        ('contests', '0002_contest_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='Время посылки')),
                ('status', models.CharField(choices=[('in queue', 'In queue'), ('running', 'Running'), ('accepted', 'Accepted'), ('wrong answer', 'Wrong answer'), ('time limit exceeded', 'Time limit exceeded'), ('runtime error', 'Runtime error'), ('compilation error', 'Compilation error'), ('ignored', 'Ignored')], max_length=19, verbose_name='Вердикт')),
                ('memory', models.PositiveIntegerField(default=0, verbose_name='Память')),
                ('time', models.PositiveIntegerField(default=0, verbose_name='Когда')),
                ('source_code', models.TextField(verbose_name='Исходный код')),
                ('points', models.PositiveIntegerField(blank=True, null=True, verbose_name='Баллы')),
                ('passed_tests_count', models.PositiveIntegerField(default=0, verbose_name='Количество пройденных тестов')),
                ('testset_dir', models.FilePathField(verbose_name='Тестовые данные')),
                ('relative_time', models.PositiveIntegerField(verbose_name='Время прошедшее с начала контеста')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Автор')),
                ('contest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contests.contest', verbose_name='Контест')),
                ('language', models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.SET_DEFAULT, to='submissions.language', verbose_name='Язык')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problemset.problem', verbose_name='Задача')),
            ],
        ),
    ]