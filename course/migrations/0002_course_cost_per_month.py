# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cost_per_month',
            field=models.IntegerField(default=400000),
            preserve_default=False,
        ),
    ]
