# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-28 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0013_comment_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.FloatField(),
        ),
    ]