# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-03 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvgSites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=30)),
                ('site_id', models.CharField(max_length=30)),
                ('avg_a_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('avg_b_value', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]