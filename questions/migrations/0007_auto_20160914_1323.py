# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-14 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20160914_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='ordre',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='ordre',
            field=models.IntegerField(blank=True, default=10, null=True),
        ),
    ]