# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-14 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180514_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagem',
            field=models.ImageField(blank=True, db_column='Imagem', null=True, upload_to='media'),
        ),
    ]
