# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedMOHApp', '0003_auto_20170321_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]
