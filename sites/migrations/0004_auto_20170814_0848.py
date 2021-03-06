# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-14 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_site'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'verbose_name_plural': 'Site Items'},
        ),
        migrations.AlterModelOptions(
            name='sites',
            options={'verbose_name_plural': 'Site Names'},
        ),
        migrations.AlterField(
            model_name='site',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='sites',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Site name'),
        ),
    ]
