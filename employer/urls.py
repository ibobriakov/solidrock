# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import EmployerView, CreateJobView, EditJobView, delete_job_view


urlpatterns = patterns(
    '',
    url(r'^$', EmployerView.as_view(), name='employer.profile.base'),
    url(r'^job/create$', CreateJobView.as_view(), name='employer.job.create'),
    url(r'^job/(?P<pk>\d+)/edit$', EditJobView.as_view(), name='employer.job.edit'),
    url(r'^job/(?P<pk>\d+)/delete$', delete_job_view, name='employer.job.delete'),
    )
