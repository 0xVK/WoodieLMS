# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0011_auto_20170204_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]