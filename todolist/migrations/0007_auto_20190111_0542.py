# Generated by Django 2.1.4 on 2019-01-11 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_todolist_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='comments',
            field=models.TextField(max_length=150),
        ),
    ]
