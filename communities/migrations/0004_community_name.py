# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-29 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_community_communityinvite_communitywallpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='name',
            field=models.CharField(default='MDK', max_length=30),
            preserve_default=False,
        ),
    ]
