# Generated by Django 2.1.4 on 2019-01-11 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_auto_20190111_0542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='comments',
            new_name='comment',
        ),
    ]