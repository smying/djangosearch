# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-07 02:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0006_auto_20160507_0244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=30)),
                ('brief', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('count', models.IntegerField()),
                ('pub_at', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='ebook',
            name='types',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Type'),
        ),
    ]
