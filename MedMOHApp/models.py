# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from django_datatables_view.base_datatable_view import BaseDatatableView

from django.core.urlresolvers import reverse


from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()

class Company(models.Model):
    id = models.AutoField
    name = models.CharField(u'Εταιρία', max_length=50, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('MedMOHApp:listCompany')

class ExaminationCategory(models.Model):
    id = models.AutoField
    name = models.CharField(u'Κατηγορία Εξέτασης', max_length=50, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('MedMOHApp:listexaminationcategory')

class People(models.Model):
    id = models.AutoField
    name = models.CharField(u'Όνομα',max_length=30)
    surname = models.CharField(u'Επώνυμο',max_length=50)
    dateofbirth = models.DateField(u'Ημερομηνία Γέννησης', blank=True, null=True)
    phone = models.CharField(u'Τηλέφωνο',max_length=60, blank=True, null=True)
    fax = models.CharField(u'FAX',max_length=60, blank=True, null=True)
    mobile = models.CharField(u'Κινητό',max_length=60, blank=True, null=True)
    mail = models.EmailField(u'Email', max_length=250, blank=True, null=True)
    ispatient = models.NullBooleanField(u'Ασθενής',db_column='IsPatient')   
    isdoctor = models.NullBooleanField(u'Γιατρός',db_column='IsDoctor')   
    notes = models.CharField(verbose_name=u'Σημειώσεις', max_length=8192, blank=True, null=True)
    companyid = models.ForeignKey(Company, verbose_name=u'Εταιρία')
    amka = models.CharField(verbose_name=u'ΑΜΚΑ', max_length=8, blank=True, null=True)


    class Meta:
        unique_together = (("name", "surname", "companyid"),)
        ordering = ('surname','name')

    def __unicode__(self):
        return self.surname + ' ' + self.name

    def get_absolute_url(self):
        if self.isdoctor:
            return reverse('MedMOHApp:doctor_list')
        else:
            return reverse('MedMOHApp:patient_list')

class Examination(models.Model):
    id = models.AutoField
    peopleid = models.ForeignKey(People, verbose_name=u'Ασθενής')
    doctorid = models.ForeignKey(People, verbose_name=u'Γιατρός',limit_choices_to={'isdoctor': True} , related_name = 'Examination0Doctor')
    examinationcategorid = models.ForeignKey(ExaminationCategory,verbose_name=u'Κατηγορία')
    dateofexam = models.DateField(verbose_name=u'Ημερομηνία Εξέτασης')
    dayoff = models.BooleanField(verbose_name=u'Άδεια')
    dateoffstart = models.DateField(verbose_name=u'Άδεια από', blank=True, null=True)
    dateoffend   = models.DateField(verbose_name=u'Άδεια έως', blank=True, null=True)
    daysoffgiven = models.IntegerField(verbose_name=u'Ημέρες Άδειας', blank=True, null=True)
    treatment = models.CharField(verbose_name=u'Αγωγή', max_length=8192, blank=True, null=True)
    diagnosis = models.CharField(verbose_name=u'Διάγνωση', max_length=8192, blank=True, null=True)
    notes   = models.CharField(verbose_name=u'Σημειώσεις',max_length=8192, blank=True, null=True)
    comments = models.CharField(verbose_name=u'Σχόλια',max_length=8192, blank=True, null=True)
#    docfile = models.FileField(upload_to='%Y/%m/%d', blank=True, null=True)
    docfile = models.FileField(upload_to='%Y\%m\%d', blank=True, null=True, storage=gd_storage)

    class Meta:
        ordering = ('-dateofexam',)

    def surname(self):
        return self.peopleid.surname + ' ' + self.peopleid.name

    def get_absolute_url(self):
        return reverse('MedMOHApp:listexam', kwargs={'Patient': self.peopleid.id})

    def __unicode__(self):
        a=self.dateofexam
        return self.peopleid.surname + ' ' + self.peopleid.name +  ' ' +a.strftime('%d/%m/%Y') + ' + ' + self.notes[:100]



from django.contrib.auth.models import User

class SpecialUsers(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    peopleid    = models.ForeignKey(People, verbose_name='Άνθρωπος')
    altpeopleid = models.ForeignKey(People, verbose_name='Alt.Άνθρωπος', related_name='SpecialUserAltPeople')
    peoples     = models.ManyToManyField(People, verbose_name = 'Άνθρωποι', related_name='SpecialUserAltPeoples')
    doctors     = models.ManyToManyField(People, limit_choices_to={'isdoctor': True}, verbose_name = 'Γιατροί', related_name='SpecialUserAltDoctors')
    notes       = models.CharField(verbose_name=u'Σημειώσεις',max_length=100)


# MedicineCategory
class MedicineCategory(models.Model):
    id = models.AutoField
    name = models.CharField(verbose_name=u'Ονομασία',max_length=50, unique=True)
    sname = models.CharField(verbose_name=u'Σύντμηση',max_length=15)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', 'sname')

    def get_absolute_url(self):
        return reverse('MedMOHApp:listMedicineCategory')


# Medicine
class Medicine(models.Model):
    peopleid  = models.ForeignKey(People,verbose_name=u'Ασθενής')
    doctorid  = models.ForeignKey(People,verbose_name=u'Γιατρός', limit_choices_to={'isdoctor': True} , related_name = 'MedicineDoctor')
    categorid = models.ForeignKey(MedicineCategory,verbose_name=u'Κατηγορία')
    dateof    = models.DateField(verbose_name=u'Ημερομηνία')
    datestart = models.DateField(verbose_name=u'Από', blank = True, null = True)
    dateend   = models.DateField(verbose_name=u'Έως', blank=True, null=True)
    notes     = models.CharField(verbose_name=u'Σημειώσεις',max_length=8192, blank=True, null=True)

    class Meta:
        unique_together = (("peopleid", "doctorid", "categorid", "dateof" ),)
        ordering = ('-dateof',)

    def get_absolute_url(self):
        return reverse('MedMOHApp:listmedicine', kwargs={'Patient': self.peopleid.id})

    def __unicode__(self):
        a=self.dateofexam
        return self.peopleid.surname + ' ' + self.peopleid.name +  ' ' +a.strftime('%d/%m/%Y') + ' + ' + self.notes[:100]



class ExamDocument(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')