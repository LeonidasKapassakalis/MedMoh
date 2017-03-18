"""MedMOHApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from DjgLeoApp001 import views
from DjgLeoApp001 import models
from DjgLeoApp001 import forms

#from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^menu/', views.NewMenu),
    url(r'^menu1/', views.NewMenu1),
    url(r'^MedMOHApp/', include('MedMOHApp.urls')),
    url(r'^contact999/$',views.ZeroConfigurationDatatableView.as_view(), name='contact999'),
    url(r'^contact998/$',views.ZeroConfigurationDatatableView0.as_view(), name='contact998'),
    url(r'^multiexam/$', views.MultiExam, name='MultiExamForm'),
    url(r'^multiexam0/$', views.MultiExam0, name='MultiExamForm0'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),
    url(r'^admin/', admin.site.urls),
    url(r'', views.MainMenu, name='MainMenu'),
]
