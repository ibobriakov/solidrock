# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import EmployerView, EmployerEditView, create_job_view, JobListView,\
    EditJobView, delete_job_view, JobPublicView, EmployerPublicView


urlpatterns = patterns(
    '',
    url(r'^$', EmployerView.as_view(), name='employer.profile.base'),
    url(r'^(?P<pk>\d+)/$', EmployerPublicView.as_view(), name='employer.profile.public'),
    url(r'^edit/$', EmployerEditView.as_view(), name='employer.profile.edit'),
    url(r'^job/create$', create_job_view, name='employer.job.create'),
    url(r'^job/list', JobListView.as_view(), name='employer.job.list'),
    url(r'^job/(?P<pk>\d+)/edit/$', EditJobView.as_view(), name='employer.job.edit'),
    url(r'^job/(?P<pk>\d+)/view/$', JobPublicView.as_view(), name='employer.job.view'),
    url(r'^job/(?P<pk>\d+)/delete/$', delete_job_view, name='employer.job.delete'),
)
