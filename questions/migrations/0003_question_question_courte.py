# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-19 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20160919_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_courte',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
