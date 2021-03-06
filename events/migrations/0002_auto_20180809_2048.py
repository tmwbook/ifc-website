# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-10 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_squashed_0002_auto_20180523_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='houseevent',
            options={'ordering': ('-date', '-start_time')},
        ),
        migrations.AlterModelOptions(
            name='officerevent',
            options={'ordering': ('-date', '-start_time')},
        ),
        migrations.RemoveField(
            model_name='houseevent',
            name='d_time',
        ),
        migrations.RemoveField(
            model_name='officerevent',
            name='d_time',
        ),
        migrations.AddField(
            model_name='houseevent',
            name='date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='houseevent',
            name='end_time',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='houseevent',
            name='start_time',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='officerevent',
            name='date',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='officerevent',
            name='end_time',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='officerevent',
            name='start_time',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
    ]
