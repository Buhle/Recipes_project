# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-04 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0002_auto_20170804_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
