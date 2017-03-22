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

########################################################################################################
from .models import MedicineCategory

class MedicineCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = MedicineCategory
        fields = ['name', 'sname']

class MedicineCategoryTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = MedicineCategory
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'sname', '...']

    def render_detail(self, record):
        rev = reverse('MedMOHApp:updatemedicinecategory', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def MedicineCategoryList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = MedicineCategoryTable(MedicineCategory.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'MedicineCategoryList',
                    'form_name': u'MedicineCategoryList',
                    'param_action1': reverse('MedMOHApp:createmedicinecategory'),
                    'param_action1_name': 'Προσθήκη'})

class MedicineCategoryCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MedicineCategory
    form_class = MedicineCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class MedicineCategoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MedicineCategory
    form_class = MedicineCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import ExaminationCategory

class ExaminationCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = ExaminationCategory
        fields = ['name',]

class ExaminationCategoryTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = ExaminationCategory
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', '...']

    def render_detail(self, record):
        rev = reverse('MedMOHApp:updateexaminationcategory', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def ExaminationCategoryList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = ExaminationCategoryTable(ExaminationCategory.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'ExaminationCategoryList',
                    'form_name': u'ExaminationCategoryList',
                    'param_action1': reverse('MedMOHApp:createexaminationcategory'),
                    'param_action1_name': 'Προσθήκη'})

class ExaminationCategoryCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ExaminationCategory
    form_class = ExaminationCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class ExaminationCategoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ExaminationCategory
    form_class = ExaminationCategoryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################

########################################################################################################
from .models import Country

class CountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__, self).__init__(*args, **kwargs)

    class Meta:
        model = Country
        fields = ['name', 'abbr' , 'telephoneext']


class CountryTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])

    class Meta:
        model = Country
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id']
        sequence = ['name', 'abbr', '...']

    def render_detail(self, record):
        rev = reverse('MedMOHApp:updatecountry', kwargs={'pk': str(record.pk)})
        return mark_safe('<a href=' + rev + u'><span style="color:red">Ενημέρωση</span></a>')

#@login_required
def CountryList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = CountryTable(Country.objects.all())
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table, 'page_title': u'Εξετάσεις',
                    'page_title': u'CountryList',
                    'form_name': u'CountryList',
                    'param_action1': reverse('MedMOHApp:createcountry'),
                    'param_action1_name': 'Προσθήκη'})

class CountryCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Country
    form_class = CountryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

class CountryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Country
    form_class = CountryForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True

########################################################################################################



