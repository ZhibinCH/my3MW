# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-03 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SumSites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=30)),
                ('site_id', models.CharField(max_length=30)),
                ('sum_a_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sum_b_value', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
