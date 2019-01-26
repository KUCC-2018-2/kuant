# Generated by Django 2.1.4 on 2019-01-26 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_used', models.BooleanField(default=0)),
                ('title', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateTimeField()),
                ('pay', models.IntegerField(default=0)),
                ('experience', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace_name', models.CharField(max_length=30)),
                ('level', models.IntegerField(default=0)),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posting.WorkPlace')),
            ],
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worktype_name', models.CharField(max_length=30)),
                ('level', models.IntegerField(default=0)),
                ('parend_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posting.WorkType')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='workplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posting.WorkPlace'),
        ),
        migrations.AddField(
            model_name='content',
            name='worktype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posting.WorkType'),
        ),
    ]
