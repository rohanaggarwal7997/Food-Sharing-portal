# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-07-07 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0016_notifications1'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications1',
            name='boolean_field',
            field=models.BooleanField(default=True),
        ),
    ]
