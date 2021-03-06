# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ersignup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='full_name',
        ),
        migrations.AddField(
            model_name='signup',
            name='first_name',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='signup',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='pan',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
    ]
