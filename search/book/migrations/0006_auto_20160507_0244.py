# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-07 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20160507_0240'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ebook',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]