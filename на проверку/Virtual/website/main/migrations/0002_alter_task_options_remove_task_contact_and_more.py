# Generated by Django 4.2.2 on 2023-07-07 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
    ]
