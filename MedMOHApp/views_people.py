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
from django.contrib.auth.decorators import permission_required

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from datetimewidget.widgets import DateTimeWidget, DateWidget , TimeWidget

from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError

from .views import ModelFormWidgetMixin
from .views import get_spec_user


from django.core.urlresolvers import reverse_lazy
from django_addanother.widgets import AddAnotherWidgetWrapper
from django_addanother.widgets import AddAnotherEditSelectedWidgetWrapper


########################################################################################################

#['name','surname','dateofbirth','nationality','countryid','phone','fax','mobile','mail'\
#    ,'ispatient','isdoctor','canlogin','accessonlyhisfile','notes','photo']


from .models import People

from dal import autocomplete

from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.db.models.fields.reverse_related import ManyToOneRel

class PeopleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(self.__class__ , self).__init__(*args, **kwargs)

    class Meta:
        model = People
        fields = ['name', 'surname', 'dateofbirth', 'phone', 'mobile', 'mail' , 'amka' ,'companyid'
                  ,'ispatient','isdoctor','notes']
        widgets = {
            'companyid': autocomplete.ModelSelect2(url='MedMOHApp:select2_fk'),
            'dateofbirth': DateWidget(attrs={'id': "id_dateof"}, bootstrap_version=3),
            'notes': forms.Textarea(attrs={'cols': 100, 'rows': 5})
            }


class PeopleDetailView(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DetailView):
    model = People

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['page_title'] = u'Στοιχεία ' +  context['object'].surname + ' '  +  context['object'].name
        context['form_name'] = u'Αναλυτικά Στοιχεία Ατόμου '
        return context

    def test_func(self):
        return True


class PeopleCreare(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = People
    form_class = PeopleForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True


class PeopleUpdate(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = People
    form_class = PeopleForm
    template_name = 'General/General_cu_form.html'

    def test_func(self):
        return True


class PeopleDelete(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,DeleteView):
    model = People
    fields = ['name','surname','notes','mail']
    def test_func(self):
        return True

@permission_required('People.view', login_url='/login/')
def patient_list(request):
#     u = User.objects.get(username=request.user)
#     if request.user.is_superuser or request.user.is_staff:
#         print 'Super'
#
#     us = SpecialUsers.objects.get(user=request.user)
#
#     # qlist = []
#     # q_object = Q()
#     # for x in us.peoples.all():
#     #     a=('id',str(x.id))
#     #     qlist.append(a)
#
#     q_object = Q()
# #    print q_object
#     bb=[]
#     for x in us.peoples.all():
#         aa=x.id
#         bb.append(x.id)
#         q_object.add(Q(id=aa),Q.OR)
#     global GlobPeopleid
#     GlobPeopleid = bb[:]
#        print q_object
# #    qlist.append(('ispatient','1'))
#     q_list = [Q(x) for x in qlist]
#     print  q_list
#     print q_object
#     print reduce(operator.or_, q_list)

    userparam=get_spec_user(request)

    # if userparam[0]:
    #     table = PatientListTable(models.People.objects.all().filter(ispatient=True))
    # else:
    #     table = PatientListTable(models.People.objects.all().filter(userparam[7]))

    table = PatientListTable(People.objects.all().filter(userparam[7]))

#    table = PatientListTable(models.People.objects.all().filter(ispatient=1).filter(reduce(operator.or_,q_list)))
#    table = PatientListTable(models.People.objects.all().filter(ispatient=1))

    RequestConfig(request, paginate={'per_page': 25}).configure(table)
    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table,
                   'page_title': u'Ασθενείς',
                   'form_name': u'Ασθενείς',
                   'param_action1': reverse('MedMOHApp:create'),
                   'param_action1_name': 'Προσθήκη'})


class PeopleTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor='pk', verbose_name=('Delete'))
#    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
#    detail1 = tables.LinkColumn('item_detail1', args=[('pk')], orderable=False, empty_values=[''])
#    amend = tables.CheckBoxColumn(verbose_name=('Amend'), accessor='pk')
    class Meta:
        model = People
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id','ispatient','isdoctor','canlogin','accessonlyhisfile','notes']
        sequence = ['selection','name','surname','phone','...']

    def render_detail(self, record):
        return mark_safe('<a href=/MedMOHApp/detail/' + str(record.pk) + '/><span style="color:green">Λεπτομέριες</span></a></a>')


    def render_detail1(self, record):
        aaa='<input type="checkbox" name=' + str(record.pk) + ' value=' + str(record.pk) +' > '
        return mark_safe(aaa)


