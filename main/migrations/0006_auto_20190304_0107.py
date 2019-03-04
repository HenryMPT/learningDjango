# Generated by Django 2.1.7 on 2019-03-04 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190303_2320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tutorial_published',
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 4, 1, 7, 16, 794296), verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=-1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 4, 1, 7, 16, 794296), verbose_name='date published'),
        ),
    ]
