# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-06 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_auto_20170806_0833'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('a_value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='A Value')),
                ('b_value', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='B Value')),
                ('site_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Sites')),
            ],
        ),
    ]
