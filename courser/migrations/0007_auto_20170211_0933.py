# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-11 07:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courser', '0006_auto_20170210_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursestep',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coursestep',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='course_step',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courser.CourseStep'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='text',
            field=models.TextField(max_length=15000),
        ),
    ]
