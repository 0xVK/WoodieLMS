# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-25 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courser', '0024_auto_20170525_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerfile',
            name='status',
            field=models.CharField(choices=[('C', 'Перевірено'), ('R', 'Відправлено на доопрацювання'), ('W', 'Очікує перевірки')], default='W', max_length=3),
        ),
    ]
