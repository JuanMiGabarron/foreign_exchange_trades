# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_auto_20170313_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='rate',
            field=models.DecimalField(decimal_places=5, max_digits=6),
        ),
    ]