@permission_required('People.view', login_url='/login/')
def person_list(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    table = PeopleTable(People.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'General/Generic_Table_view_Selection.html',
                  {'objects': table,
                   'page_title': u'Άτομα',
                   'form_name': u'Άτομα',
                   'param_action1': reverse('MedMOHApp:create'),
                   'param_action1_name': 'Προσθήκη'})


class DoctorListTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
#    exams  = tables.LinkColumn('item_exams', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = People
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['dateofbirth', 'nationality', 'ispatient', 'isdoctor', 'canlogin', 'accessonlyhisfile', 'notes' ,'id']
        sequence = ['name','surname','...']

    def render_exams(self, record):
        return mark_safe('<a href=/MedMOHApp/examinationsListPerDoctor/'+str(record.pk)+'/><span style="color:blue">Εξετάσεις</span></a>')

    def render_detail(self,record):
        return mark_safe('<a href=/MedMOHApp/detail/'+str(record.pk)+'/><span style="color:green">Λεπτομέριες</span></a></a>')


@permission_required('People.view', login_url='/login/')
def doctor_list(request):
    table = DoctorListTable(People.objects.all().filter(isdoctor=1))
    RequestConfig(request, paginate={'per_page': 25}).configure(table)

    return render(request, 'General/Generic_Table_view.html',
                  {'objects': table,
                   'page_title': u'Γιατροί',
                   'form_name': u'Γιατροί' ,
                   'param_action1': reverse('MedMOHApp:create'),
                   'param_action1_name': 'Προσθήκη'})


#Patient Table
class PatientListTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')],orderable=False,empty_values=[''])
    exam   = tables.LinkColumn('item_exam', args=[('pk')],orderable=False,empty_values=[''])
    medicine  = tables.LinkColumn('item_medicine', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = People
        row_attrs = {
            'data-id': lambda record: record.pk,
        }
        attrs = {'class': 'paleblue'}
        exclude = ['dateofbirth', 'ispatient', 'isdoctor', 'canlogin', 'accessonlyhisfile', 'notes' ,'id', 'photo']
        sequence = ['name','surname','...']

    def render_detail(self,record):
        return mark_safe('<a href=/MedMOHApp/detail/'+str(record.pk)+'/><span style="color:green">Λεπτομέριες</span></a></a>')

    def render_exam(self, record):
        return mark_safe('<a href=/MedMOHApp/listexam/'+str(record.pk)+'/><span style="color:blue">Ιατρικές Εξ.</span></a>')

    def render_medicine(self, record):
        return mark_safe('<a href=/MedMOHApp/listmedicine/'+str(record.pk)+'/><span style="color:blue">Φάρμακα</span></a>')


####################################################################################################

import django_filters

class PeopleDetailTable(tables.Table):
    class Meta:
        model = People

class PeopleDetailFilter(django_filters.FilterSet):
    class Meta:
        model = People
        exclude = ()

class FilteredSingleTableView(tables.SingleTableView):
    filter_class = None

    def get_table_data(self):
        data = super(FilteredSingleTableView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=data)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
        context['filter'] = self.filter
        return context

class BioExaminationDetailFilteredSingleTableView(FilteredSingleTableView):
    model = People
    table_class = PeopleDetailTable
    filter_class = PeopleDetailFilter



class BioExaminationDetailFilterAll(django_filters.FilterSet):
    class Meta:
        model = People
        exclude = ('id','isdoctor','ispatient','dateofbirth','fax','mail','notes','mobile')
        # fields = {
        #     'name'
        # }

        fields = {'name': ['icontains'],
                  'surname': ['icontains'],
                  'amka': ['exact'],
                  'companyid':['exact']
          }



def BioExaminationDetailFilteredAll(request):
    data = People.objects.all()
    filter = BioExaminationDetailFilterAll(request.GET, queryset=data)
    table = PatientListTable(filter.qs)

    RequestConfig(request, paginate={'per_page': 20}).configure(table)
    return render(request, 'General/Generic_Table_view_filter_panel.html',
                  {'objects': table,
                   'filter' : filter,
                   'page_title': u'Ανάληση Εργαστηριακών για ',
                   'form_name':  u'Ανάληση Εργαστηριακών για ',
                   'param_action1': reverse('MedMOHApp:create'),
                   'param_action1_name': 'Προσθήκη'})



