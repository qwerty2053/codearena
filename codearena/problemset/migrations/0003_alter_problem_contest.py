# Generated by Django 4.2.1 on 2023-06-02 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0001_initial'),
        ('problemset', '0002_alter_problem_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='contest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='contests.contest', verbose_name='Контест'),
        ),
    ]