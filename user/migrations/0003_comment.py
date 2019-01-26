# Generated by Django 2.1.4 on 2019-01-26 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_message_scrap_write'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField()),
                ('registerd_at', models.DateTimeField()),
                ('message', models.CharField(max_length=2000)),
                ('is_recreated', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]