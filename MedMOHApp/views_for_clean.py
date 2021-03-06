# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404
from django import forms

from django.http import HttpResponseRedirect

import datetime

from models import *

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from .views import ModelFormWidgetMixin

from datetimewidget.widgets import DateTimeWidget, DateWidget , TimeWidget

import datatableview
from datatableview import Datatable, ValuesDatatable, columns, SkipRecord
from datatableview.views import DatatableView, MultipleDatatableView, XEditableDatatableView
from datatableview.views.legacy import LegacyDatatableView
from datatableview import helpers

import django_tables2 as tables

#DataTables
from django.views.generic import View, TemplateView
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import timesince





from django.shortcuts import render
def people0(request):
    return render(request, 'General/Generic_Table_view.html' , {'objects': People.objects.all(), 'add_url_leo': 'locationcreate' } )

from models import Examination
def examination00(request):
    return render(request, 'General/Generic_Table_view.html', {'objects': Examination.objects.all()})



def people10(request):
    return render(request, 'people0.html', {'my-table':Examname.objects.all()})


def detail(request, id):
    return HttpResponse("You're looking at question %s." % id)


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def current_datetime2(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def test(request):
    return render_to_response('mypage.html', {'title': 'Leonidas','current_section':'Kapa'})


def results(request, id):
    try:
        p=People.objects.get(pk=id)
        return render_to_response('myPeople.html', {'title': 'Leonidas', 'current_section': 'Kapa','p':p})
    except People.DoesNotExist:
        return HttpResponse("People does not exist")


def results0(request, id):
    try:
        p=People.objects.get(pk=id)
        response = "You're looking at the results of question %s %s." % (p.name,p.surname)
    except People.DoesNotExist:
        response = "People does not exist"
#        raise Http404("People does not exist")
#    return render(request,response)
    return HttpResponse(response)


def people_det(request, id):
    try:
        p = People.objects.get(pk=id)
        response = "You're looking for people %s %s." % (p.name, p.surname)
    except People.DoesNotExist:
        response = "People does not exist"
    return HttpResponse(response)


def vote(request,id):
    return HttpResponse("You're voting on question %s." % id)


def index(request):
    latest_question_list = People.objects.order_by('-name')[:5]
    output = ', '.join([q.name+' '+q.surname+'\n' for q in latest_question_list])
    return HttpResponse(output)
#    return HttpResponse(latest_question_list)


from forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
##            send_mail(
##                cd['subject'],
##                cd['message'],
##                cd.get('email', 'noreply@example.com'),
##                ['siteowner@example.com'],
##            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})




#Examination0
from models import Examination

def ExaminationsListPer000(request):
    queryset  = Examination.objects.all()
    table = Examination(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'Generic/Generic_Table_view.html', {'object_list': table})

from django.contrib.auth.decorators import login_required
#@login_required(login_url='/login/')

from django.conf import settings
from django.shortcuts import redirect

class ExaminationsList(LoginRequiredMixin,UserPassesTestMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Examination

    def test_func(self):
        return True

class ExaminationsList0(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,ListView):
    model = Examination

    def __init__(self, *args, **kwargs):
        super(ExaminationsList, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'notes',
                'peopleid',
                'categorid'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )

    def test_func(self):
        return True


class ExaminationsListPer(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Examination
##    template_name = 'examination_list_per_person.html'

#    queryset  = Examination0.dahl_objects.all()
#    queryset  = Examination0.leo_objects.all()
#    queryset  = Examination0.objects.filter(peopleid=1)
    def get_queryset(self):
        self.id = get_object_or_404(People,id=self.args[0])
        self.name = get_object_or_404(People,id=self.args[0])
        return Examination.objects.filter(peopleid=self.id)

    def get_context_data(self, **kwargs):
# Call the base implementation first to get a context
        context = super(ExaminationsListPer, self).get_context_data(**kwargs)
# Add in the publisher
        context['publisher'] = self.id
        context['name'] = u' για ' + self.name.surname + ' ' +  self.name.name
        return context

    def test_func(self):
        return True


class ExaminationsListPerDoctor(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Examination
##    template_name = 'examination_list_per_person.html'
    def get_queryset(self):
        self.id = get_object_or_404(People,id=self.args[0])
        self.name = get_object_or_404(People,id=self.args[0])
        return Examination.objects.filter(doctorid=self.id)

    def get_context_data(self, **kwargs):
        context = super(ExaminationsListPerDoctor, self).get_context_data(**kwargs)
        context['publisher'] = self.id
        context['name'] = u' απο ' +  self.name.surname
        return context

    def test_func(self):
        return True


class ExaminationsListPerDoctorPatient(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,ListView):
    model = Examination
##    template_name = 'examination_list_per_person.html'
    def get_queryset(self):
        self.did = get_object_or_404(People,id=self.args[0])
        self.dname = get_object_or_404(People,id=self.args[0])
        self.pid = get_object_or_404(People,id=self.args[1])
        self.pname = get_object_or_404(People,id=self.args[1])

        return Examination.objects.filter(doctorid=self.did,peopleid=self.pid)

    def get_context_data(self, **kwargs):
        context = super(ExaminationsListPerDoctorPatient, self).get_context_data(**kwargs)
        context['publisher'] = self.pid
        context['name'] = u' για ' + self.pname.name + ' ' + self.pname.surname + u' απο ' + self.dname.name + ' ' + self.dname.surname
        return context

    def test_func(self):
        return True


from models import ExaminationCategory

class ExaminationsListPerCategory(LoginRequiredMixin,UserPassesTestMixin,ModelFormWidgetMixin,ListView):
    model = Examination
    def get_queryset(self):
        self.id = get_object_or_404(ExaminationCategory,id=self.args[0])
        return Examination.objects.filter(categorid=self.id)

    def test_func(self):
        return True


from django.views.generic.detail import DetailView


from django.shortcuts import render

from  django.shortcuts import render_to_response
from django.template import RequestContext

def index1(request):
    example_form0 = ExampleForm0()
    return render_to_response("example_form0.html",
                              {"form": example_form0 ,"example_form0": example_form0},)

class ValidColumnFormatsView(TemplateView):
    template_name = "valid_column_formats.html"

import re

class DemoMixin(object):
    description = """Missing description!"""
    implementation = """Missing implementation details!"""

    def get_template_names(self):
        """ Try the view's snake_case name, or else use default simple template. """
        name = self.__class__.__name__.replace("DatatableView", "")
        name = re.sub(r'([a-z]|[A-Z]+)(?=[A-Z])', r'\1_', name)
        return [name.lower() + ".html", "example_base.html"]

    def get_context_data(self, **kwargs):
        context = super(DemoMixin, self).get_context_data(**kwargs)
        context['implementation'] = self.implementation

        # Unwrap the lines of description text so that they don't linebreak funny after being put
        # through the ``linebreaks`` template filter.
        alert_types = ['info', 'warning', 'danger']
        paragraphs = []
        p = []
        alert = False
        for line in self.__doc__.splitlines():
            line = line[4:].rstrip()
            if not line:
                if alert:
                    p.append(u"""</div>""")
                    alert = False
                paragraphs.append(p)
                p = []
            elif line.lower()[:-1] in alert_types:
                p.append(u"""<div class="alert alert-{type}">""".format(type=line.lower()[:-1]))
                alert = True
            else:
                p.append(line)
        description = "\n\n".join(" ".join(p) for p in paragraphs)
        context['description'] = re.sub(r'``(.*?)``', r'<code>\1</code>', description)

        return context


# Column configurations
class ZeroConfigurationDatatableView(DemoMixin, DatatableView):
    """
    If no columns are specified by the view's ``Datatable`` configuration object (or no
    ``datatable_class`` is given at all), ``DatatableView`` will use all of the model's local
    fields.  Note that this does not include reverse relationships, many-to-many fields (even if the
    ``ManyToManyField`` is defined on the model directly), nor the special ``pk`` field, but DOES
    include ``ForeignKey`` fields defined directly on the model.

    Note that fields will automatically use their ``verbose_name`` for the frontend table headers.

    WARNING:
    When no columns list is explicitly given, the table will end up trying to show foreign keys as
    columns, generating at least one extra query per displayed row.  Implement a ``get_queryset()``
    method on your view that returns a queryset with the appropriate call to ``select_related()``.
    """

    model = Examination

    implementation = u"""
    class ZeroConfigurationDatatableView(DatatableView):
        model = Entry
    """

# Column configurations

from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin.widgets import AdminTimeWidget
from django.contrib.admin.widgets import AdminSplitDateTime

from django.contrib.admin import widgets

class CustomAdminSplitDateTime(AdminSplitDateTime):
    def __init__(self, attrs=None):
        widgets = [AdminDateWidget, AdminTimeWidget(attrs=None, format='%I:%M %p')]
        forms.MultiWidget.__init__(self, widgets, attrs)

class MultiExamForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    phone = forms.CharField()
    mail = forms.EmailField(required=False)
    tk = forms.CharField()
    text = forms.CharField()
    #hospital = forms.NullBooleanField(db_column='Hospital')  # Field name made lowercase.
    #medicalcenter = models.NullBooleanField(db_column='MedicalCenter')  # Field name made lowercase.
    #eopyy = models.NullBooleanField(db_column='EOPYY')  # Field name made lowercase.
#    contact = forms.CharField()
    #countryid = forms.ForeignKey(Country, db_column='CountryId')  # Field name
    CHOICES = (('1', 'First',), ('2', 'Second',))
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    choice_field1 = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
#    choice_field2 = forms.SplitDateTimeField()
#    choice_field3 = forms.SplitDateTimeWidget()
    choice_field4 = forms.DateField(widget=widgets.AdminDateWidget())

#    start_datetime = forms.DateField(
#        widget=CustomAdminSplitDateTime())
#    end_datetime= forms.DateField(
#        widget=CustomAdminSplitDateTime())


    OPTIONS = (
                ("AUT", "Austria"),
                ("DEU", "Germany"),
                ("NLD", "Neitherlands"),
                ("GRE", "Greece"),
                )
    Countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)

    countries1 = forms.ModelChoiceField(queryset=People.objects.all())

    countries2 = forms.ModelMultipleChoiceField(queryset=People.objects.all())




def MultiExam(request):
    if request.method == 'POST':
        form = MultiExamForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd['mail']
            print cd['Countries']
            print cd['countries1']
            print cd['countries2']
##            send_mail(
##                cd['subject'],
##                cd['message'],
##                cd.get('email', 'noreply@example.com'),
##                ['siteowner@example.com'],
##            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = MultiExamForm()
    return render(request, 'contact_form.html', {'form': form})

def MultiExam0(request):
    if request.method == 'POST':
        form = MultiExamForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
##            send_mail(
##                cd['subject'],
##                cd['message'],
##                cd.get('email', 'noreply@example.com'),
##                ['siteowner@example.com'],
##            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = MultiExamForm()
    return render(request, 'contact_form0.html', {'form': form})





class ExaminationsListPerTable(tables.Table):
    detail = tables.LinkColumn('item_detail', args=[('pk')], orderable=False, empty_values=[''])
    edit = tables.LinkColumn('item_edit', args=[('pk')],orderable=False,empty_values=[''])
    delete = tables.LinkColumn('item_delete', args=[('pk')],orderable=False,empty_values=[''])
    class Meta:
        model = Examination
        row_attrs = {
            'data-id': lambda record: record.pk
        }
        attrs = {'class': 'paleblue'}
        exclude = ['id','nationality','idoncontry','ispatient','notes','isdoctor','canlogin','accessonlyhisfile','photo','notes']
#        fields
#        sequence = ['dateofexam','...']

    def render_edit(self, record):
        return mark_safe('<a href=/MedMOHApp/examinationupd/' + str(record.pk) + '/><span style="color:blue">Edit</span></a>')

    def render_delete(self, record):
        return mark_safe('<a href=/MedMOHApp/examinationdel/' + str(record.pk) + '/><span style="color:red">Delete</span></a>')

    def render_detail(self, record):
        return mark_safe('<a href=/MedMOHApp/examinationdet/' + str(record.pk) + '/><span style="color:green">View</span></a></a>')


def ExaminationsListPer_Table(request,pk):
    id = get_object_or_404(People, id=pk)
    table = ExaminationsListPerTable(Examination.objects.filter(peopleid=id))
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table})

#
def people10(request):
    queryset  = People.objects.all()
    table = PeopleTable(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table})

###MultiExamForm<


def examination_list_per(request,pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    id = get_object_or_404(People, id=pk)
    table = ExaminationTable(Examination.objects.filter(peopleid=pk))
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'people': table, 'page_title' : 'Εξετάσεις', 'add_url_leo': 'examinationcreate' })


