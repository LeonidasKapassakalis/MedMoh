# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedMOHApp', '0008_auto_20170403_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='amka',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='\u0391\u039c\u039a\u0391'),
        ),
    ]
