# Generated by Django 2.1.7 on 2019-03-03 23:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190303_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.DeleteModel(
            name='Tutorial2',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 3, 23, 16, 25, 688282), verbose_name='date published'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
