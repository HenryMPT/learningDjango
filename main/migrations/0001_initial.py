# Generated by Django 2.1.7 on 2019-03-03 23:11

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('tutorial_published', models.DateTimeField(default=datetime.datetime(2019, 3, 3, 23, 11, 1, 141155), verbose_name='date published')),
                ('username', models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.CharField(max_length=200)),
                ('tutorial_content', models.TextField()),
                ('tutorial_published', models.DateTimeField(default=datetime.datetime(2019, 3, 3, 23, 11, 1, 141155), verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial2_title', models.CharField(max_length=200)),
                ('tutorial2_content', models.TextField()),
                ('tutorial2_published', models.DateTimeField(default=datetime.datetime(2019, 3, 3, 23, 11, 1, 142151), verbose_name='date published')),
            ],
        ),
    ]
