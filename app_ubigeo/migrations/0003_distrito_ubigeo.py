# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-22 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ubigeo', '0002_auto_20180222_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='distrito',
            name='ubigeo',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]