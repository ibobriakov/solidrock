# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import ResumeView


__author__ = 'ir4y'

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', ResumeView.as_view()),
    )
