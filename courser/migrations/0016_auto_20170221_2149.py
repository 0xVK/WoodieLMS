# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-21 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courser', '0015_dictation_show_results'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dictationsolution',
            old_name='solution',
            new_name='result',
        ),
    ]