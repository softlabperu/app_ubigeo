# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-12 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('ubigeo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ubigeo.Departamento')),
            ],
        ),
        migrations.AddField(
            model_name='distrito',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_ubigeo.Provincia'),
        ),
        migrations.AlterUniqueTogether(
            name='provincia',
            unique_together=set([('nombre', 'departamento')]),
        ),
        migrations.AlterUniqueTogether(
            name='distrito',
            unique_together=set([('nombre', 'provincia')]),
        ),
    ]