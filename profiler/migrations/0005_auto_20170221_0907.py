# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-21 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiler', '0004_auto_20170131_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='communities',
            field=models.ManyToManyField(related_name='get_members', to='communities.Community'),
        ),
    ]
