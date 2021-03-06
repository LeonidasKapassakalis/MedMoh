# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 11:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='\u0395\u03c4\u03b1\u03b9\u03c1\u03af\u03b1')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='\u03a7\u03ce\u03c1\u03b1')),
                ('abbr', models.CharField(max_length=2, unique=True, verbose_name='\u03a7\u03ce\u03c1\u03b1(2)')),
                ('telephoneext', models.CharField(max_length=4, verbose_name='\u03a4\u03b7\u03bb')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateofexam', models.DateField(verbose_name='\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1 \u0395\u03be\u03ad\u03c4\u03b1\u03c3\u03b7\u03c2')),
                ('dayoff', models.BooleanField(verbose_name='\u0386\u03b4\u03b5\u03b9\u03b1')),
                ('dateoffstart', models.DateField(blank=True, null=True, verbose_name='\u0386\u03b4\u03b5\u03b9\u03b1 \u03b1\u03c0\u03cc')),
                ('dateoffend', models.DateField(blank=True, null=True, verbose_name='\u0386\u03b4\u03b5\u03b9\u03b1 \u03ad\u03c9\u03c2')),
                ('daysoffgiven', models.IntegerField(verbose_name='\u0397\u03bc\u03ad\u03c1\u03b5\u03c2 \u0386\u03b4\u03b5\u03b9\u03b1\u03c2')),
                ('treatment', models.CharField(blank=True, max_length=8192, null=True, verbose_name='\u0391\u03b3\u03c9\u03b3\u03ae')),
                ('diagnosis', models.CharField(blank=True, max_length=8192, null=True, verbose_name='\u0394\u03b9\u03ac\u03b3\u03bd\u03c9\u03c3\u03b7')),
                ('notes', models.CharField(blank=True, max_length=8192, null=True, verbose_name='\u03a3\u03b7\u03bc\u03b5\u03b9\u03ce\u03c3\u03b5\u03b9\u03c2')),
                ('comments', models.CharField(blank=True, max_length=8192, null=True, verbose_name='\u03a3\u03c7\u03cc\u03bb\u03b9\u03b1')),
            ],
            options={
                'ordering': ('-dateofexam',),
            },
        ),
        migrations.CreateModel(
            name='ExaminationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1 \u0395\u03be\u03ad\u03c4\u03b1\u03c3\u03b7\u03c2')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='\u039f\u03bd\u03b1\u03bc\u03b1\u03c3\u03af\u03b1')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u0394\u03b9\u03b5\u03cd\u03b8\u03c5\u03bd\u03c3\u03b7')),
                ('phone', models.CharField(blank=True, max_length=60, null=True, verbose_name='\u03a4\u03b7\u03bb\u03ad\u03c6\u03c9\u03bd\u03b1')),
                ('mail', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('tk', models.CharField(blank=True, max_length=5, null=True, verbose_name='TK')),
                ('text', models.TextField(blank=True, null=True, verbose_name='\u03a3\u03c7\u03cc\u03bb\u03b9\u03b1')),
                ('hospital', models.NullBooleanField(verbose_name='\u039d\u03bf\u03c3\u03bf\u03ba\u03bf\u03bc\u03b5\u03af\u03bf')),
                ('medicalcenter', models.NullBooleanField(verbose_name='\u0399\u03b1\u03c4\u03c1\u03b9\u03ba\u03cc \u039a\u03ad\u03bd\u03c4\u03c1\u03bf')),
                ('eopyy', models.NullBooleanField(verbose_name='\u0395\u039f\u03a0\u03a0\u03a5')),
                ('contact', models.TextField(blank=True, null=True, verbose_name='\u03a3\u03cd\u03bd\u03b4\u03b5\u03c3\u03bc\u03bf\u03c2')),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedMOHApp.Country', verbose_name='\u03a7\u03ce\u03c1\u03b1')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateof', models.DateField(verbose_name='\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1')),
                ('datestart', models.DateField(verbose_name='\u0391\u03c0\u03cc')),
                ('dateend', models.DateField(verbose_name='\u0388\u03c9\u03c2')),
                ('notes', models.CharField(blank=True, max_length=8192, null=True, verbose_name='\u03a3\u03b7\u03bc\u03b5\u03b9\u03ce\u03c3\u03b5\u03b9\u03c2')),
            ],
            options={
                'ordering': ('-dateof',),
            },
        ),
        migrations.CreateModel(
            name='MedicineCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='\u039f\u03bd\u03bf\u03bc\u03b1\u03c3\u03af\u03b1')),
                ('sname', models.CharField(max_length=15, verbose_name='\u03a3\u03cd\u03bd\u03c4\u03bc\u03b7\u03c3\u03b7')),
            ],
            options={
                'ordering': ('name', 'sname'),
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u038c\u03bd\u03bf\u03bc\u03b1')),
                ('surname', models.CharField(max_length=50, verbose_name='\u0395\u03c0\u03ce\u03bd\u03c5\u03bc\u03bf')),
                ('dateofbirth', models.DateField(blank=True, null=True, verbose_name='\u0397\u03bc\u03b5\u03c1\u03bf\u03bc\u03b7\u03bd\u03af\u03b1 \u0393\u03ad\u03bd\u03bd\u03b7\u03c3\u03b7\u03c2')),
                ('phone', models.CharField(blank=True, max_length=60, null=True, verbose_name='\u03a4\u03b7\u03bb\u03ad\u03c6\u03c9\u03bd\u03bf')),
                ('fax', models.CharField(blank=True, max_length=60, null=True, verbose_name='FAX')),
                ('mobile', models.CharField(blank=True, max_length=60, null=True, verbose_name='\u039a\u03b9\u03bd\u03b7\u03c4\u03cc')),
                ('mail', models.EmailField(blank=True, max_length=250, null=True, verbose_name='Email')),
                ('ispatient', models.NullBooleanField(db_column='IsPatient', verbose_name='\u0391\u03c3\u03b8\u03b5\u03bd\u03ae\u03c2')),
                ('isdoctor', models.NullBooleanField(db_column='IsDoctor', verbose_name='\u0393\u03b9\u03b1\u03c4\u03c1\u03cc\u03c2')),
                ('notes', models.CharField(blank=True, max_length=8192, null=True, verbose_name='\u03a3\u03b7\u03bc\u03b5\u03b9\u03ce\u03c3\u03b5\u03b9\u03c2')),
            ],
            options={
                'ordering': ('surname', 'name'),
            },
        ),
        migrations.CreateModel(
            name='SpecialUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=100, verbose_name='\u03a3\u03b7\u03bc\u03b5\u03b9\u03ce\u03c3\u03b5\u03b9\u03c2')),
                ('altpeopleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SpecialUserAltPeople', to='MedMOHApp.People', verbose_name='Alt.\u0386\u03bd\u03b8\u03c1\u03c9\u03c0\u03bf\u03c2')),
                ('doctors', models.ManyToManyField(related_name='SpecialUserAltDoctors', to='MedMOHApp.People', verbose_name='\u0393\u03b9\u03b1\u03c4\u03c1\u03bf\u03af')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedMOHApp.Locations', verbose_name='\u03a4\u03cc\u03c0\u03bf\u03c2')),
                ('peopleid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedMOHApp.People', verbose_name='\u0386\u03bd\u03b8\u03c1\u03c9\u03c0\u03bf\u03c2')),
                ('peoples', models.ManyToManyField(related_name='SpecialUserAltPeoples', to='MedMOHApp.People', verbose_name='\u0386\u03bd\u03b8\u03c1\u03c9\u03c0\u03bf\u03b9')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='categorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedMOHApp.MedicineCategory', verbose_name='\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='doctorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MedicineDoctor', to='MedMOHApp.People', verbose_name='\u0393\u03b9\u03b1\u03c4\u03c1\u03cc\u03c2'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='peopleid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedMOHApp.People', verbose_name='\u0391\u03c3\u03b8\u03b5\u03bd\u03ae\u03c2'),
        ),
        migrations.AddField(
            model_name='locations',
            name='peoples',
            field=models.ManyToManyField(blank=True, null=True, to='MedMOHApp.People', verbose_name='\u0391\u03c4\u03bf\u03bc\u03b1'),
        ),
        migrations.AddField(
            model_name='examination',
            name='doctorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Examination0Doctor', to='MedMOHApp.People', verbose_name='\u0393\u03b9\u03b1\u03c4\u03c1\u03cc\u03c2'),
        ),
        migrations.AddField(
            model_name='examination',
            name='examinationcategorid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedMOHApp.ExaminationCategory', verbose_name='\u039a\u03b1\u03c4\u03b7\u03b3\u03bf\u03c1\u03af\u03b1'),
        ),
        migrations.AddField(
            model_name='examination',
            name='peopleid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MedMOHApp.People', verbose_name='\u0391\u03c3\u03b8\u03b5\u03bd\u03ae\u03c2'),
        ),
        migrations.AlterUniqueTogether(
            name='medicine',
            unique_together=set([('peopleid', 'doctorid', 'categorid', 'dateof')]),
        ),
    ]
