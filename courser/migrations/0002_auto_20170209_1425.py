# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-09 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(blank=True, max_length=80, null=True)),
                ('step_type', models.CharField(choices=[('L', 'Лекція'), ('D', 'Диктант'), ('T', 'Тест'), ('I', 'Самостійна робота')], max_length=1)),
                ('is_available', models.BooleanField(default=True)),
                ('start_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('stop_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='community',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.Community'),
        ),
        migrations.AddField(
            model_name='coursestep',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courser.Course'),
        ),
    ]
