# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0012_auto_20170204_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='text',
            field=models.TextField(max_length=2500),
        ),
    ]
