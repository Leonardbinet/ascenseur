# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-19 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='meta_description',
            field=models.TextField(blank=True, max_length=155, null=True),
        ),
    ]
