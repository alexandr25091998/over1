# Generated by Django 4.2.2 on 2023-07-07 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_tittle_task_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
