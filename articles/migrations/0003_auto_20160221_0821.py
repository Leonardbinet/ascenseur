# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20160221_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_db', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]