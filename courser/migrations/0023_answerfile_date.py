# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 18:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courser', '0022_auto_20170302_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerfile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 25, 21, 3, 0, 893967)),
        ),
    ]
