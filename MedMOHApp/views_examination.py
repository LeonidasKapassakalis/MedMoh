# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms

import django_tables2 as tables
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.utils.html import mark_safe
from  django.urls import reverse
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from datetimewidget.widgets import DateTimeWidget, DateWidget , TimeWidget

from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError

from .views import ModelFormWidgetMixin
from .views import get_spec_user

########################################################################################################

#'peopleid','doctorid'.'examinationcategorid','dateofexam','dayoff','dateoffstart','dateoffend','daysoffgiven','treatment','diagnosis','notes','comments''


########################################################################################################
# Examination
from .models import Examination
from .models import People

class ExaminationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = Examination
        fields = ['peopleid', 'doctorid','examinationcategorid', 'dateofexam',
                  'treatment', 'diagnosis', 'notes', 'comments',
                  'dayoff', 'dateoffstart', 'dateoffend','daysoffgiven']
        widgets = {
            'dateofexam': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
            'dateoffstart': DateWidget(attrs={'id': "id_dateofstart"}, bootstrap_version=3),
            'dateoffend': DateWidget(attrs={'id': "id_dateofend"}, bootstrap_version=3),
            'diagnosis': forms.Textarea(attrs={'cols': 100, 'rows': 5}),
            'treatment': forms.Textarea(attrs={'cols': 100, 'rows': 5}),
            'notes': forms.Textarea(attrs={'cols': 100, 'rows': 5}),
            'comments': forms.Textarea(attrs={'cols': 100, 'rows': 5})
            }

    def clean_peopleid(self):
        peopleid = self.cleaned_data['peopleid']
        userparam = get_spec_user(self.request)
#Super is allowed for anything TODO
#        if userparam[0]:
#            return peopleid
        if userparam[1]:
            return peopleid
        if not userparam[1]:
            if peopleid.id in userparam[5]:
                return peopleid
            else:
                raise ValidationError((u'Δεν μπορεί να γίνει καταχώρηση για ' + peopleid.name + ' ' +peopleid.surname), code='invalid')


class ExaminationTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = Examination
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['peopleid', 'comments', 'id']
        sequence = ['dateofexam', 'doctorid',  '...']

    def render_detail(self, record):
        rev = reverse('MedMOHApp:detailexam', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Λεπτομέρειες</span></a>')


def ExaminationList(request, Patient):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = ExaminationTable(Examination.objects.all().filter(peopleid=Patient))
    request.session['patient_id'] = Patient
    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    p = People.objects.get(pk=Patient)
    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table,
                   'page_title': u'Εξετάσεις για ' + p.name + ' ' + p.surname,
                   'form_name': u'Εξετάσεις για ' + p.name + ' ' + p.surname,
                   'param_action1': reverse('MedMOHApp:createexam'),
                    'param_action1_name': 'Προσθήκη'})


class ExaminationCreare(LoginRequiredMixin, UserPassesTestMixin,CreateView):
    model = Examination
    form_class = ExaminationForm
    template_name = 'General/General_cu_form.html'

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(self.__class__ , self).get_form_kwargs(*args, **kwargs)
        form_kwargs['request'] = self.request
        return form_kwargs

    def get_initial(self):
#        return  {'peopleid': get_spec_user(self.request)[3]}
        return  {'peopleid': self.request.session['patient_id']}

    def test_func(self):
        return True

class ExaminationDetailView(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DetailView):
    model = Examination

    def test_func(self):
        return True

class ExaminationUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Examination
    form_class = ExaminationForm
    template_name = 'General/General_cu_form.html'

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(self.__class__, self).get_form_kwargs(*args, **kwargs)
        form_kwargs['request'] = self.request
        return form_kwargs

    def test_func(self):
        return True


class ExaminationDelete(LoginRequiredMixin, UserPassesTestMixin, ModelFormWidgetMixin, DeleteView):
    model = Examination

    def test_func(self):
        return True

########################################################################################################
