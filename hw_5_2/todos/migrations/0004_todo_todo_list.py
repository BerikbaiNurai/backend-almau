# Generated by Django 5.1.5 on 2025-02-28 12:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todos.todolist'),
        ),
    ]
