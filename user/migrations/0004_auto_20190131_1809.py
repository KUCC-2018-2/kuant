# Generated by Django 2.1.4 on 2019-01-31 18:09

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('user', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='User',
            old_name='user_id',
            new_name='username'
        ),
        migrations.RenameField(
            model_name='User',
            old_name='user_name',
            new_name='nickname'
        ),
    ]
