# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-16 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestataires', '0007_auto_20160916_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='type_prestataire',
            name='logo_defaut',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='logos/categorie/'),
        ),
    ]