# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import EmployerView, EmployerEditView, create_job_view, JobListView,\
    EditJobView, delete_job_view, JobPublicView, EmployerPublicView


urlpatterns = patterns(
    '',
    url(r'^$', EmployerEditView.as_view(), name='employer.profile.base'),
)
