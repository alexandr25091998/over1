# Generated by Django 4.2.2 on 2023-07-07 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_task_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tittle',
            new_name='title',
        ),
    ]
