# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-19 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='name_db',
        ),
        migrations.RemoveField(
            model_name='categorie',
            name='name_db',
        ),
        migrations.AddField(
            model_name='article',
            name='titre_court',
            field=models.CharField(blank=True, default=None, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='titre_article',
            field=models.CharField(max_length=300),
        ),
    ]
