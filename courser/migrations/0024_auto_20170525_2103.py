# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courser', '0023_answerfile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerfile',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
