# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MedMOHApp', '0006_auto_20170402_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='docfile',
            field=models.FileField(blank=True, null=True, upload_to='examdocuments/%Y/%m/%d'),
        ),
    ]
