# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import create_resume_view, ResumeView, ResumePublicView, delete_resume_view


__author__ = 'ir4y'

urlpatterns = patterns(
    '',
    url(r'^create/$', create_resume_view, name='resume.create'),
    url(r'^(?P<pk>\d+)/$', ResumeView.as_view(), name='resume.edit'),
    url(r'^(?P<pk>\d+)/view$', ResumePublicView.as_view(), name='resume.view'),
    url(r'^(?P<resume_pk>\d+)/delete$', delete_resume_view, name='resume.delete'),
)
