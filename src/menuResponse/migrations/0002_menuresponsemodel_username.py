# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-13 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuResponse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuresponsemodel',
            name='userName',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
