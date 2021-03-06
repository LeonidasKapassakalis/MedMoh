from django.conf.urls import url


from . import views

from . import views_test

from models import Company
from dal import autocomplete



app_name = 'MedMOHApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),

#    url(r'^list/$', views.PublisherList.as_view(), name='list'),
    url(r'^list/$', views.person_list, name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.PeopleDetailView.as_view(), name='detail'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.PeopleUpdate.as_view(), name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.PeopleDelete.as_view(), name='delete'),
    url(r'^create/$', views.PeopleCreare.as_view(), name='create'),
    url(r'^listd/', views.doctor_list, name='doctor_list'),
    url(r'^listp/', views.patient_list, name='patient_list'),

#Exams
    url(r'^listexaminations/$', views.ExaminationDetailFilteredAll, name='listexaminations'),
    url(r'^listexaminationsf/$', views.ExaminationDetailFilteredAll, name='listexaminationsf'),
    url(r'^listexam/(?P<Patient>[0-9]+)/$', views.ExaminationList, name='listexam'),
    url(r'^detailexam/(?P<pk>[0-9]+)/$', views.ExaminationDetailView.as_view(), name='detailexam'),
    url(r'^updateexam/(?P<pk>[0-9]+)/$', views.ExaminationUpdate.as_view(), name='updateexam'),
    url(r'^deleteexam/(?P<pk>[0-9]+)/$', views.ExaminationDelete.as_view(), name='deleteexam'),
    url(r'^createexam/$', views.ExaminationCreare.as_view(), name='createexam'),

    url(r'^pdfviewexamination/(?P<id>[0-9]+)/$', views.pdf_view_examination, name='pdfviewexamination'),

    url(r'^examinationsper/([0-9]+)/$', views.ExaminationsListPer.as_view(), name='examinationsper'),
    url(r'^examinationsper1/([0-9]+)/$', views.examination_list_per, name='examinationspert'),
    url(r'^examinationsListPerDoctor/([0-9]+)/$', views.ExaminationsListPerDoctor.as_view(),name='examinationsListPerDoctor'),
    url(r'^examinationsListPerDoctorPatient/([0-9]+)/([0-9]+)/$', views.ExaminationsListPerDoctorPatient.as_view(),name='examinationsperdoctorpatient'),

#Medicine
    url(r'^listmedicine/(?P<Patient>[0-9]+)/$', views.MedicineList, name='listmedicine'),
    url(r'^detailmedicine/(?P<pk>[0-9]+)/$', views.MedicineDetailView.as_view(), name='detailmedicine'),
    url(r'^updatemedicine/(?P<pk>[0-9]+)/$', views.MedicineUpdate.as_view(), name='updatemedicine'),
    url(r'^deletemedicine/(?P<pk>[0-9]+)/$', views.MedicineDelete.as_view(), name='deletemedicine'),
    url(r'^createmedicine/$', views.MedicineCreare.as_view(), name='createmedicine'),

#medicinecategory
    url(r'^listmedicinecategory/$', views.MedicineCategoryList, name='listmedicinecategory'),
    url(r'^updatemedicinecategory/(?P<pk>[0-9]+)/$', views.MedicineCategoryUpdate.as_view(), name='updatemedicinecategory'),
    url(r'^createmedicinecategory/$', views.MedicineCategoryCreate.as_view(), name='createmedicinecategory'),


#examinationcategory
    url(r'^listexaminationcategory/$', views.ExaminationCategoryList, name='listexaminationcategory'),
#Change for django_addanother
#    url(r'^updateexaminationcategory/(?P<pk>[0-9]+)/$', views.ExaminationCategoryUpdate.as_view(), name='updateexaminationcategory'),
    url(r'^updateexaminationcategory/(?P<pk>.*)/$', views.ExaminationCategoryUpdate.as_view(), name='updateexaminationcategory'),
#Change for django_addanother
    url(r'^createexaminationcategory/$', views.ExaminationCategoryCreate.as_view(), name='createexaminationcategory'),


    # url(r'^testf/(?P<exampk>[0-9]+)/$', views_test.BioExaminationDetailFiltered, name='testf'),
    url(r'^testfa/$', views.BioExaminationDetailFilteredAll, name='testfa'),
    url(r'^testff/$', views_test.PeopleFiltered, name='testf'),
    url(r'^Graphos/$', views_test.Graphos, name='Graphos'),
    url(r'^someurl/$', views.someurl, name='someurl'),


#    url(r'^pdf_view/$', views.pdf_view, name='pdf_view'),
    url(r'^pdf_view/(?P<docid>[0-9]+)/$', views.pdf_view, name='pdf_view'),

    url(r'^listdoc/$', views.list, name='listdoc'),

    url(r'^listaaa/$', views.listaaa, name='listdocaaa'),


    url('^test-autocomplete/$', autocomplete.Select2QuerySetView.as_view(model=Company,create_field='name'), name='select2_fk',),

]